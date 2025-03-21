from ..LLMInterface import LLMInterface
from ..LLMEnums import OpenAIEnums
from openai import OpenAI
import logging

class OpenAIProvider(LLMInterface):
    def __init__(self, api_key: str, api_url: str = None, 
                 default_input_max_characters: int = 1000,
                 default_output_max_tokens: int = 1000,
                 default_generation_temperature: float=.1):
        
        self.api_key = api_key
        self.api_url = api_url
        self.default_input_max_characters = default_input_max_characters
        self.default_output_max_tokens = default_output_max_tokens
        self.default_generation_temperature = default_generation_temperature
        
        self.generation_model_id = None 
        
        self. embedding_model_id = None
        self.embedding_size = None 
        
        self.client = OpenAI(
            api_key=self.api_key,
            #base_url = self.api_url if self.api_url and len(self.api_url) else None
        )
        
        self.logger = logging.getLogger(__name__)
        
    def set_generation_model(self, model_id: str):
        self.generation_model_id = model_id
        
    def set_embedding_model(self, model_id: str, embedding_size: int):
        self.embedding_model_id = model_id
        self.embedding_size = embedding_size
    
    def process_text(self, text: str):
        return text[:self.default_input_max_characters].strip()
            
    def generate_text(self, prompt: str, chat_history: list=[], max_output_length: int = None,
                      temperature: float = None):
        
        if not self.client:
            self.logger.error("OpenAI client not initialized")
            return None 
        
        if not self.generation_model_id:
            self.logger.error("No generation model for openai set")
            return None
    
        max_output_length = max_output_length if max_output_length else self.default_output_max_tokens
        temperature = temperature if temperature else self.default_generation_temperature
        
        chat_history.append(self.construct_prompt(prompt, OpenAIEnums.USER.value))
        
        response = self.client.chat.completions.create(
            model=self.generation_model_id,
            messages=chat_history,
            max_tokens=max_output_length,
            temperature=temperature
        )
        
        if not response or not response.choices or len(response.choices) == 0 or not response.choices[0].message:
            self.logger.error("No response from OpenAI while generating text")
            return None 
        
        return response.choices[0].message['content']
            
            
    def embed_text(self, text: str, document_type: str = None):
        
        if not self.client:
            self.logger.error("OpenAI client not initialized")
            return None 
        
        if not self.embedding_model_id:
            self.logger.error("No embedding model for OpenAI set")
            return None
        
        response = self.client.embeddings.create(
            model = self.embedding_model_id,
            input = text
        )
        
        if not response or not response.data or len(response.data) == 0 or not response.data[0].embeddings :
            self.logger.error("No embeddings returned with OpenAI")
            return None
        
        return response.data[0].embeddings
    
    def construct_prompt(self, prompt: str, role: str):
        return {
            "role": role,
            "content": self.process_text(prompt)
        }