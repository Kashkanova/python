new_list = []
with open('nginx_logs.txt') as file:
    lines = file.readlines()
    for line in lines:
        a = line.split(' ')
        new_list.append((a[0], a[5].strip('"'), a[6]))

for item in new_list:
    print(item)
