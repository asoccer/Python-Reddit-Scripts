import praw,pafy,sys,time

def reddit_login():
    submission = praw.helpers.submission_stream(r,'leagueoflegends',limit=10,verbosity = 1)
    video_length = []
    for a in submission:
        if 'youtube' in a.url or 'youtu.be' in a.url:
            try:
                video = pafy.new(a.url)
                duration = str(video.duration).replace(":","")
                #Is it even 30s?
                if '0000' == duration[0:4]:
                    if int(duration[4]) <3:
                        wiki = r.get_wiki_page('leagueoflegends','shortduration')
                        wiki.edit(wiki.content_md + '\n\n ' + a.id)
                        a.remove()
                        a.add_comment("Hello, your post has been removed because it is in violation of our short content rule. All Content <30s must be submitted as a self post. This action was done automatically. If you beleive this removal was incorrent immediately [Message the mods](http://www.reddit.com/message/compose?to=%2Fr%2Fleagueoflegends)").distinguish()
            except Exception as e:
                a.report("Picflutes Bot Could not understand the duration of this video")
                print(e)
        else:
            pass
                    
                                    
if __name__ == '__main__':
    r = praw.Reddit("Approve/Remove Short Duration Content")
    r.login()
    reddit_login()
    
