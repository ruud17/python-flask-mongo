from mongoengine import *


class Network(EmbeddedDocument):
    bytes_sent = IntField()
    bytes_recv = IntField()
    packets_sent = IntField()
    packets_recv = IntField()
    errin = IntField()
    errout = IntField()
    dropin = IntField()
    dropout = IntField()
