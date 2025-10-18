# Audio (.m4a) Splitter

A simple Python script to split audio files (especially .m4a) into smaller parts. Perfect for breaking down long recordings into manageable chunks.

## Prerequisites
- Python 3.11.2 (or similar version)
- ffmpeg and ffprobe executables (included in repository as .zip files)

## Setup
1. Extract `ffmpeg.zip` and `ffprobe.zip` into the project directory
2. Install required Python packages:
```
   pip install -r requirements.txt
```

## How to Use
1. Open `audio_splitter_final.py` in a text editor
2. Update the `directory` and `filename` variables in the script:
```python
   directory = "your/audio/file/directory/"
   filename = "your_audio_file.m4a"
```
3. (Optional) Change `part_length_minutes` in the `split_audio()` call to adjust chunk size (default is 15 minutes)
4. Run the script:
```
   python audio_splitter_final.py
```
5. Split files will be saved in the same directory as the original file

## Features
- Splits audio files into equal-length parts (default: 15 minutes each)
- Preserves original filename with part numbering
- Shows progress bar during processing
- Supports various audio formats (m4a, mp3, wav, etc.)

## Tested On
Python 3.11.2