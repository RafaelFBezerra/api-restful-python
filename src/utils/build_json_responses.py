def responses_builder(status_code: int, status_message: str, data: dict) -> dict:
    return {"status_code": status_code, "status_message": status_message, "data_return": data}
