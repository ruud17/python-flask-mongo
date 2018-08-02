from models.ServerUsage import ServerUsage


def get_query_data(server_name, start_datetime, end_datetime):
    if (server_name is not None and start_datetime is not None):
        return ServerUsage.objects(name=server_name, start_datetime__gte=start_datetime,
                                   start_datetime__lte=end_datetime).order_by('start_datetime')
    elif (server_name is not None):
        return ServerUsage.objects(name=server_name, start_datetime__lte=end_datetime).order_by('start_datetime')
    else:
        return ServerUsage.objects(start_datetime__gte=start_datetime, start_datetime__lte=end_datetime).order_by(
            'start_datetime')


def get_response_data(server_name, start_datetime, end_datetime, query_response, split_by):
    response_data = {
        "server_name": server_name,
        "start_datetime": start_datetime,
        "end_datetime": end_datetime,
        "data": list()
    }
    created_response_data = create_response_data(query_response, split_by)
    response_data["data"].append(created_response_data)

    return response_data


def create_response_data(query_response, split_by):
    data = []
    for server_usage in query_response:

        if (split_by is None):
            data.append({
                "cpus": server_usage.cpus,
                "disk": server_usage.disk.to_mongo(),
                "memory": server_usage.memory.to_mongo(),
                "network": server_usage.network.to_mongo(),
                "start_datetime": server_usage.start_datetime
            })
        else:
            items = server_usage[split_by] if split_by == 'cpus' else server_usage[split_by].to_mongo()
            data.append({
                split_by: items,
                "start_datetime": server_usage.start_datetime
            })

    return data
