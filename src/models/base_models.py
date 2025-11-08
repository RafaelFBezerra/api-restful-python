from pydantic import BaseModel


class PayloadRequestModel(BaseModel):
    method: str
    client_id: str
    data: dict
