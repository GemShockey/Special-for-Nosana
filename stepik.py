import requests
import re

url = input().strip()
html_text = requests.get(url).text
regex = r"<a.+?href=[\"\']((https?://)|(ftp://))?(\w[\w\.\-]+).*?>"

url_groups = re.findall(regex, html_text)
url_lst = []
for groups in url_groups:
    url_lst.append(groups[-1])
url_lst = list(set(url_lst))
url_lst.sort()

for url in url_lst:
    print(url)
