# python-file-comp
Compares all files (incl. subdirs) in the directory that it is executed from to spot duplicate files (even with different filenames)

There are two (only slightly) different versions of this script. Unlike CompareShallow.py, CompareDeep.py performs a byte by byte comparison of each file. However, it is rather unlikely that CompareDeep.py will pick up on anything CompareShallow.py would have, and execution time increases **massively** depending on file size for CompareDeep.py, so I recommend only using CompareShallow.py.

To use this script, pass the script a directory path as a command line argument or move/copy the file to the top level of the directory whose files you wish to compare and execute it. After execution is complete, a file will be genereated in that directory called "Found Duplicate Files.txt" which contains a list of all found duplicates in the following format:
```
.\file1.file
.\dir1\file1-copy.file


.\file2.file
.\file2-copy.file
.\dir2\dir3\poorlynamedfile.file

[etc.]
```
Where duplicate files are grouped together as seen above.
