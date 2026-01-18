from peewee import Model, TextField, DateTimeField
from datetime import datetime

from app.database.db import db


class BaseModel(Model):
    class Meta:
        database = db


class SearchHistory(BaseModel):
    user_id = TextField()
    command = TextField()
    query = TextField()
    created_at = DateTimeField(default=datetime.now)
