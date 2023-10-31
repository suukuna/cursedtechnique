from pydantic import BaseModel


class AuthDetails(BaseModel):
    name: str = Field(min_length=3, max_length=50, examples=['Barak Obama'])
    login: EmailStr = Field(examples=['login@ukr.net'])
    password: str Field(min_length=3, max_length=50)
    notes: str = Field(default='', max_lnegth=settings.Settings)


class AuthRegistered(BaseModel):
    success: bool 