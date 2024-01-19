import requests
import base64

from PIL import Image


def get_token(clientId, clientSecret):
    url = "https://accounts.spotify.com/api/token"
    headers = {}
    data = {}
    message = f"{clientId}:{clientSecret}"
    messageBytes = message.encode('ascii')
    base64Bytes = base64.b64encode(messageBytes)
    base64Message = base64Bytes.decode('ascii')
    headers['Authorization'] = "Basic " + base64Message
    data['grant_type'] = "client_credentials"
    r = requests.post(url, headers=headers, data=data)
    token = r.json()['access_token']
    return token


def get_track_recommendations(seed_tracks, token):
    limit = 10
    recUrl = f"https://api.spotify.com/v1/recommendations?limit={limit}&seed_tracks={seed_tracks}"

    headers = {
        "Authorization": "Bearer " + token
    }

    res = requests.get(url=recUrl, headers=headers)
    return res.json()



def save_album_image(img_url, track_id):
    r = requests.get(img_url)
    open('img/' + track_id + '.jpg', "wb").write(r.content)


def get_album_mage(track_id):
    return Image.open('img/' + track_id + '.jpg')