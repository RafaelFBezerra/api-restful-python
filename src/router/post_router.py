from fastapi import APIRouter
from models.base_models import PayloadRequestModel
from utils.build_json_responses import responses_builder


router = APIRouter()


@router.post("/api/validate-request-data")
async def validate_request_data(payload_request: PayloadRequestModel):
    return responses_builder(
        status_code=200,
        status_message="Sucess to validate request data",
        data=payload_request
    )
