from instagram.client import InstagramAPI
client_id ="607cb47bff57453a89d3b4e516bb6a1f"
client_secret="38a9d61d7ed343fc9bf0e83979e3324e"

access_token = "3624239421.607cb47.d3e5fa0ff9774bce84f004dd1ee44c55"

api = InstagramAPI(access_token=access_token, client_secret=client_secret)

print('Test')
recent_media, url = api.tag_recent_media(tag_name="coding", count=5)
print(recent_media)
for media in recent_media['data']:
    print('Hello World')
    print(media.caption.text)
