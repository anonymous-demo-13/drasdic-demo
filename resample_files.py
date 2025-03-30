import os
import librosa
import soundfile as sf

# Set the root directory and target sample rate
root_dir = '/Users/davidrobinson/Code/esp/drasdic-demo/audio'
target_sr = 16000

# Supported audio extensions (librosa can load many formats)
audio_extensions = ('.wav', '.mp3', '.flac', '.aac')

# Walk through all directories and files
for dirpath, dirnames, filenames in os.walk(root_dir):
    for filename in filenames:
        if filename.lower().endswith(audio_extensions):
            input_path = os.path.join(dirpath, filename)
            print(f"Processing {input_path}")
            try:
                # Load the audio file with its original sample rate (sr=None)
                y, sr = librosa.load(input_path, sr=None)
                if sr == target_sr:
                    print("  Already at 16 kHz, skipping.")
                    continue

                # Resample audio to target sample rate
                y_resampled = librosa.resample(y, orig_sr=sr, target_sr=target_sr)

                # Write the resampled audio back, overwriting the original
                sf.write(input_path, y_resampled, target_sr)
                print("  Resampled to 16 kHz.")
            except Exception as e:
                print(f"  Error processing {input_path}: {e}")
