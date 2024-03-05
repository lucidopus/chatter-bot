import os
from langchain.callbacks.manager import CallbackManager
from langchain.callbacks.streaming_stdout import StreamingStdOutCallbackHandler

# API Configurations

API_KEY = os.getenv("API_KEY")


# Groq Configurations

GROQ_API_KEY = os.getenv("GROQ_API_KEY")
GROQ_MODEL = os.getenv("GROQ_MODEL")


# Azure Configurations

AZURE_COMMON_PARAMS = {
    "openai_api_base": os.getenv("AZURE_OPENAI_API_BASE"),
    "openai_api_version": os.getenv("AZURE_OPENAI_API_VERSION"),
    "openai_api_key": os.getenv("AZURE_OPENAI_API_KEY"),
    "openai_api_type": os.getenv("AZURE_OPENAI_API_TYPE"),
}

AZURE_OPENAI_PARAMS = {
    "streaming": True,
    "callback_manager": CallbackManager([StreamingStdOutCallbackHandler()]),
    "deployment_name": os.getenv("AZURE_OPENAI_DEPLOYMENT_NAME_GPT_35"),
    **AZURE_COMMON_PARAMS,
}
# Embedding model Configurations

AZURE_ADA_PARAMS = {
    "deployment": os.getenv("AZURE_OPENAI_EMBEDDINGS_MODEL"),
    **AZURE_COMMON_PARAMS,
}


# Pinecone Configurations

PINECONE_CONFIG = {
    "PINECONE_API_KEY": os.getenv("PINECONE_API_KEY"),
    "PINECONE_ENV": os.getenv("PINECONE_ENV"),
}
PINECONE_INDEX = os.getenv("PINECONE_INDEX")


# MongoDB Configurations

MONGODB_URI = os.getenv("MONGODB_URI")
