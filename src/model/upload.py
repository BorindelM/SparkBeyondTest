from pydantic import BaseModel

class Upload(BaseModel):
    filename: str
    filelocation: str
    content: str