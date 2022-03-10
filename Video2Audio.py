# This going to import MOVIEPY library
from moviepy.editor import VideoFileClip

# Call variable for file path
video = VideoFileClip(r"Video_File")
# Get audio from video
video.audio
# Save audio file in intended location.
audio.write_audiofile(r"Audio_File")
