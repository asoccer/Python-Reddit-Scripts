import praw,time

r = praw.Reddit("Archive ModMail Bot")
message = 'https://www.reddit.com/message/messages/'
after_field =""
modmail = r.get_mod_mail('leagueoflegends',limit = 10000)
modid = []
content = {'subject':[],'author': [],'dest':[],'id':[],'time':[]}
for a in modmail:
    content['author'].append(str(a.author))
    content['subject'].append(str(a.subject))
    t = time.ctime(int(a.created_utc))
    content['time'].append(str(t))
    content['id'].append(str(message + a.id))
    content['dest'].append(str(a.dest))
                           


f = open('write.txt','w')
for a in range(len(content['author'])):
    try:
        f.write(str(content['author'][a]) + "|" +str(content['dest'][a]) + "|" + content['subject'][a] + '|' + content['id'][a] + "|" + str(content['time'][a]) + "\n")
    except:
        print(str(content['author'][a]) + "|" +str(content['dest'][a]) + "|" + content['subject'][a] + '|' + content['id'][a] + "|" + str(content['time'][a]))
        print("this didn't load")
