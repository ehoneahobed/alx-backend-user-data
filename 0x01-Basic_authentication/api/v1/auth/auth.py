#!/usr/bin/env python3
"""
Module for authentication
"""


from typing import List, TypeVar
from flask import request


class Auth:
    """_summary_
    """

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """_summary_

        Args:
                path (str): _description_
                excluded_paths (List[str]): _description_

        Returns:
                bool: _description_
        """
        return False

    def authorization_header(self, request=None) -> str:
        """_summary_

        Args:
                request (_type_, optional): _description_. Defaults to None.

        Returns:
                str: _description_
        """
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """_summary_
        """
        return None
