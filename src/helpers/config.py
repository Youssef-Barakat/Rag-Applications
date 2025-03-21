from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    
    APP_NAME : str
    OPENAI_API_KEY : str
    
    FILE_ALLOWED_TYPES : list
    FILE_MAX_SIZE: int 
    FILE_DEFAULT_CHUNK_SIZE : int
    
    MONGODB_URL : str 
    MONGODB_DATABASE : str
    
    GENERATION_BACKEND: str
    EMBEDDING_BACKEND: str
    
    OPENAI_API_KEY: str
    OPENAI_API_URL: str
    COHERE_API_KEY: str
    
    GENERATION_MODEL_ID: str
    EMBEDDING_MODEL_ID: str
    EMBEDDING_MODEL_SIZE: int
    
    INPUT_DEFAULT_MAX_CHARS: int
    GENERATION_DEFAULT_MAX_TOKENS: int
    GENERATION_DEFAULT_TEMPERATURE: float
    
    ## ======================== Vector DB Config ========================
    VECTOR_DB_BACKEND: str
    VECTOR_DB_PATH: str
    VECTOR_DB_DISTANCE_METHOD: str
    
    
    class Config:
        env_file = ".env"
        
def get_settings():
    return Settings()
