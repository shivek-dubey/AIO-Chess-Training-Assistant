from pydantic import BaseModel
from typing import List


class PlayerProfile(BaseModel):
    name: str
    age_group: str
    rating: int | None = None
    strengths: List[str] = []
    improvement_areas: List[str] = []
    preferred_openings: List[str] = []
