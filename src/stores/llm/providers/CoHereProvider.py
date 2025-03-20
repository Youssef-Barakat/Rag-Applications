from ..LLMInterface import LLMInterface
from ..LLMEnums import CohereEnums, DocumentTypeEnum
import cohere
import logging

class CoHereProvider(LLMInterface):
    def __init__(self, api_key: str, 
                 default_input_max_characters: int = 1000,
                 default_output_max_tokens: int = 1000,
                 default_generation_temperature: float=.1):
        
        self.api_key = api_key
        self.default_input_max_characters = default_input_max_characters
        self.default_output_max_tokens = default_output_max_tokens
        self.default_generation_temperature = default_generation_temperature
        
        self.generation_model_id = None 
        
        self. embedding_model_id = None
        self.embedding_size = None 
        
        self.client = cohere.Client(
            api_key=self.api_key,
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
            self.logger.error("Cohere client not initialized")
            return None 
        
        if not self.generation_model_id:
            self.logger.error("No generation model for Cohere set")
            return None
    
        max_output_length = max_output_length if max_output_length else self.default_output_max_tokens
        temperature = temperature if temperature else self.default_generation_temperature
                
        response = self.client.chat(
            model= self.generation_model_id,
            chat_history= chat_history,
            message= self.process_text(prompt),
            temperature=temperature,
            max_tokens= max_output_length
        )
        
        if not response or not response.text:
            self.logger.error("No response from Cohere while generating text")
            return None 
        
        return response.text
            
            
    def embed_text(self, text: str, document_type: str = None):
        
        if not self.client:
            self.logger.error("Cohere client not initialized")
            return None 
        
        if not self.embedding_model_id:
            self.logger.error("No embedding model for Cohere set")
            return None
        
        input_type = CohereEnums.DOCUMENT.value 
        if document_type == DocumentTypeEnum.QUERY.value:
            input_type = CohereEnums.QUERY.value
            
        response = self.client.embed(   
            model = self.embedding_model_id,
            texts = [self.process_text(text)],
            input_type = input_type,
            embedding_types = ['float']
        )
        
        if not response or not response.embeddings or not response.embeddings.float :
            self.logger.error("No embeddings returned with Cohere")
            return None
        
        return response.embeddings.float[0]
    
    def construct_prompt(self, prompt: str, role: str):
        return {
            "role": role,
            "content": self.process_text(prompt)
        }