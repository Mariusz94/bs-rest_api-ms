from service.connectors.db_connector_service import get_balance


def check_balance(user_id: str) -> dict:
    """
    Method allow obtain balance for user by user id.

    Args:
        user_id (str): User id.

    Returns:
        dict: Balance info.
    """
    balance_info = get_balance(user_id=user_id)
    return balance_info


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
