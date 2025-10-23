"""
save.py
文字起こし結果をテキストファイルに保存するモジュール
- 上書きせず追記する仕様
- 他作業者が出力した文字列を簡単に受け取り保存可能
"""

def save_text(text: str, filename: str = "result.txt") -> None:
    """
    文字列をテキストファイルに保存
    ファイルが存在する場合は追記し、存在しない場合は新規作成

    Args:
        text (str): 保存する文字列
        filename (str): 保存するファイル名（デフォルト: result.txt）
    """
    with open(filename, "a", encoding="utf-8") as f:
        f.write(text + "\n")
    print(f"保存完了: {filename}")