import sys
import secrets
import requests

#username = sys.argv[1]
#password = sys.argv[2]

auth_url = "https://api.instagram.com/oauth/authorize/?client_id="+ secrets.client_id + "&redirect_uri=http://www.example.com&response_type=token"

