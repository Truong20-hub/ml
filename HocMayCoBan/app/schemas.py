from pydantic import BaseModel


class PropertyData(BaseModel):
    area: float
    rooms: int
    distance: float
