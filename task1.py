
import os
import shutil
import argparse
from pathlib import Path


def parse_arguments():
    parser = argparse.ArgumentParser(
        description="Копіювання та сортування файлів за розширенням.")
    parser.add_argument("source_dir", help="Шлях до вихідної директорії")
    parser.add_argument("dest_dir", nargs='?', default="dist",
                        help="Шлях до директорії призначення (за замовчуванням 'dist')")
    return parser.parse_args()


def process_directory(source_path, dest_path):
    try:
        for entry in os.scandir(source_path):
            if entry.is_dir():
                process_directory(entry.path, dest_path)  # рекурсія
            elif entry.is_file():
                copy_file_by_extension(entry.path, dest_path)
    except PermissionError as e:
        print(f"[Помилка доступу] {e}")
    except Exception as e:
        print(f"[Помилка] {e}")


def copy_file_by_extension(file_path, dest_root):
    try:
        ext = Path(file_path).suffix.lower().strip(".")
        if not ext:  # если нет расширения — пропускаем
            print(f"Пропущено без розширення: {file_path}")
            return

        dest_folder = os.path.join(dest_root, ext)
        os.makedirs(dest_folder, exist_ok=True)

        dest_file_path = os.path.join(dest_folder, os.path.basename(file_path))
        shutil.copy2(file_path, dest_file_path)

        print(f"Скопійовано: {file_path} → {dest_file_path}")
    except Exception as e:
        print(f"Не вдалося скопіювати {file_path}: {e}")


def main():
    args = parse_arguments()
    source = os.path.abspath(args.source_dir)
    dest = os.path.abspath(args.dest_dir)

    print(f"Вихідна директорія: {source}")
    print(f"Директорія призначення: {dest}")

    if not os.path.exists(source):
        print(f"Вихідна директорія не існує: {source}")
        return

    os.makedirs(dest, exist_ok=True)
    process_directory(source, dest)
    print("Копіювання завершено.")


if __name__ == "__main__":
    main()
