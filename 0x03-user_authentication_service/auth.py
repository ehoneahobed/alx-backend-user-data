#!/usr/bin/env python3
"""_summary_
"""


import bcrypt


def _hash_password(password: str) -> str:
    """_summary_

    Args:
        password (str): _description_

    Returns:
        bytes: _description_
    """
    return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
