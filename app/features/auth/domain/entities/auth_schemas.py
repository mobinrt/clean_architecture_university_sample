from pydantic import BaseModel

class TokenDisplay(BaseModel):
    access_token: str
    token_type: str

    model_config = {
        'from_attributes': True
    }