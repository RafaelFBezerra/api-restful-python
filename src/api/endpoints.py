from fastapi import APIRouter, Depends, HTTPException

from models.table_models import ClientTable
from models.table_models import ProductTable
from utils.init_db_objects import db_session
from utils.build_json_responses import responses_builder
from utils.mappers import API_CONSUMER_PAYLOAD_REQUEST_MAPPER
from clients.db_client_table import DBClientTable
from clients.db_product_table import DBProductTable
from schemas.client_table_schemas import InsertClientTable, ReadClientTable, UpdateClientTable, DeleteClientTable
from schemas.product_table_schemas import InsertProductTable, GetProductTable
from api.consumer import consume_api_by_id


router = APIRouter()


@router.post("/insert-client-data")
async def insert_client_data(request_payload: InsertClientTable, db_session=Depends(db_session)):
    db_client = DBClientTable(
        table=ClientTable,
        db_session=db_session
    )

    data_return = db_client.insert_client(request_payload)
    
    db_session.commit()
    db_session.refresh(data_return)

    return responses_builder(
        status_code=200,
        status_message="Sucesso ao inserir cliente na tabela de clientes",
        data=data_return
    )


@router.get("/get-client-data")
async def get_client_data(request_payload: ReadClientTable, db_session=Depends(db_session)):
    db_client = DBClientTable(
        table=ClientTable,
        db_session=db_session
    ) 

    data_return = db_client.get_client(request_payload)
    if data_return is None:
        status_code = 404
        status_messsage = f"ID {request_payload.cliente_id} não encontrado na tabela de clientes"

        raise HTTPException(status_code=status_code, detail=status_messsage)

    return responses_builder(
        status_code=200,
        status_message="Sucesso ao buscar dados do cliente na tabela de clientes",
        data=data_return
    )


@router.put("/update-client-data")
async def update_client_data(request_payload: UpdateClientTable, db_session=Depends(db_session)):
    db_client = DBClientTable(
        table=ClientTable,
        db_session=db_session
    )

    data_return = db_client.update_client(request_payload)
    if data_return is None:
        status_code = 404
        status_messsage = f"ID {request_payload.cliente_id} não encontrado na tabela de clientes"

        raise HTTPException(status_code=status_code, detail=status_messsage)
    
    db_session.commit()
    db_session.refresh(data_return)

    return responses_builder(
        status_code=200,
        status_message="Sucesso ao atualizar dados do cliente na tabela de clientes",
        data=data_return
    )

@router.delete("/delete-client-data")
async def delete_client_data(request_payload: DeleteClientTable, db_session=Depends(db_session)):
    db_client = DBClientTable(
        table=ClientTable,
        db_session=db_session
    )

    data_return = db_client.delete_client(request_payload)
    if data_return is None:
        status_code = 404
        status_messsage = f"ID {request_payload.cliente_id} não encontrado na tabela de clientes"

        raise HTTPException(status_code=status_code, detail=status_messsage)

    db_session.commit()

    return responses_builder(
        status_code=200,
        status_message="Sucesso ao deletar dados do cliente na tabela de clientes",
        data=data_return
    )


@router.get("/get-all-client-data")
async def get_all_client_data(db_session=Depends(db_session)):
    db_client = DBClientTable(
        table=ClientTable,
        db_session=db_session
    )

    data_return = db_client.get_all_client()

    return responses_builder(
        status_code=200,
        status_message="Sucesso ao buscar todos os dados dos clientes na tabela de clientes",
        data=data_return
    )


@router.post("/insert-favorite-client-product-data")
async def insert_favorite_client_product_data(request_payload: InsertProductTable, db_session=Depends(db_session)):
    validate_product_response = consume_api_by_id(request_payload.id_produto)
    if validate_product_response.status_code != 200:
        raise HTTPException(status_code=validate_product_response.status_code, detail="Falha ao consumir API para validar os produtos")
    
    text_response = validate_product_response.text.strip()
    if text_response == "":
        raise HTTPException(status_code=400, detail="ID do produto informado não encontrado na API de produtos")
    
    product_json_data = validate_product_response.json()
    for key, value in product_json_data.items():
        atribute_name = API_CONSUMER_PAYLOAD_REQUEST_MAPPER.get(key)
        if atribute_name is None:
            continue
        
        if str(value).strip() != str(getattr(request_payload, atribute_name)).strip():
            raise HTTPException(status_code=400, detail=f"O atributo [{atribute_name}] com valor [{getattr(request_payload, atribute_name)}] não está em conformidade com o valor [{value}] da API referência!")

    db_client = DBClientTable(
        table=ClientTable,
        db_session=db_session
    )
    
    client_data = db_client.get_client(request_payload)
    if client_data is None:
        status_code = 404
        status_messsage = f"ID {request_payload.cliente_id} não encontrado na tabela de clientes para inserir produto favorito"

        raise HTTPException(status_code=status_code, detail=status_messsage)

    db_product = DBProductTable(
        table=ProductTable,
        db_session=db_session
    )

    data_return = db_product.insert_favorite_products(request_payload)

    db_session.commit()
    db_session.refresh(data_return)

    return responses_builder(
        status_code=200,
        status_message="Sucesso ao inserir produto favorito na tabela de produtos",
        data=data_return
    )


@router.get("/get-all-favorite-products-by-client-id")
async def get_all_favorite_products_by_client_id(request_payload: GetProductTable, db_session=Depends(db_session)):
    db_client = DBClientTable(
        table=ClientTable,
        db_session=db_session
    )
    
    db_product = DBProductTable(
        table=ProductTable,
        db_session=db_session
    )

    client_data = db_client.get_client(request_payload)
    if client_data is None:
        status_code = 404
        status_messsage = f"ID {request_payload.cliente_id} não encontrado na tabela de clientes para inserir produto favorito"

        raise HTTPException(status_code=status_code, detail=status_messsage)

    data_return = db_product.get_favorite_products_by_id(request_payload)
    if data_return is None:
        status_code = 404
        status_messsage = f"Produtos não encontrados para o ID {request_payload.cliente_id}"

        raise HTTPException(status_code=status_code, detail=status_messsage)

    return responses_builder(
        status_code=200,
        status_message="Sucesso ao buscar todos os produtos favoritos para o ID informado",
        data=data_return
    )
