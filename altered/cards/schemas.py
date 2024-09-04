from ninja import Schema
from .models import Card
from ninja.orm import create_schema

CardSchema = create_schema(Card, depth=2, name='Card')

class RatingsUploadSchema(Schema):
    id: str
    faction: str


class Error(Schema):
    message: str
