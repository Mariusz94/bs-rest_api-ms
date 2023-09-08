import config
from flask import Flask, jsonify
from service.logs_service.app_logs import config_logs, init_logging

app = Flask(__name__)


@app.route("/", methods=["GET"])
def welcome():
    """
    Funkcja sprawdzająca dostępność mikroserwisu.

    Returns:
        json: Informacja o serwisie.
    """
    return jsonify({"info": "server works"}), 200


if __name__ == "__main__":
    init_logging()
    config_logs()
    app.run(debug=False, port=config.SERVICE_PORT, host="0.0.0.0", use_reloader=False)
