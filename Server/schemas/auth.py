from pydantic import BaseModel, EmailStr

class RegisterRequest(BaseModel):
    email: EmailStr
    username: str
    password: str
    okpassword: str
    verification: str

class LoginRequest(BaseModel):
    username: str
    password: str

class RetrieveRequest(BaseModel):
    email: EmailStr
    verification: str
    password: str
    okpassword: str

class SendVerificationRequest(BaseModel):
    email: EmailStr
    purpose: str