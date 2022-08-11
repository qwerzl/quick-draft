import requests

rawEmby = requests.get("https://gist.githubusercontent.com/futurkk/6b3843c36194070ba052018878596c2e/raw/Emby.list").text
rawSpotify = requests.get("https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Surge/Spotify/Spotify.list").text
rawTwitch = requests.get("https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Surge/Twitch/Twitch.list").text

result = rawEmby.split("\n") + rawSpotify.split("\n") + rawTwitch.split("\n")

result = list(set(result))

with open("./result.list", "w") as f:
    f.write("\n".join(result))
