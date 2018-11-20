# 画像をflickrからダウンロード
from flickrapi import FlickrAPI
from urllib.request import urlretrieve
from pprint import pprint
import os, time, sys
import json

# API情報
f = open("config.json","r")
json_data = json.load(f)
key = json_data["key"]
secret = json_data["secret"]
wait_time = 1

#保存フォルダの指定
animalname = sys.argv[1]
savedir = "./animal_picture/" + animalname

flickr = FlickrAPI(key, secret, format="parsed-json")
result = flickr.photos.search(
    text = animalname,
    per_page = 400,
    media = 'photos',
    sort = 'relevance',
    safe_search = 1,
    extras = 'url_q, licence'
)

photos = result['photos']
pprint(photos)