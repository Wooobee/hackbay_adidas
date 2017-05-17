from instagram.client import InstagramAPI
client_id ="607cb47bff57453a89d3b4e516bb6a1f"
client_secret="38a9d61d7ed343fc9bf0e83979e3324e"

api = InstagramAPI(client_id=client_id, client_secret=client_secret)
popular_media = api.media_popular(count=20)
for media in popular_media:
    print(media.images['standard_resolution'].url)
