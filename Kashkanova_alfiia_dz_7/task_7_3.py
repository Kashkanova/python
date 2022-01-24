import argparse
import os
import shutil

parser = argparse.ArgumentParser()

parser.add_argument('--input', required = True)
parser.add_argument('--output', required = True)

args = parser.parse_args()

for dirpath, dirnames,filenames in os.walk(args.input):
    for dirname in dirnames:
        print(dirpath, dirname)
        if 'templates' in dirname:
            shutil.copytree(os.path.join(dirpath, 'templates' ),
                            os.path.join(args.output, 'templates' ), dirs_exist_ok=True)
