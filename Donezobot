__author__ = 'picflute'
import OAuth2Util
import praw,time
#-----------------------------------------------#
#Loads Slack Client
from pyslack import SlackClient
client = SlackClient("-SECRET API KEY-")
#-----------------------------------------------#

def reddit_login():
    r = praw.Reddit("My Dank Memer DONEZOBOT")
    o = OAuth2Util.OAuth2Util(r)
    return r

def slackresponse(message):
    author = "From: " + str(message.author)
    subject = "Subject: " + str(message.subject)
    body = "Body: \n" + str(message.body)
    link = "Link to Message: " + "https://www.reddit.com/message/messages/" + str(message.id)
    num_replies = len(message.replies)
    
    if num_replies == 0:
        response = "New Message: " + author + "\n" + subject + "\n" + body + "\n" + link
    else:
        response = "New Response " + author + " on\n" + subject +"\n" + link + "\nLast Reply from " + str(message.replies[-1].author)
    return response
        
def main():
    prev = ""
    while True:
        try:
            r = reddit_login()
            modmail = r.get_mod_mail('leagueoflegends',limit = 1)
            for message in modmail:
                if prev != message.id:
                    try:
                        response = slackresponse(message)
                        client.chat_post_message('#modmail-channel', response, username='-Insert Your Bots Name')
                        prev = message.id
                    except:
                        print("Didn't work")
                else: print("No New Updates since " + prev)
            
        except Exception as e:
            print(e)
        time.sleep(60)

