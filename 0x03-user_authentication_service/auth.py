#!/usr/bin/env python3
"""_summary_
"""


import bcrypt
from db import DB
from user import User
from sqlalchemy.orm.exc import NoResultFound
from uuid import uuid4


def _hash_password(password: str) -> str:
    """_summary_

    Args:
        password (str): _description_

    Returns:
        bytes: _description_
    """
    return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())


def _generate_uuid() -> str:
    """_summary_

    Raises:
        ValueError: _description_

    Returns:
        str: _description_
    """
    id = uuid4()
    return str(id)


class Auth:
    """Auth class to interact with the authentication database.
    """

    def __init__(self):
        """_summary_
        """
        self._db = DB()

    def register_user(self, email: str, password: str) -> User:
        """_summary_
        """
        try:
            # find the user with the given email
            self._db.find_user_by(email=email)
        except NoResultFound:
            # add user to database
            return self._db.add_user(email, _hash_password(password))

        else:
            # if user already exists, throw error
            raise ValueError('User {} already exists'.format(email))

    def valid_login(self, email: str, password: str) -> bool:
        """_summary_

        Args:
            email (str): _description_
            password (str): _description_

        Returns:
            Boolean: _description_
        """
        try:
            # find the user with the given email
            user = self._db.find_user_by(email=email)
        except NoResultFound:
            return False
        # check validity of password
        return bcrypt.checkpw(password.encode('utf-8'), user.hashed_password)

    def create_session(self, email: str) -> str:
        """_summary_

        Args:
            email (str): _description_

        Returns:
            str: _description_
        """
        try:
            user = self._db.find_user_by(email=email)
        except NoResultFound:
            return None
        else:
            user.session_id = _generate_uuid()
            return user.session_id
