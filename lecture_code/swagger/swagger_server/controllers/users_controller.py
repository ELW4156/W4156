import connexion
from swagger_server.models.user import User
from datetime import date, datetime
from typing import List, Dict
from six import iteritems
from ..util import deserialize_date, deserialize_datetime


def createuser_username_get(username):
    """
    Create User
    Create a user where blah blah blah blah 
    :param username: username to create
    :type username: str

    :rtype: None
    """
    return 'do some magic!'


def listusers_get():
    """
    List users
    Get all the users 

    :rtype: List[User]
    """
    u1 = User("foo")
    u2 = User("bar")
    return [u1,u2]
    #return u
    #return 'do some magic!'
