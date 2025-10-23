"""
audio_recorder.py
-----------------
マイクから10秒間の音声を録音し、WAVファイルとして保存するモジュール。

他の人（例: 文字起こし担当）が簡単に使えるように関数化しています。

使用例:
    from audio_recorder import record_audio
    record_audio(duration=10, output_file="sample.wav")
"""

import ffmpeg


def record_audio(duration: int = 10, output_file: str = "python-audio-output.wav"):
    """
    マイクから指定秒数の音声を録音し、指定ファイルに保存します。

    Parameters
    ----------
    duration : int, optional
        録音時間（秒）。デフォルトは10秒。
    output_file : str, optional
        保存先のファイル名。デフォルトは 'python-audio-output.wav'。

    Notes
    -----
    macOSでは `avfoundation`、Windowsでは `dshow`、Linuxでは `alsa` が利用されます。
    必要に応じて ffmpeg コマンドの入力設定を変更してください。
    """
    try:
        print(f"{duration}秒間、マイクからの録音を開始します...")

        # macOS用設定
        (
            ffmpeg
            .input(':0', format='avfoundation', t=duration) # macOSの例
            .output(output_file, acodec='pcm_s16le', ar='44100', ac=1)
            .run(overwrite_output=True)
        )

        print(f"✅ 録音完了: {output_file} に保存されました。")

    except ffmpeg.Error as e:
        print(f"⚠️ FFmpegエラー: {e.stderr.decode() if e.stderr else e}")
    except Exception as e:
        print(f"⚠️ 予期せぬエラー: {e}")


# テスト実行用（直接実行されたときのみ動作）
if __name__ == "__main__":
    record_audio()
