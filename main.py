from TTS import create_tts_files, combine_tts_files
from reddit import connect_to_reddit, get_screenshots, get_screenshots, select_a_subreddit
from video import create_redditclip_video, create_background , create_final_vid

def main():
    reddit = connect_to_reddit()
    picked_post = select_a_subreddit(reddit)
    num_of_comments, audio_files = create_tts_files(picked_post)
    combine_tts_files(num_of_comments, audio_files)
    files = get_screenshots(picked_post, num_of_comments)
    reddit_clip = create_redditclip_video(num_of_comments, files)
    create_background(reddit_clip)
    create_final_vid()

if __name__ == "__main__":
    main()
