from webbrowser import BackgroundBrowser
from moviepy.editor import *
from mutagen.mp3 import MP3
from random import randint
from PIL import Image

W, H = 1080, 1920

def create_redditclip_video(num_of_comments,files):
    titlefile = "redditscreenshots/title.png"
    title_clip = (
        ImageClip(titlefile, duration = MP3(f"audiofiles/output.mp3").info.length)
        .resize(width = W-300)
        )
    img = Image.open(titlefile)
    title_height = img.height
    title_width = img.width
    frames = [title_clip]
    for i in range(num_of_comments):
        length = MP3(f"audiofiles/comment" + str(i) + ".mp3").info.length
        frames.append(ImageClip(files[i], duration = length).resize(width = title_width, height = title_height))
        
    clip = concatenate_videoclips(frames, method="compose")
    clip.write_videofile("videos/reddit.mp4", fps = 24)
    return clip 


def create_background(reddit_clip):
        background_vid = VideoFileClip("background/bbswitzer-parkour.mp4")
        background_length = int(background_vid.duration)
        value = randint(0, background_length)
        background_clip = background_vid.subclip(value, value+int(reddit_clip.duration)+1)
        background_clip.write_videofile("background/background.mp4", fps = 30)
        
      
def create_final_vid():
    final_clip = (
        CompositeVideoClip([VideoFileClip("background/background.mp4"), VideoFileClip("videos/reddit.mp4").set_position("center")])
        .resize(height=H)
        .crop(x1=1100.6, y1=0, x2=2400.6, y2=1920)
    )
    audio = AudioFileClip("audiofiles/redditAudio.mp3")
    final_clip.audio = audio
    final_clip.write_videofile("final_video.mp4")

