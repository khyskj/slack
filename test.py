import requests
 
def post_message(token, channel, text):
    response = requests.post("https://slack.com/api/chat.postMessage",
        headers={"Authorization": "Bearer "+token},
        data={"channel": channel,"text": text}
    )
    print(response)
 
myToken = "xoxb-6774306060754-6759756072599-Inmx181urLeTdb9AQGW5HDoU"
 
post_message(myToken,"#msg-test","Hello")
