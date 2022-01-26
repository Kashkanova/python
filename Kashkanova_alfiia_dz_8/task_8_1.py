import re

def email_parse(email_adress):
    dict_email = {}

    result = re.findall(r'^[0-9A-z.]+@\w+\.\w+', email_adress)
    print(result)
    if len(result)<1:
      raise ValueError('неверный адрес электронной почты')
    result = re.split(r'@', email_adress)

    dict_email['username']=result[0]
    dict_email['domain'] = result[1]
    return dict_email
print(email_parse('As.df@gmail.com'))