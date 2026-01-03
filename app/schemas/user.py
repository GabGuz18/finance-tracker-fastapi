from pydantic import BaseModel, EmailStr
import uuid

class UserOut(BaseModel):
    id_user: uuid.UUID
    first_name: str
    last_name: str
    email: EmailStr
