import requests
from operator import itemgetter

rawEmby = requests.get("https://gist.githubusercontent.com/futurkk/6b3843c36194070ba052018878596c2e/raw/Emby.list").text
rawSpotify = requests.get("https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Surge/Spotify/Spotify.list").text
rawTwitch = requests.get("https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Surge/Twitch/Twitch.list").text

tmpresult = rawEmby.split("\n") + rawSpotify.split("\n") + rawTwitch.split("\n")

tmpresult = list(set(tmpresult))

result = []
print(tmpresult)

for i in tmpresult:
    if i.startswith("#") or i == '':
        continue
    elif i.startswith("DOMAIN-SUFFIX,"):
        result.append(i.split(",") + [1])
    elif i.startswith("DOMAIN-KEYWORD,"):
        result.append(i.split(",") + [2])
    elif i.startswith("PROCESS-NAME,"):
        result.append(i.split(",") + [3])
    elif i.startswith("IP-CIDR,"):
        result.append(i.split(",") + [4])
    elif i.startswith("IP-CIDR6,"):
        result.append(i.split(",") + [5])
    else:
        result.append(i.split(",") + [6])

result = sorted(result, key=itemgetter(-1))

for i in range(len(result)):
    result[i] = ','.join(result[i][:-1])


with open("./result.list", "w") as f:
    f.write("\n".join(result))
