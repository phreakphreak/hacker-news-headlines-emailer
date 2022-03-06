from jinja2 import Template
import requests  # http requests
import datetime  # system date and time manipulation
import smtplib  # send email
from bs4 import BeautifulSoup  # web scraping
# email body
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

content = 'https://news.ycombinator.com/'

now = datetime.datetime.now()

URL_BASE = 'https://news.ycombinator.com/'


def extract_news(url):
    print("Extracting news...")
    cnt = ''
    cnt += '<h1>' + url + '</h1>' + '\n'
    cnt += '<h2>' + str(now) + '</h2>' + '\n'
    cnt += '<hr>' + '\n'
    cnt += '<h3>' + 'News' + '</h3>' + '\n'
    cnt += '<hr>' + '\n'
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    for i, tag in enumerate(soup.find_all('td', attrs={
        'class': 'title',
        'valign': ''
    })):
        cnt += ('<br>' + (str(i + 1) + ' :: ' + tag.text + '\n') if tag.text != 'More' else '')

    return cnt


data = extract_news(URL_BASE)

value = {'replace_me': data}

with open('index.html') as f:
    t = Template(f.read())

with open('HackerNews.html', 'w') as f:
    f.write(t.render(value))

print(data)
