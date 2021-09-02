import os
import json

import googleapiclient.discovery
#remember to use your developer key every 90 days or it just expires
#the quota system refreshes after like 10 days
def main():
    comment=[]
    os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"

    api_service_name = "youtube"
    api_version = "v3"
    DEVELOPER_KEY = "AIzaSyCTw6EKjTjzEwZEu3Y9szp39RvpW5HyBCk"

    youtube = googleapiclient.discovery.build(
        api_service_name, api_version, developerKey = DEVELOPER_KEY)

    request = youtube.commentThreads().list(
        part="snippet",
        textFormat="plainText",
        videoId="AaZ_RSt0KP8",
        order="relevance",
        maxResults=10

    )
    response = request.execute()
    # data=json.loads(response)

    # print(response)
    b=response['items']                                                                    
    for i in b:                                                                     
       c=i["snippet"]                                                              
       topLevelComment=c["topLevelComment"]                                        
       snippetLast=topLevelComment["snippet"]                                      
       comment.append(snippetLast["textDisplay"])                                          
    print(comment)
if __name__ == "__main__":
    main()
