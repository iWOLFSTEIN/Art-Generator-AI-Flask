# download and save images from dall E 2 to downlaods folder

from env.secrets import APP_USERNAME, APP_PASSWORD
import requests
import os
import time


url = 'http://127.0.0.1:5000'
downloads_path = os.path.expanduser("~/Downloads")


def getFileNmae():
    microseconds_since_epoch = int(time.time() * 1000000)
    microseconds_string = str(microseconds_since_epoch)
    filename = microseconds_string + ".png"
    return filename


def getJwtTokenFromServer():  
    payload = {'username': APP_USERNAME, 'password': APP_PASSWORD}
    response = requests.post(url+'/login', data=payload)
    if (response.status_code == 200):
        return response.json()['token']
    

def generateImages(token: str) -> list:
    prompt = input('Enter your prompt: ')
    payload = {'username': APP_USERNAME, 'password': APP_PASSWORD}
    headers = {'Authorization': 'Bearer '+token}
    response = requests.get(url+'/prompt/'+prompt, headers=headers)
    if (response.status_code == 200):
        return response.json()['data']
    

def downloadImages(images: list):   
    for index, image in enumerate(images):
        file_path = os.path.join(downloads_path, getFileNmae())
        response = requests.get(image['url'])
        with open(file_path, "wb") as file:
            file.write(response.content)
            print(f'File {index+1} is downloaded')




if __name__ == '__main__':
    while True:
        jwtToken = getJwtTokenFromServer()
        images_urls = generateImages(token=jwtToken)
        downloadImages(images=images_urls)




