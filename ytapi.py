import json
# https://googleapis.github.io/google-api-python-client/docs/dyn/youtube_v3.html

apikey = ''

from googleapiclient.discovery import build

youtube = build('youtube', 'v3', developerKey=apikey)

plid = "PLB9-ow4nx95_bSFbk7IY2VptrZjLWwQWq"  
nextPageToken = None

ytpls = youtube.playlistItems()



request = ytpls.list(part='snippet', maxResults=50, pageToken=nextPageToken, playlistId=plid)

response = request.execute()

#requestt = ytpls.list_next(previous_request=request, previous_response=response)

#responsee = requestt.execute()

ay = '' 

for item in response['items']:
    title = item["snippet"]["title"]
    try:
        channel = item["snippet"]["videoOwnerChannelTitle"]
    except Exception:
        channel = "NONE"
    ay = ay + "\n" + title + " -- " + channel

#for item in responsee['items']:
#    title = item["snippet"]["title"]
#    try:
#        channel = item["snippet"]["videoOwnerChannelTitle"]
#    except Exception:
#        channel = "NONE"
#    ay = ay + "\n" + title + " -- " + channel
#print(response)
#print(ay)

#for key in response.keys():
#  print(key)

#jsonresp = response["kind"].json()
#resp = json.dumps(jsonresp, indent=2)

response = json.dumps(response, indent=2)

print(response)
f = open("demoytapi.json", "a")
f.write(response)
#f.write(requestt)
f.close()
