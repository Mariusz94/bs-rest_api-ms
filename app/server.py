import jwt
import config
import logging
from datetime import datetime, timedelta
from flask import Flask, jsonify, request
from service.logs_service.app_logs import config_logs, init_logging
import service.api_service as api_service
from functools import wraps

app = Flask(__name__)
app.config["SECRET_KEY"] = config.JWT_SECRET_KEY
app.config["ACCESS_TOKEN_EXPIRATION"] = timedelta(minutes=30)
app.config["REFRESH_TOKEN_EXPIRATION"] = timedelta(days=7)


# decorator for verifying the JWT
def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = None
        # jwt is passed in the request header
        if "x-access-token" in request.headers:
            token = request.headers["x-access-token"]
        # return 401 if token is not passed
        if not token:
            return jsonify({"message": "Token is missing !!"}), 401

        try:
            # decoding the payload to fetch the stored details
            data = jwt.decode(token, app.config["SECRET_KEY"], algorithms=["HS256"])
            # current_user = User.query.filter_by(public_id=data["public_id"]).first()
            logging.debug(data["login"])
            logging.debug(data)
            current_user = {"a": 1}
        except:
            return jsonify({"message": "Token is invalid !!"}), 401
        # returns the current logged in users context to the routes
        return f(current_user, *args, **kwargs)

    return decorated


@app.route("/", methods=["GET"])
def welcome():
    """
    Method used to check the service.

    Returns:
        json: Service information.
    """
    return jsonify({"info": "server works"}), 200


@app.route("/protected", methods=["GET"])
@token_required
def foo_protected_method(current_user):
    return jsonify({"info": "You are in"}), 200


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
            access_token_expiration = (
                datetime.utcnow() + app.config["ACCESS_TOKEN_EXPIRATION"]
            )
            refresh_token_expiration = (
                datetime.utcnow() + app.config["REFRESH_TOKEN_EXPIRATION"]
            )

            access_token = jwt.encode(
                {
                    "login": login,
                    "exp": access_token_expiration,
                    "token_type": "access_token",
                },
                config.JWT_SECRET_KEY,
                algorithm="HS256",
            )
            refresh_token = jwt.encode(
                {
                    "login": login,
                    "exp": refresh_token_expiration,
                    "token_type": "refresh_token",
                },
                config.JWT_SECRET_KEY,
                algorithm="HS256",
            )

            user_info["access_token"] = access_token
            user_info["refresh_token"] = refresh_token

            return jsonify(user_info), 200
        else:
            return jsonify({"message": "Invalid credentials"}), 401
    except Exception as e:
        logging.exception(str(e))
        return jsonify({"message": "Login failed", "error": str(e)}), 500


if __name__ == "__main__":
    init_logging()
    config_logs()
    app.run(debug=False, port=config.SERVICE_PORT, host="0.0.0.0", use_reloader=False)
