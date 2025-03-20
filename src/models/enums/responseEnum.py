from enum import Enum

class ResponseSignal(Enum):
    FILE_TYPE_NOT_ALLOWED = "File type not allowed"
    FILE_SIZE_TOO_LARGE = "File size too large"
    FILE_UPLOAD_SUCCESS = " file upload success"
    FILE_UPLOAD_FAILED = "file upload failed"
    FILE_VALIDATION_SUCCESS = "file validation success"
    FILE_VALIDATION_FAILED = "file validation failed"
    PROCESSING_FAILED = "processing failed"
    PROCESSING_SUCCESS = "processing success"
    NO_FILES_ERROR = "not found files"
    FILE_ID_ERROR = "no_file_found_with_this_id"
    PROJECT_NOT_FOUND_ERROR = "project_nout_found"
    INSERT_INTO_DB_ERROR = "insert_into_db_error"
    INSERT_INTO_DB_SUCCESS = "insert_into_db_success"
    VECTORDB_COLLECTION_RETRIEVED = "vectordb_collection_retrieved"
    VECTORDB_SEARCH_SUCCESS = "vectordb_search_success"
    VECTORDB_SEARCH_ERROR = "vectordb_search_error"