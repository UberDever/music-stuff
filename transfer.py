import shutil
import os
import constants as c
import argparse

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '-p', '--path', help='Path to transfer directory', required=True)
    parser.add_argument(
        '-d', '--delete',
        help='Should delete files after transfer', required=True,
        choices=['y', 'n']
    )
    args = parser.parse_args()

    for src, dirs, files in os.walk(c.OUT_DIR):
        if src == c.TMP_DIR or src == c.OUT_DIR:
            continue
        src = src.replace(':', '')
        dst = args.path + os.sep + os.path.basename(src)
        if os.path.exists(dst):
            print(f'Skipping {dst} since it exists in the source')
            continue
        print(f'Copying from {src} to {dst}')
        try:
            shutil.copytree(src, dst)
        except OSError:
            # shutil doesn't bother to fill errno code,
            # so skip all exceptions
            pass
        if args.delete == 'y':
            for file in files:
                path = src + os.sep + file
                print(f'Removing {path}')
                os.remove(path)
