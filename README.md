# Python-Reddit-Scripts

Hi there. The following Python Files were wrote to operate on the [League of Legends Subreddit](https://www.reddit.com/r/leagueoflegends/).

>Donezobot.py

While funny Donezobot operated as our notification bot that would send a message to our slack channel alerting us when we received new modmail messages and response. The bot requires knowledge of PRAW, a wrapper for the Reddit API.

>ForceFlairCounter.py

One of our now deprecated tools we used to count how many users used a certain flair for their account on /r/leagueoflegends and outputted it into a CSV file for distribution.

>Modmail_Archive.py

Due to Reddit's lack of tools for archiving Modmail we are forced to create an archive ourselves. What this does is write out a text file that is formatted with the author, subject and message link so that we can add find past messages and access them despite the websites limitations on the last 15,000 messages.

>Short_Content_Auto_Removal.py

While constantly looking through new submissions it checks to see whether or not the YouTube video is below <30s in length. If it is then it must be removed according to the subreddits policy [here](https://www.reddit.com/r/leagueoflegends/wiki/subredditrules#wiki_short_duration_content_belongs_in_a_self_post)

>eSports_Image_Grab.py

Riot Games has an eSports API that contain links to team images. We use these team images to build CSS Sprites and these grab each official regions team images and downloads them into a folder for later resizing.


