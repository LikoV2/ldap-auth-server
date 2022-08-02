# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from openapi_server.models.base_model_ import Model
from openapi_server import util


class VerifyToken(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, auth_token=None):  # noqa: E501
        """VerifyToken - a model defined in OpenAPI

        :param auth_token: The auth_token of this VerifyToken.  # noqa: E501
        :type auth_token: str
        """
        self.openapi_types = {
            'auth_token': str
        }

        self.attribute_map = {
            'auth_token': 'auth_token'
        }

        self._auth_token = auth_token

    @classmethod
    def from_dict(cls, dikt) -> 'VerifyToken':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The VerifyToken of this VerifyToken.  # noqa: E501
        :rtype: VerifyToken
        """
        return util.deserialize_model(dikt, cls)

    @property
    def auth_token(self):
        """Gets the auth_token of this VerifyToken.


        :return: The auth_token of this VerifyToken.
        :rtype: str
        """
        return self._auth_token

    @auth_token.setter
    def auth_token(self, auth_token):
        """Sets the auth_token of this VerifyToken.


        :param auth_token: The auth_token of this VerifyToken.
        :type auth_token: str
        """

        self._auth_token = auth_token