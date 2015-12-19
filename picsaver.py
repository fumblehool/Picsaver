import sys
import secrets
import requests
import os
import datetime

auth_url = ("https://api.instagram.com/oauth/authorize/?client_id=%s"
            "&redirect_uri=http://www.example.com"
            "&response_type=token" % secrets.client_id)
path = os.getcwd()

if os.path.exists('images') is False:
    os.makedirs('images')
path = path + '/images/'


def download_all_imgs(name):
    user_id = get_user_id(name)
    user_info = ("https://api.instagram.com/v1/users/%s"
                 "/?access_token=" % user_id)
    info = requests.get(user_info + secrets.access_token)
    u_info = info.json()
    total_media = u_info['data']['counts']['media']

    if total_media % 20 != 0:
        steps = total_media / 20 + 1
    else:
        steps = total_media/20

    url = ("https://api.instagram.com/v1/users/%s"
           "/media/recent/?access_token=" % user_id)
    z = 1
    print "Total Number of Images are " + str(total_media) + "."
    print "Saving images in directory : " + path[0:len(path)-1]
    for j in range(steps):
        r = requests.get(url+secrets.access_token)
        data = r.json()

        for i in range(len(data['data'])):
            link = data['data'][i]['images']['standard_resolution']['url']
            r = requests.get(link, stream=True)
            img_name = datetime.datetime.fromtimestamp(
                        int(data['data'][i]['created_time'])
                        ).strftime('%Y-%m-%d %H:%M:%S') + ".jpg"

            print "Saving image " + img_name
            print "Image number " + str(z) + "."
            with open(path + img_name, 'wb') as f:
                for chunks in r:
                    f.write(chunks)
            z += 1
        if len(data['pagination']) is 0:
            break
        url = data['pagination']['next_url']


def get_user_id(name):
    u = ("https://api.instagram.com/v1/users/search?q=%s"
         "&access_token=" % name)
    r_ = requests.get(u + secrets.access_token)
    d = r_.json()
    user_id = d['data'][0]['id']
    return user_id


# download_all_imgs()

download_all_imgs(raw_input("Enter Your Username: "))
