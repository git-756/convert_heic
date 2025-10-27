import sys
from pathlib import Path
from PIL import Image

# pillow-heif プラグインをPillowに登録します
# これにより、Image.open() が .heic ファイルを認識できるようになります
try:
    from pillow_heif import register_heif_opener
    register_heif_opener()
except ImportError:
    print("エラー: 'pillow_heif' がインストールされていません。")
    print("Rye環境で 'rye add pillow-heif' を実行してください。")
    sys.exit(1)


# --- 設定ここから ---

# 1. HEICファイルが保存されている親ディレクトリのパス
# このディレクトリ内のサブフォルダもすべて検索対象となります
INPUT_DIR = Path("./src/heic_2_jpg/picture")

# 2. 変換後のJPGファイルを保存するディレクトリのパス
# 元のフォルダ構造を維持したまま、ここに保存されます
OUTPUT_DIR = Path("./src/heic_2_jpg/output_jpg_files")

# 3. 保存するJPGの品質 (1-100, デフォルトは95)
JPG_QUALITY = 95

# --- 設定ここまで ---


def convert_heic_to_jpg(input_dir: Path, output_dir: Path, quality: int):
    """
    指定されたディレクトリ内のHEICファイルを再帰的に検索し、
    JPGに変換して出力ディレクトリに保存する。
    """
    print(f"スキャンを開始します: {input_dir}")
    print(f"保存先: {output_dir}")
    print("-" * 30)

    # 出力ディレクトリが存在しない場合は作成します
    output_dir.mkdir(parents=True, exist_ok=True)

    # .heic と .HEIC の両方を再帰的に検索します (rglob)
    # list() で囲むことで、検索を先に完了させ、処理数を把握します
    heic_files = list(input_dir.rglob('*.heic')) + list(input_dir.rglob('*.HEIC'))

    if not heic_files:
        print("変換対象のHEICファイルが見つかりませんでした。")
        print(f"検索ディレクトリ: {input_dir.resolve()}")
        return

    print(f"{len(heic_files)} 件のHEICファイルが見つかりました。変換を開始します...")

    success_count = 0
    fail_count = 0

    for i, heic_path in enumerate(heic_files):
        try:
            # 1. 出力パスを決定する
            # 入力ディレクトリからの相対パスを取得
            relative_path = heic_path.relative_to(input_dir)
            # 出力ディレクトリに相対パスを組み合わせ、拡張子を .jpg に変更
            jpg_path = output_dir / relative_path.with_suffix('.jpg')

            # 2. 出力先のサブディレクトリを作成する
            # (例: output_dir/subfolder/image.jpg の場合、'subfolder'を作成)
            jpg_path.parent.mkdir(parents=True, exist_ok=True)

            # 3. 画像を開いて変換・保存する
            with Image.open(heic_path) as image:
                
                # HEICは透明情報(RGBA)を持つことがありますが、JPGは持ちません(RGB)。
                # .convert('RGB') を呼び出すことで、透明情報を破棄し、
                # JPGとして保存できる形式に変換します。
                image.convert('RGB').save(jpg_path, format="JPEG", quality=quality)
            
            print(f"[{i+1}/{len(heic_files)}] 成功: {heic_path.name} -> {jpg_path.name}")
            success_count += 1

        except Exception as e:
            # 変換中にエラーが発生した場合
            print(f"[{i+1}/{len(heic_files)}] ★失敗★: {heic_path.name} (エラー: {e})")
            fail_count += 1

    print("-" * 30)
    print("変換処理が完了しました。")
    print(f"成功: {success_count} 件")
    print(f"失敗: {fail_count} 件")


if __name__ == "__main__":
    # スクリプトが直接実行された場合
    
    # 入力ディレクトリの存在チェック
    if not INPUT_DIR.exists():
        print(f"エラー: 入力ディレクトリが見つかりません: {INPUT_DIR.resolve()}")
        print("スクリプト内の INPUT_DIR を正しいパスに変更してください。")
        sys.exit(1)
        
    convert_heic_to_jpg(INPUT_DIR, OUTPUT_DIR, JPG_QUALITY)