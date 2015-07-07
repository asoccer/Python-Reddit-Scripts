#from our lord and savior /u/p00rleno
#r/leagueoflegends flair counter script
#For python 2.6.6
 
from __future__ import division

import operator
import cookielib
import urllib2
import json
from urllib import urlencode
from getpass import getpass
import time

 
cj = cookielib.CookieJar()
opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))

badflair = [None,'']


def login(user, passwd):
    url = 'http://www.reddit.com/api/login'
    opener.addheaders = [('User-agent', 'Flair Data Aggregation Script')]
    r = opener.open(url, urlencode({'user': user, 'passwd': passwd}))
 
def get_modhash():
    url = 'http://www.reddit.com/api/me.json'
    data = json.load(opener.open(url))
    return data['data']['modhash'] if 'data' in data else False
 
def flair_stats(subreddit, modhash):
    url = 'http://www.reddit.com/r/%s/api/flairlist.json?' % (subreddit,)
    stats = {'total': 0, 'class': {} }
    q = {'limit': 1000, 'uh': modhash}
 
    _next = None
    i = 1
    while True:
        print ('%d users parsed' %  ((i-1)*1000))
        if _next:
            q['after'] = _next
        data = None
        while data == None:
            try:
                data = json.load(opener.open(url + urlencode(q)))
            except:
                print 'err'
        if not data:
            break
        for user in data['users']:
            c = user['flair_css_class']
            if c not in badflair:
                if c not in stats['class']:
                    stats['class'][c] = 0
                stats['class'][c] += 1
                stats['total'] += 1
        if 'next' not in data:
            break
        _next = data['next']
        i = i+1
    print '%d users parsed' % (stats['total'])
    return stats


def make_output(stats):
    output = {}
    for flair,count in stats['class'].items():
        name = flair
        output[name] = count
    sorted_output = sorted(output.keys())
    
    filename = 'flairstats%s.csv'%(time.strftime("-%H-%d-%m-%Y"))
    f = open(filename, 'w')
    for name in sorted_output:
        f.write('%s,%d\n' % (name,output[name]))
    f.write('\n\n')
    f.write('%s,%d' % ('Total',stats['total']))
    f.close()

if __name__ == '__main__':
    import sys
    username = raw_input('username: ')
    passwd = getpass('password (will not be echoed!): ')
    login(username, passwd)
    modhash = get_modhash()
    if not modhash:
        print 'Login Failed!'
        sys.exit(1)
 
    subreddit = raw_input('subreddit: ')
    print 'Loading stats...'
    stats = flair_stats(subreddit, modhash)
    print 'Writing output'
    make_output(stats)
    print 'Done! Exiting'
