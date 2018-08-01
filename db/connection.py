from mongoengine import connect


def connect_to_db():
    connect(db='bpu_server_resources')
