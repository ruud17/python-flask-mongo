from mongoengine import *


class Memory(EmbeddedDocument):
    total = IntField()
    available = IntField()
    percent = FloatField()
    used = IntField()
    free = IntField()
    active = IntField()
    inactive = IntField()
    wired = IntField()
