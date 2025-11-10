# Projeto de API Restful Python

Este é um projeto de API Restful Python que utiliza o FastAPI e SQLAlchemy. A API permite que os usuários realizem operações CRUD em tabelas de clientes e produtos favoritos.

## Configuração

Antes de executar o projeto, certifique-se de ter as seguintes dependências instaladas:

- Docker

Siga as instruções abaixo para configurar o projeto:

1. Clone este repositório para o seu ambiente local.

2. Crie um arquivo chamado `.env` na raiz do projeto e defina as seguintes variáveis de ambiente:
    DB_HOST=<host_do_banco_de_dados>
    DB_PORT=<porta_do_banco_de_dados>
    DB_NAME=<nome_do_banco_de_dados>
    DB_USER=<usuario_do_banco_de_dados>
    DB_PASSWORD=<senha_do_banco_de_dados>

3. Execute o seguinte comando para construir a imagem Docker:
    docker build -t api-restful-python

4. Execute o seguinte comando para executar a imagem Docker:
    docker run -p 8000:8000 api-restful-python

Isso iniciará a API no endereço `http://<IP publico do servidor onde o docker está hospedado>:8000`.

## Endpoints

Abaixo estão os endpoints disponíveis na API:

### Clientes

- `POST /clients`: Inserir um novo cliente.
- `GET /clients`: Buscar todos os clientes.
- `GET /clients/data`: Buscar dados de um cliente específico (busca pelo ID).
- `PUT /clients`: Atualizar dados de um cliente.
- `DELETE /clients`: Excluir um cliente.

### Produtos Favoritos

- `POST /products/favorites`: Inserir um novo produto favorito na tabela de produtos favoritos.
- `GET /products/favorites/by-client`: Buscar todos os produtos favoritos de um cliente.


### Documentação API
Para acessar a documentação da API, acesse a rota http://<IP publico do servidor onde o docker está hospedado>:8000/docs
