from pydantic import BaseModel, Field, field_validator
import re


class User(BaseModel):
    name: str
    id: int

class User2(BaseModel):
    name: str
    age: int

class Feedback(BaseModel):
    name: str
    message: str

class Feedback2(BaseModel):
    name: str = Field(min_length=2, max_length=50)
    message: str = Field(min_length=10, max_length=500)

    @field_validator("message")
    @classmethod
    def check_bed_words(cls, value: str):
        bad_words = ["редиск", "бяк", "козявк"]
        text = value.lower()
        for word in bad_words:
            pattern = rf"\b{word}\w\b"
            if re.search(pattern, text):
                raise ValueError("Использование недопустимых слов")
        return value