from pydantic import BaseModel


class MessageRequest(BaseModel):
    system_prompt: str
    user_message: str
