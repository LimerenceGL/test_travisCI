import re

import requests

url = "https://www.ucas.ac.cn/site/37"
headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.63 Safari/537.36 Edg/93.0.961.47'
}

s = requests.session()
s.headers = headers
r = s.get(url, verify=False)
# print(r.text)
mail=re.search('邮编.*?</p>',r.text)
tel=re.search('联系电话：.*?</p>',r.text)
print(mail.group(0)[:-5])
print(tel.group(0)[:-5])
