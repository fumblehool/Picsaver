import sys
import secrets
import requests
import shutil
import os
import datetime

auth_url = "https://api.instagram.com/oauth/authorize/?client_id="+ secrets.client_id + "&redirect_uri=http://www.example.com&response_type=token"
path = os.getcwd()

if os.path.exists('images') == False:
    os.makedirs('images')
path = path + '/images/'


def download_all_imgs(user_id):
    url = "https://api.instagram.com/v1/users/" +user_id+ "/media/recent/?access_token="
    r = requests.get(url+secrets.access_token)
    data = r.json()
    items = len(data['data'])
    z=1
    y=0
    print "Saving images in directory : " + path[0:len(path)-1]
    print "Total Number of Images are " + str(items) + "."
    for i in range(items):
        link = data['data'][i]['images']['standard_resolution']['url']
        r = requests.get(link, stream = True)
        img_name = datetime.datetime.fromtimestamp(int(data['data'][i]['created_time'])).strftime('%Y-%m-%d %H:%M:%S') + '.jpg'

        print "Saving image "+ img_name
        print "Image number " + str(z) + "."
        with open(path + img_name + '.jpg','wb') as f:
            shutil.copyfileobj(r.raw,f)
        z=z+1


def download_all_imgs_user(name):
    download_all_imgs(get_user_id(name))


def get_user_id(name):
    u = "https://api.instagram.com/v1/users/search?q="+ name +"&access_token="
    r_ = requests.get(u+secrets.access_token)
    d = r_.json()
    user_id = d['data'][0]['id']
    return user_id


#download_all_imgs()
download_all_imgs_user(raw_input("Enter Your Username: "))
