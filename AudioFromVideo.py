import moviepy.editor
from pathlib import Path

name_video_file: 'str' = ''  # Name of the file (with the extension)
dir_video_file: 'str' = ''  # Path to the file

video_file = Path(f'{dir_video_file}/{name_video_file}')
video = moviepy.editor.VideoFileClip(f'{video_file}')
audio = video.audio
audio.write_audiofile(f'{dir_video_file}/{video_file.stem}.mp3')
