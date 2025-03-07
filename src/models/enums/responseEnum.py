from enum import Enum

class ResponseSignal(Enum):
    FILE_TYPE_NOT_ALLOWED = "File type not allowed"
    FILE_SIZE_TOO_LARGE = "File size too large"
    FILE_UPLOAD_SUCCESS = " file upload success"
    FILE_UPLOAD_FAILED = "file upload failed"
    FILE_VALIDATION_SUCCESS = "file validation success"
    FILE_VALIDATION_FAILED = "file validation failed"