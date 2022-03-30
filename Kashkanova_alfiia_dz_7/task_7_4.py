import os
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--input', required = True)
args = parser.parse_args()

dict_files = {100 : 0,
              1000 : 0,
              10000 : 0,
              100000 : 0,
              'big' : 0}

for dirpath, dirnames,filenames in os.walk(args.input):
    print(len(filenames))
    for file in filenames:
        file_size = os.stat(os.path.join(dirpath,file)).st_size
        if file_size <= 100:
            dict_files[100]+=1
        elif file_size <= 1000:
            dict_files[1000]+=1
        elif file_size <= 10000:
            dict_files[10000]+=1
        elif file_size <= 100000:
            dict_files[100000]+=1
        else:
            dict_files['big'] += 1

    print(dict_files)
    