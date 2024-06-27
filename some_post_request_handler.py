from pydantic import BaseModel


class Data(BaseModel):
    field: str


def handle_post_endpoint(data: Data):
    return {"message": f"Received data: {data.field}"}
