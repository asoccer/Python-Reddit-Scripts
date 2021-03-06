import requests,json

regions = ['226','225','230','229','231']
for region in regions:
    r = requests.get('http://na.lolesports.com:80/api/standings.json?tournamentId='+ region) #Gets each regions team roster
    j = r.json() 
    TeamID = {}#Each Team ID request will return LogoURL which is what will be downloaded
    for team in j:
        TeamID[team['teamId']] = team['teamTitle'] #Dictionary Sorted by ID:TeamTitle
    base = 'http://na.lolesports.com:80/api/team/' 

    LogoURL = {}
    for ID in list(TeamID.keys()):#ID
        page = requests.get(base + str(ID) + '.json')
        page = page.json()
        LogoURL[TeamID[ID]] = page['logoUrl']#Each Team now has a URL for download

    for name in list(LogoURL.keys()):#Downloads Each Team Icon and names it with teh accoriding team
            url = LogoURL[name]
            page = requests.get(url)
            with open(name+".png",'wb') as tile:
                tile.write(page.content)


