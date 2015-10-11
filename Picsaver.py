import sys
import secrets
import requests
import shutil

auth_url = "https://api.instagram.com/oauth/authorize/?client_id="+ secrets.client_id + "&redirect_uri=http://www.example.com&response_type=token"

def download_all_imgs():
    url = "https://api.instagram.com/v1/users/self/media/recent/?access_token="
    r = requests.get(url+secrets.access_token)
    data = r.json()
    items = len(data['data'])
    z = 0
    for i in range(items):
        link = data['data'][i]['images']['standard_resolution']['url']
        r = requests.get(link, stream = True)
        with open(str(z)+'.jpg','wb') as f:
            shutil.copyfileobj(r.raw,f)
        z=z+1


#download_all_imgs()
