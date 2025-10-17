from pydub import AudioSegment
import math
import os
from tqdm import tqdm

# Set ffmpeg paths to local executables
AudioSegment.converter = os.path.join(os.getcwd(), "ffmpeg.exe")
AudioSegment.ffmpeg = os.path.join(os.getcwd(), "ffmpeg.exe")
AudioSegment.ffprobe = os.path.join(os.getcwd(), "ffprobe.exe")


def split_audio(input_file: str, output_folder: str, part_length_minutes: int = 15):
    # Get original filename without extension
    original_filename = os.path.splitext(os.path.basename(input_file))[0]
    file_ext = input_file.split(".")[-1].lower()

    print("🎵 Loading audio file...")
    # Load the audio file
    audio = AudioSegment.from_file(input_file, format=file_ext)

    # Convert minutes to milliseconds
    part_length_ms = part_length_minutes * 60 * 1000
    total_length_ms = len(audio)

    # Calculate number of parts
    num_parts = math.ceil(total_length_ms / part_length_ms)

    # Ensure output folder exists
    os.makedirs(output_folder, exist_ok=True)

    print(f"📂 Splitting into {num_parts} parts...")

    # Split and export with progress bar
    for i in tqdm(range(num_parts), desc="Processing parts", unit="part"):
        start_time = i * part_length_ms
        end_time = min((i + 1) * part_length_ms, total_length_ms)
        part = audio[start_time:end_time]

        # Use original filename with part suffix
        part_filename = f"{original_filename}_part_{i + 1:02d}.{file_ext}"
        output_path = os.path.join(output_folder, part_filename)

        # Use mp4 format for m4a files (ffmpeg compatibility)
        export_format = "mp4" if file_ext == "m4a" else file_ext
        part.export(
            output_path,
            format=export_format,
            codec="aac" if file_ext == "m4a" else None,
        )

    print(f"\n🎧 Done! Created {num_parts} parts in '{output_folder}'")
    print(
        f"📝 Files named: {original_filename}_part_01.{file_ext}, {original_filename}_part_02.{file_ext}, etc."
    )


if __name__ == "__main__":
    directory = "G:\\Folder Name\\Another Folder Name\\"
    filename = "filename.m4a"

    # Check if file exists first
    full_path = os.path.join(directory, filename)
    if os.path.exists(full_path):
        print(f"🎵 Processing: {filename}")
        split_audio(full_path, directory)
    else:
        print(f"❌ File not found: {full_path}")
        print("Please check the path and filename.")
        print("\n📁 Current directory files:")
        for file in os.listdir("."):
            print(f"  - {file}")
