require "instagram"

access_token = "3624239421.607cb47.d3e5fa0ff9774bce84f004dd1ee44c55"


client = Instagram.client(:access_token => access_token)
tags = client.tag_search('hackbay')

while true do
  for media_item in client.tag_recent_media(tags[0].name)
    puts media_item.images.standard_resolution.url
  end
  sleep 60
end

#

#sub = client.create_subscription("user", "http://example.com/instagram/callback", aspect = "media", object_id="coding")
