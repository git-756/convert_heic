# HEIC to JPG Converter

`HEIC to JPG Converter`は、iPhoneなどで撮影されたHEIC（`.heic`）形式の画像ファイルを、汎用的なJPG（`.jpg`）形式に一括変換するためのPythonスクリプトです。

---

## ✨ 主な機能

- **再帰的検索**: 指定した入力ディレクトリ（サブフォルダを含む）内のすべての `.heic` / `.HEIC` ファイルを自動で検索します。
- **フォルダ構造の維持**: 元のフォルダ構造を保ったまま、指定した出力ディレクトリに変換後のJPGファイルを保存します。
- **透明情報（アルファチャンネル）の自動処理**: HEICファイルが持つ透明情報（RGBA）を自動的にRGBに変換し、JPGとして正しく保存します。
- **品質指定**: 保存するJPGの品質（1〜100）を指定できます。

---

## ⚙️ 動作要件

- Python 3.8 以上
- **pillow**
- **pillow-heif**

---

## 🚀 使い方

1.  **リポジトリのクローン**
    ```bash
    git clone [リポジトリのURL]
    cd convert_heic
    ```

2.  **依存ライブラリのインストール**
    ```bash
    # Ryeを使用している場合
    rye sync
    # pipを直接使用する場合
    # pip install pillow pillow-heif
    ```

3.  **スクリプトの編集**
    - `src/heic_2_jpg/convert_heic.py` を開き、冒頭の**設定項目**を編集します。

    ```python
    # --- 設定ここから ---

    # 1. HEICファイルが保存されている親ディレクトリのパス
    INPUT_DIR = Path("./src/heic_2_jpg/picture")

    # 2. 変換後のJPGファイルを保存するディレクトリのパス
    OUTPUT_DIR = Path("./src/heic_2_jpg/output_jpg_files")

    # 3. 保存するJPGの品質 (1-100, デフォルトは95)
    JPG_QUALITY = 95
    
    # --- 設定ここまで ---
    ```

4.  **スクリプトの実行**
    - ターミナルで以下のコマンドを実行します。

    ```bash
    python src/heic_2_jpg/convert_heic.py
    ```

5.  **結果の確認**
    - 実行後、ターミナルに進捗が表示され、`OUTPUT_DIR`で指定したフォルダにJPGファイルが生成されます。

---

## 📜 ライセンス

このプロジェクトは **MIT License** のもとで公開されています。ライセンスの全文については、[LICENSE](LICENSE) ファイルをご覧ください。

また、このプロジェクトはサードパーティ製のライブラリを利用しています。これらのライブラリのライセンス情報については、[NOTICE.md](NOTICE.md) ファイルに記載しています。

## 作成者
[Samurai-Human-Go](https://samurai-human-go.com/%e9%81%8b%e5%96%b6%e8%80%85%e6%83%85%e5%a0%b1/)
- [ブログ記事: 【Python】HEIC画像をJPGに一括変換するスクリプト開発記【Pillow / pillow-heif】](https://samurai-human-go.com/python-convert-heic-to-jpg/)