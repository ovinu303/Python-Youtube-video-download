from pytube import YouTube
import os

#to remove invalid characters from youtube title
def clean_filename(filename: str) -> str:
    invalid_chars = '<>:"/\\|?*'
    return ''.join(c for c in filename if c not in invalid_chars)


link = input("Enter a YouTube video URL: ")
yt = YouTube(link)
ys = yt.streams.get_highest_resolution()

output_file =  f'{yt.title}.mp4'
cleaned_filename = clean_filename(output_file)

output_path = os.path.join(os.path.expanduser("~"), "Downloads") #to path to user's Downloads folder
ys.download(output_path= output_path, filename=cleaned_filename)
print('Video downloaded successfully to your Downloads folder.')

