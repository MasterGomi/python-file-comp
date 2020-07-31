import os
from os.path import join
import sys
import filecmp
import time
from collections import defaultdict

def get_index(value, tuple_list):
    for i in range(len(tuple_list)):
        if value in tuple_list[i]:
            return i
    return -1

if len(sys.argv) > 1:
    if not os.path.isdir(sys.argv[1]):
        print("Path supplied is not recognised as a directory")
        time.sleep(3)
        raise SystemExit
    os.chdir(sys.argv[1])
else:
    os.chdir(os.path.dirname(sys.argv[0]))

master_file_list = []
for root, dirs, files in os.walk('.'):
    for name in files:
        master_file_list.append(os.path.join(root, name))

duplicate_files = []
compared = defaultdict(lambda: [])

for cur_file in master_file_list:
    for other_file in (f for f in master_file_list if f is not cur_file and f not in compared[cur_file]):
        if filecmp.cmp(cur_file, other_file, shallow=False):
            cur_file_index = get_index(cur_file, duplicate_files)
            if cur_file_index > -1:
                compared[other_file].extend(iter(duplicate_files[cur_file_index]))
                for files in (f for f in duplicate_files[cur_file_index] if f is not cur_file):
                    compared[files].append(other_file)
                duplicate_files[cur_file_index] += (other_file,)
                continue
            else:
                duplicate_files.append((cur_file, other_file))
        compared[other_file].append(cur_file)

f = open("Found Duplicate Files.txt", 'w')
for t in duplicate_files:
    for files in t:
        f.write(files + "\n")
    f.write("\n\n")
f.close()