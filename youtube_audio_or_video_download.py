from pytube import YouTube

# https://www.youtube.com/watch?v=ijj_hheGEi0 - A link if you want to try

link = input("Enter the link:\n>> ")
yt = YouTube(link)

print(f"Title: {yt.title}")
print(f"Number of views: {yt.views}\n")

user_input = input("This is the video you want do download? (y/n) ").lower()
if user_input == "y":
    audio_or_video = input("\nYou want the video(v) or audio(a)? (v/a) ").lower()
    if audio_or_video == "a":
        try:
            print("\nDownloading audio...")
            ys = yt.streams.get_audio_only()
            ys.download("audio") # Path for audio files
            print(f"{yt.title} has been downloaded successfully.")
        except:
            print("Something went wrong! Try again or use another link.")
    if audio_or_video == "v":
        try:
            print("\nDownloading video...")
            ys = yt.streams.get_highest_resolution()
            ys.download("video") # Path for video files
            print(f"{yt.title} has been downloaded successfully.")
        except:
            print("Something went wrong! Try again or use another link.")

if user_input == "n":
    print("\nYou made the decision not do download.")