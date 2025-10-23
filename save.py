import mlx_whisper
from pydub import AudioSegment
import numpy as np
from save import save_text  # 作業者3のモジュールをインポート

# -------------------------------
# 単体ファイルの文字起こし
# -------------------------------
audio_file_path = "python-audio-output.wav"

result = mlx_whisper.transcribe(
    audio_file_path, path_or_hf_repo="whisper-base-mlx"
)
text_result = result['text']
print("文字起こし結果:", text_result)

# 作業者3に渡して保存
save_text(text_result, filename="result.txt")

# -------------------------------
# 複数ファイルの文字起こし
# -------------------------------
def preprocess_audio(sound):
    if sound.frame_rate != 16000:
        sound = sound.set_frame_rate(16000)
    if sound.sample_width != 2:
        sound = sound.set_sample_width(2)
    if sound.channels != 1:
        sound = sound.set_channels(1)
    return sound

audio_files = ["audio-output-before.wav", "audio-output-after.wav"]

for file in audio_files:
    sound = AudioSegment.from_file(file, format="wav")
    sound = preprocess_audio(sound)

    arr = np.array(sound.get_array_of_samples()).astype(np.float32) / 32768.0
    result = mlx_whisper.transcribe(
        arr, path_or_hf_repo="whisper-base-mlx"
    )
    text_result = result['text']
    print(f"{file} の文字起こし結果:", text_result)

    # 作業者3に渡して保存
    save_text(text_result, filename="result.txt")