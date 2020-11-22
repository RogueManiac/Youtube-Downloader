import pytube
import os
import getpass


def activate():
    convert = False

    ID = getpass.getuser()

    default = input("Default directory?")
    
    if default:
        directory = f"/Users/{ID}/Desktop/Youtube_vids"
    else:
        directory = f"/Users/{ID}/{input('Directory:')}"
    
    link = input("Enter the video's link:")
    Title = input("Download as:")
    sound = input("Only audio?")
    
    if not link:
        print("Please enter a link")
        link = input("Enter the video's link:")
        if not link:
            print("Enter a link:")
            return False

    yt = pytube.YouTube(link)
    
    video = yt.streams.first()
    
    if sound:
        video = yt.streams.get_audio_only(subtype="mp4")
        convert = input("Convert to mp3?")
        
    else:
        Resolution = input("Highest resolution?")
        if Resolution:
            video = yt.streams.get_highest_resolution()
    
    video.download(directory, Title)

    if convert:
        os.system(f"ffmpeg -i {directory}/{Title}.mp4 {directory}/{Title}.mp3")
        os.system(f"rm {directory}/{Title}.mp4")

    return True


if activate():
    print("Done!")
    
else:
    print("try again")
