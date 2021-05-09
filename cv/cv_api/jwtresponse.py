from rest_framework_jwt.compat import get_username
import datetime,types
import os

def jwt_response_payload_handler(token, user=None, request=None):

    response_packet = {}
    usr = str(user.get_username())
    usrfn = str(user.get_full_name())
    response_packet['datetime'] = str(datetime.datetime.now())
    response_packet['username'] = usr
    response_packet['token'] = token
    response_packet['success'] = True

    return response_packet


