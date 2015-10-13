import sys
import secrets
import requests
import shutil

auth_url = "https://api.instagram.com/oauth/authorize/?client_id="+ secrets.client_id + "&redirect_uri=http://www.example.com&response_type=token"

def download_all_imgs(user_id):
    url = "https://api.instagram.com/v1/users/" + user_id + "/media/recent/?access_token="
    r = requests.get(url+secrets.access_token)
    data = r.json()
    items = len(data['data'])
    z=1
    y=0
    print "Total Number of Images are " + str(items) + "."
    for i in range(items):
        link = data['data'][i]['images']['standard_resolution']['url']
        r = requests.get(link, stream = True)
        img_name =data['data'][i]['caption']
        if img_name == None:
            img_name = str(y)
            y=y+1
        else:
            img_name = img_name =data['data'][i]['caption']['text']

        print "Saving image "+ img_name
        print "Image number " + str(z) + "."
        with open(img_name + ".jpg",'wb') as f:
            shutil.copyfileobj(r.raw,f)
        print "Done."
        z+=1

def download_all_imgs_user(name):
    download_all_imgs(get_user_id(name))

def get_user_id(name):
    u = "https://api.instagram.com/v1/users/search?q="+ name +"&access_token="
    r_ = requests.get(u+secrets.access_token)
    d = r_.json()
    user_id = d['data'][0]['id']
    return user_id


# function calls.
download_all_imgs_user(raw_input("Enter the Username "))
#download_all_imgs()
