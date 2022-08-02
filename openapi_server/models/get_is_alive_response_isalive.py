# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from openapi_server.models.base_model_ import Model
from openapi_server import util


class GetIsAliveResponseIsalive(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, uri=None, title=None, description=None):  # noqa: E501
        """GetIsAliveResponseIsalive - a model defined in OpenAPI

        :param uri: The uri of this GetIsAliveResponseIsalive.  # noqa: E501
        :type uri: str
        :param title: The title of this GetIsAliveResponseIsalive.  # noqa: E501
        :type title: str
        :param description: The description of this GetIsAliveResponseIsalive.  # noqa: E501
        :type description: str
        """
        self.openapi_types = {
            'uri': str,
            'title': str,
            'description': str
        }

        self.attribute_map = {
            'uri': 'uri',
            'title': 'title',
            'description': 'description'
        }

        self._uri = uri
        self._title = title
        self._description = description

    @classmethod
    def from_dict(cls, dikt) -> 'GetIsAliveResponseIsalive':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The GetIsAlive_response_isalive of this GetIsAliveResponseIsalive.  # noqa: E501
        :rtype: GetIsAliveResponseIsalive
        """
        return util.deserialize_model(dikt, cls)

    @property
    def uri(self):
        """Gets the uri of this GetIsAliveResponseIsalive.


        :return: The uri of this GetIsAliveResponseIsalive.
        :rtype: str
        """
        return self._uri

    @uri.setter
    def uri(self, uri):
        """Sets the uri of this GetIsAliveResponseIsalive.


        :param uri: The uri of this GetIsAliveResponseIsalive.
        :type uri: str
        """

        self._uri = uri

    @property
    def title(self):
        """Gets the title of this GetIsAliveResponseIsalive.


        :return: The title of this GetIsAliveResponseIsalive.
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        """Sets the title of this GetIsAliveResponseIsalive.


        :param title: The title of this GetIsAliveResponseIsalive.
        :type title: str
        """

        self._title = title

    @property
    def description(self):
        """Gets the description of this GetIsAliveResponseIsalive.


        :return: The description of this GetIsAliveResponseIsalive.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this GetIsAliveResponseIsalive.


        :param description: The description of this GetIsAliveResponseIsalive.
        :type description: str
        """

        self._description = description