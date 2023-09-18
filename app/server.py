import jwt
import config
from flask import Flask, jsonify, request
from service.logs_service.app_logs import config_logs, init_logging
import service.api_service as api_service

app = Flask(__name__)
app.config['SECRET_KEY'] = 'supersecretkey'


@app.route("/", methods=["GET"])
def welcome():
    """
    Method used to check the service.

    Returns:
        json: Service information.
    """
    return jsonify({"info": "server works"}), 200


@app.route("/checkBalance/userID={user_id}", methods=["GET"])
def check_balance(user_id: str):
    """
    Method that allows obtaining the balance for a user by user id.

    Args:
        user_id (str): User Id.

    Returns:
        dict: Balance information.
    """
    dict_data = api_service.check_balance()
    return jsonify(dict_data), 200


@app.route("/makeWithdrawal/userID={user_id}", methods=["GET"])
def make_withdrawal(user_id: str):
    """
    Method used to make a withdrawal.

    Args:
        user_id (str): User Id.

    Returns:
        dict: Information about the withdrawal.
    """
    dict_data = api_service.make_withdrawal()
    return jsonify(dict_data), 200


@app.route("/makeDeposit/userID={user_id}", methods=["GET"])
def make_deposit(user_id: str):
    """
    Method used to make a deposit.

    Args:
        user_id (str): User Id.

    Returns:
        json: Information about the deposit.
    """
    dict_data = api_service.make_deposit()
    return jsonify(dict_data), 200


@app.route("/makeTransfer/userID={user_id}", methods=["GET"])
def make_transfer(user_id: str):
    """
    Method used to make a transfer.

    Args:
        user_id (str): User Id.

    Returns:
        json: Transfer result.
    """
    dict_data = api_service.make_transfer()
    return jsonify(dict_data), 200


@app.route("/getAccountStatement/userID={user_id}", methods=["GET"])
def get_account_statement(user_id: str):
    """
    Method used to get an account statement.

    Args:
        user_id (str): User Id.

    Returns:
        json: Account statement.
    """
    dict_data = api_service.get_account_statement()
    return jsonify(dict_data), 200


@app.route("/login", methods=["POST"])
def login():
    """
    Method used to log in a user.

    Returns:
        dict: User information and JWT tokens.
    """
    data = request.get_json()
    login = data.get("login")
    password = data.get("password")

    try:
        user_info = api_service.login(login, password)
        if user_info:
            access_token = jwt.encode({'login': login}, app.config['SECRET_KEY'], algorithm='HS256')
            secret_token = jwt.encode({'login': login}, app.config['SECRET_KEY'], algorithm='HS256')

            user_info['access_token'] = access_token
            user_info['secret_token'] = secret_token

            return jsonify(user_info), 200
        else:
            return jsonify({'message': 'Invalid credentials'}), 401
    except Exception as e:
        return jsonify({'message': 'Login failed', 'error': str(e)}), 500


if __name__ == "__main__":
    init_logging()
    config_logs()
    app.run(debug=False, port=config.SERVICE_PORT, host="0.0.0.0", use_reloader=False)
