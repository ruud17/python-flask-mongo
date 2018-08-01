from flask import Flask, request, jsonify, abort
from models.ServerUsage import ServerUsage
import datetime
import services.server_usage as server_usage_service
import services.analytics as analytics_service
from db.connection import connect_to_db

connect_to_db()
app = Flask(__name__)


@app.route('/usage', methods=['POST'])
def server_usage():
    req_data = request.get_json()
    try:
        server_usage_data = server_usage_service.prepare_data_to_save(req_data)
        server_usage_data.save()
        return jsonify(message="Successfully added server usage for the server {0}".format(server_usage_data.name))
    except Exception as e:
        return jsonify(error=str(e))


@app.route('/analytics')
def analytics():
    server_name = request.args.get('server_name')
    start_datetime = request.args.get('start_datetime')
    end_datetime = request.args.get('end_datetime') or datetime.datetime.utcnow()

    if (server_name is None and start_datetime is None):
        abort(400, 'Please set server name or start datetime as a query param')
    else:
        try:
            query_response = analytics_service.get_query_data(server_name, start_datetime, end_datetime)

            response_data = analytics_service.create_response_data(server_name, start_datetime, end_datetime,
                                                                   query_response)
            return jsonify(response_data)
        except Exception as e:
            return jsonify(error=str(e))


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
