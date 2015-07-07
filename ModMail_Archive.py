import praw
import OAuth2Util

#r = praw.Reddit("My Dank Meme's Bot")
#o = OAuth2Util.OAuth2Util(r)

import praw
import time
#Converts UTC To something readable
def t(user):
    created = user.created_utc
    date = time.ctime(created)
    return date

#Set HTTPS off in your account settings if you've never done PRAW before. This doesn't work if you have it on.
#And you can re-enable it after running this.

r = praw.Reddit("ModMail Archive action")
f = open("ModMailDemo.txt","w") #Create and Write to
f.write("Author | Subject | Permalink |Date\n---|---|----|----\n") #You're going to be posting the dump in the Wiki and don't need to doublespace
USER = input('Type User Name\n')
PASSWORD = input('Type Your Password | NOTE THIS DOESNT SEND OR SAVE THE PASSWORD ANYWHERE\n')
SUBREDDIT = input('Input the Subreddit You Wish to archive | YOU MUST HAVE MAIL PRIVS TO DO THIS')
r.login(USER,PASSWORD) #Use your damn creds "dankflute","123456"

redd = "https://www.reddit.com/message/messages/"
print("Searching in the database....")
modmail = r.get_mod_mail(SUBREDDIT,params = None,limit = None)
count =0
for a in modmail:
    if(str(a.author)!="AutoModerator"):
        try:
            count+=1
            f.write(str(a.author) + " | "+ str(a.subject) + " | " + redd+ str(a.id)+ " | " + t(a)+"\n")
        except Exception as e:
             
            pass #Weird Unicode Errors I got that I didn't want to waste time on handling. Someone else wants to fix them do it.

f.close()
print("Completed, please check your Textfile\nYou had a total of " + str(count) + "messages found god bless\n Message /u/picflute if you have any errors or improvements and I'll be happy to listen")
