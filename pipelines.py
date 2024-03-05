from utils.helper import ask_mixtral
from utils.models import MessageRequest


def get_model_response(request: MessageRequest):
    system_prompt = request.system_prompt
    user_message = request.user_message

    messages = [
        {
            "role": "system",
            "content": system_prompt,
        },
        {
            "role": "user",
            "content": user_message,
        },
    ]

    response = ask_mixtral(messages)

    return response
