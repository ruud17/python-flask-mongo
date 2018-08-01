from mongoengine import *
import datetime
from .Disk import Disk
from .Memory import Memory
from .Network import Network


class ServerUsage(Document):
    name = StringField(required=True)
    # psutil.cpu_percent(interval=1, percpu=True) -> [15.8, 1.6, 11.8, 1.4, 11.9, 1.4, 11.7, 1.4] example cpu usage per percent
    cpus = ListField(FloatField())
    # psutil.disk_usage('/') -> sdiskusage(total=250685575168, used=62146027520, free=181418029056, percent=25.5)
    disk = EmbeddedDocumentField(Disk)
    # psutil.virtual_memory() -> svmem(total=17179869184, available=3044286464, percent=82.3, used=10901143552, free=2864283648, active=6877986816, inactive=180002816, wired=3843153920)
    memory = EmbeddedDocumentField(Memory)
    # psutil.net_io_counters(pernic=False, nowrap=True) -> snetio(bytes_sent=2131083264, bytes_recv=17704563712, packets_sent=9946538, packets_recv=17503563, errin=0, errout=0, dropin=0, dropout=0)
    network = EmbeddedDocumentField(Network)
    start_datetime = DateTimeField(default=datetime.datetime.utcnow)
