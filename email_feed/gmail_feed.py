import xmltodict
import re
import requests
import datetime
from datetime import datetime, timedelta

username="xxx"
password="xxx"

URL = 'https://%s:%s@mail.google.com/mail/u/0/feed/atom/all' % (username, password)
r = requests.get(URL)

if r.status_code == 401:
    print("login [%s] or password [%s] is incorrect\n%s" % (username, password, 'Also try enable "Allow less secure apps" on https://myaccount.google.com/lesssecureapps and |Gmail Settings -> Forwarding and POP / IMAP -> IMAP Acess to Enable IMAP| '))
elif r.status_code != 200:
    print("Requests error [%s] - %s" % (r.status_code, URL))
elif r.status_code == 200:
    contents = r.text
    a = xmltodict.parse(contents)
    now_date=datetime.now()
    for k in range(len(a['feed']['entry'])):
        text = a['feed']['entry'][k]['summary']
        key_words1 = re.findall('unsusbscribe', text)
        key_words2 = re.findall('Stop these mails', text)
        keys=key_words1+key_words2
        urls = re.findall('(?:(?:https?|ftp):\/\/)?[\w/\-?=%.]+\.[\w/\-&?=%.]+', text)
        if len(keys) > 0 and len(urls)> 0:
            print(a['feed']['entry'][k]['title'])
            print(a['feed']['entry'][k]['summary'][0:50])
            print(a['feed']['entry'][k]['author']['email'])
            print(urls)
            print('----------')
