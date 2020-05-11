from pytube import YouTube
import argparse
import cv2
import ffmpeg
import os

def yt_downloader_encoder(yt):
    k=""
    yt_link=yt
    title=yt_link.title
    print("Title:\n",title)
    print("Choose Action:\n")
    c=input("              Download audio only(a) \n              Download video only(v) \n              Download video along with audio(default argument) \n Just Press Enter to download video with audio ")
    if c=='a':
        k="audio"
        pref_stream=yt.streams.filter(only_audio=True).first()
        filename=title+'.mp4a'
    else:
        filename=title+'.mp4'
        print("Adaptive Streams:")
        print(yt_link.streams.filter(adaptive=True,mime_type="video/mp4"))
        print(yt_link.streams.filter(adaptive=True,mime_type="audio/mp4"))
        itag=input("Your preferred stream itag(video): ")
        pref_stream=yt_link.streams.get_by_itag(itag)
        if c=="v":
            k="video"
        else:
            k="video & audio"
    print("Your selected stream is:  ",pref_stream)
    yn=input("Proceed? y/n  ")
    if yn=='y' or 'Y':
        print("Downloading "+k+" of "+title+ "...")
        pref_stream.download('C:/Users/saas1/Downloads/YouTube Downloads')
        if c=="":
            yt.streams.filter(only_audio=True).first().download('D:/extra downloads/a')
            in_video = ffmpeg.input('C:/Users/saas1/Downloads/YouTube Downloads/'+filename)
            in_audio = ffmpeg.input('D:/extra downloads/a/'+filename)
            ffmpeg.concat(in_video, in_audio, v=1, a=1).output("C:/Users/saas1/Downloads/YouTube Downloads/_"+filename).run()
            os.remove('D:/extra downloads/a')
            os.remove('C:/Users/saas1/Downloads/YouTube Downloads/'+filename)
            os.rename('C:/Users/saas1/Downloads/YouTube Downloads/_'+filename,'C:/Users/saas1/Downloads/YouTube Downloads/'+filename)
        print("Downloaded Succesfully")
    else:
       print("Download Cancelled.")


## parse the arguments(video link and filename) from command line

ap = argparse.ArgumentParser()
ap.add_argument("-v", "--video_link", required=True,
	help="internet link to video to be proccessed")

args = vars(ap.parse_args())  #parsed
yt=YouTube(args["video_link"])
yt_downloader_encoder(yt)
