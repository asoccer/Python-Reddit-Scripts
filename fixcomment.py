import json

f = open('CommentData_9_19_9.txt','r')

while True:
    x = f.readline()
    if x == '':
        break
    ls = x.split(',')
    k = []
    v = []
    for a in ls:
        try:
            k.append(a[1:a.index(':')])
            v.append((a[a.index(':')+2:]))
        except:
            pass
    break
    
keys = ["'downs'", "'replies'", "'edited'", "'name'", "'body_html'", "'removal_reason'", "'subreddit'", "'quarantine'", "'ups'", "'score_hidden'", "'link_author'", "'score'", "'body'", "'parent_id'", "'gilded'", "'over_18'", "'subreddit_id'", "'author_flair_css_class'", "'report_reasons'", "'likes'", "'saved'", "'link_title'", "'num_reports'", "'mod_reports'", "'created_utc'", "'banned_by'", "'controversiality'", "'created'", "'user_reports'", "'approved_by'", "'author_flair_text'", "'link_url'", "'link_id'", "'id'", "'archived'", "'distinguished'", "'author'"]
d = dict(zip(k,v))

