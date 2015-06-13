import praw,pafy

r = praw.Reddit("Approve/Remove Short Duration Content")
r.login('picflute','RX4RQheqVu5x')

submission = praw.helpers.submission_stream(r,'Riven',limit=10,verbosity = 1)
video_length = []
for a in submission:
    print(a.url)
    if 'youtube' in a.url:
        video = pafy.new(a.url)
        for i in range(0,8,3):
            video_length.append(video.duration[0+i:2+i])
        if(video_length[0] == "00" and video_length[1] == "00"):
                length = int(video_length[2])
                if length<30:
                    a.remove()
        video_length = []
    else:
        print('not YT')
        
