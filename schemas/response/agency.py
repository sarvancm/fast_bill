from pydantic import BaseModel

class AgencyOut(BaseModel):
    id:int
    name: str
    email: str
    branch: str
    address_1: str
    address_2: str
    city: str
    state: str
    gstin: str
    # pin: Optional[str] 
    district: str


class CatOut(BaseModel):
    name: str
