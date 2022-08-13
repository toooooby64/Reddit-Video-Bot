import profile
from numpy import concatenate
import praw
import boto3
import os
from mutagen.mp3 import MP3
from moviepy.editor import *

files = []

def create_tts_files(picked_post):
    aws_session = boto3.Session(aws_access_key_id='AKIASINWYKR26UMG2WFQ' , aws_secret_access_key='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')
    client = aws_session.client(service_name='polly')
    length = 0
    i = 0
    files = []
    text=picked_post.title
    response = client.synthesize_speech(Engine = 'neural', OutputFormat = 'mp3', Text = text, VoiceId ='Joey')
    file = open('audiofiles/output.mp3', 'wb')
    file.write(response['AudioStream'].read())
    file.close()

    length += MP3(f"audiofiles/output.mp3").info.length

    for top_level_comment in picked_post.comments:
        if length > 50:
            break
        print("-------------------------")
        print(top_level_comment.body)
        comment = top_level_comment.body
        response = client.synthesize_speech(Engine = 'neural', OutputFormat = 'mp3', Text = comment, VoiceId ='Joey')
        file = open("audiofiles/comment" + str(i) + ".mp3", 'wb')
        file.write(response['AudioStream'].read())
        file.close()
        files.append("audiofiles/comment" + str(i) + ".mp3")
        length += MP3(f"audiofiles/comment" + str(i) + ".mp3").info.length
        i += 1
    return i,files

def combine_tts_files(num_of_comments,files):
    title_audio = AudioFileClip("audiofiles/output.mp3")
    audio_clips = [title_audio]
    for i in range(num_of_comments):
        audio_clips.append(AudioFileClip(files[i]))
        
    clip = concatenate_audioclips(audio_clips)
    clip.write_audiofile("audiofiles/redditAudio.mp3")


