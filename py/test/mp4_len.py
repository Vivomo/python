from py.utils.IO_util import get_all_file
from moviepy.editor import VideoFileClip

filePath = input('mp4 Path:')
files = get_all_file(filePath)
duration = 0
for f in files:
    if f.endswith('.mp4'):
        clip = VideoFileClip(f)
        duration += clip.duration
        print(f, clip.duration)  # seconds
        clip.close()

print(duration / 60)
