from pydantic import BaseModel, ConfigDict


class Item(BaseModel):
    age: int
    skills: float


class Items(BaseModel):
    items: list[Item]

    model_config = ConfigDict(
        json_schema_extra={
            "examples": [
                {"items": [{"age": 20, "skills": 0.3}, {"age": 49, "skills": -0.5}]}
            ]
        },
    )
