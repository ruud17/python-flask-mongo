from models.ServerUsage import ServerUsage


def prepare_data_to_save(req_data):
    name = req_data.get('name')
    cpus = req_data.get('cpus')
    disk = req_data.get('disk')
    memory = req_data.get('memory')
    network = req_data.get('network')
    start_datetime = req_data.get('start_datetime')
    return ServerUsage(name=name, cpus=cpus, disk=disk, memory=memory, network=network, start_datetime=start_datetime)
