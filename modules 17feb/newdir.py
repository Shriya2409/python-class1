import os
directory = "GeeksforGeeks"
parent_dir = "E:\python-class1"
path = os.path.join(parent_dir, directory)

os.mkdir(path)
print("Directory '% s' created" % directory)
directory = "Geeks"
parent_dir = "E:\python-class1"
mode = 0o666
path = os.path.join(parent_dir, directory)
os.mkdir(path, mode)
print("Directory '% s' created" % directory)