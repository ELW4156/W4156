# coding: utf-8

from __future__ import absolute_import
from .base_model_ import Model
from datetime import date, datetime
from typing import List, Dict
from ..util import deserialize_model


class User(Model):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, username: str=None):
        """
        User - a model defined in Swagger

        :param username: The username of this User.
        :type username: str
        """
        self.swagger_types = {
            'username': str
        }

        self.attribute_map = {
            'username': 'username'
        }

        self._username = username

    @classmethod
    def from_dict(cls, dikt) -> 'User':
        """
        Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The User of this User.
        :rtype: User
        """
        return deserialize_model(dikt, cls)

    @property
    def username(self) -> str:
        """
        Gets the username of this User.
        The first name of the user

        :return: The username of this User.
        :rtype: str
        """
        return self._username

    @username.setter
    def username(self, username: str):
        """
        Sets the username of this User.
        The first name of the user

        :param username: The username of this User.
        :type username: str
        """

        self._username = username

