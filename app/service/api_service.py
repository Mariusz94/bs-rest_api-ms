from service.connectors.db_connector_service import get_balance as service_get_balance
from service.connectors.authentication_service import login as service_login


def check_balance(user_id: str) -> dict:
    """
    Method allow obtain balance for user by user id.

    Args:
        user_id (str): User id.

    Returns:
        dict: Balance info.
    """
    balance_info = service_get_balance(user_id=user_id)
    return balance_info


def login(login: str, password: str) -> dict:
    """
    Check is user exist.

    Args:
        login (str): User login.
        password (str): User password.

    Returns:
        dict: Info about user.
    """
    user_info = service_login(login, password)
    return user_info


def make_withdrawal() -> dict:
    a = {}
    return a


def make_deposit() -> dict:
    a = {}
    return a


def make_transfer() -> dict:
    a = {}
    return a


def get_account_statement() -> dict:
    a = {}
    return a
