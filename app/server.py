import config
from flask import Flask, jsonify
from service.logs_service.app_logs import config_logs, init_logging
import service.api_service as api_service
app = Flask(__name__)


@app.route("/", methods=["GET"])
def welcome():
    """
    Funkcja sprawdzająca dostępność mikroserwisu.

    Returns:
        json: Informacja o serwisie.
    """
    return jsonify({"info": "server works"}), 200


@app.route("/checkBalance/userID={user_id}", methods=["GET"])
def check_balance(user_id: str):
    """
    Funkcja sprawdzająca dostępność środków.

    Returns:
        json: Informacja o liczbie środków.
    """
    dict_data = api_service.check_balance()
    return jsonify(dict_data), 200


if __name__ == "__main__":
    init_logging()
    config_logs()
    app.run(debug=False, port=config.SERVICE_PORT, host="0.0.0.0", use_reloader=False)
