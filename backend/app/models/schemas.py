from pydantic import BaseModel

class UserRequest(BaseModel):
    input: str
