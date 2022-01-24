
import sys
dict_users_hobbies={}
new_list_users=[]
new_list_hobbies=[]

with open('users.csv', encoding='utf-8') as file_users:
      for line in file_users:
        a = line.rstrip().replace(',', ' ')
        new_list_users.append(a)
      print(new_list_users)

with open('hobby.csv', encoding='utf-8') as file_hobbies:
      for line in file_hobbies:
        b = line.rstrip().split(',')
        new_list_hobbies.append(b)
      print(new_list_hobbies)

if len(new_list_hobbies) > len(new_list_users):
    sys.exit(1)

for i in range(len(new_list_users)):
    if i < len(new_list_hobbies):
        dict_users_hobbies[new_list_users[i]] = new_list_hobbies[i]
    else:
        dict_users_hobbies[new_list_users[i]] = None
print(dict_users_hobbies)

with open('dict_6_3', 'w', encoding='utf-8') as file:
    for k,v in dict_users_hobbies.items():
        file.write('{}: {}\n'.format(k,v))


