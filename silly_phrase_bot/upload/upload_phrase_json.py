import firebase_admin
from firebase_admin import credentials, App
from firebase_admin import storage

print('Upload Phrase Json ')
cred = credentials.Certificate("firebase_admin.json")

app = firebase_admin.initialize_app(cred, {
    "storageBucket": 'sillyphrasebot.appspot.com',
})

# upload image to CDN
bucket = storage.bucket()

b =bucket.blob('phrase.json')
b.cache_control = "public, max-age=86400"
b.upload_from_filename('phrase.json',content_type='application/json'
                       ,)

print('End Upload Phrase Json')