import os
dir_name = 'my_project'
folders = ['settings', 'mainapp', 'adminapp', 'authapp']

if not os.path.exists(dir_name):
    os.mkdir(dir_name)

for f in folders:
    f = os.path.join(dir_name, f)
    print(f)
    if not os.path.exists(f):
        os.mkdir(f)