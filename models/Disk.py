from mongoengine import *


class Disk(EmbeddedDocument):
    total = IntField()
    used = IntField()
    free = IntField()
    percent = FloatField()
