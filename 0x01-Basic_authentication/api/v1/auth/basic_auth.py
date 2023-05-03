#!/usr/bin/env python3
"""
Module for authentication using Basic auth
"""


from api.v1.auth.auth import Auth


class BasicAuth(Auth):
    """_summary_
    """

    def extract_base64_authorization_header(self,
                                            authorization_header: str) -> str:
        """_summary_

        Args:
                        authorization_header (str): _description_

        Returns:
                        str: _description_
        """
        if authorization_header is None:
            return None
        if not isinstance(authorization_header, str):
            return None
        if not authorization_header.startswith('Basic '):
            return None

        token = authorization_header.split(' ')[-1]
        return token
