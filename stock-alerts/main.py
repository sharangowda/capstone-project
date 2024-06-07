import requests
import datetime as dt
import os
from twilio.rest import Client


STOCK = "AdaniPower"
COMPANY_NAME = "ADANI"

API_KEY = ''


url = f'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=ADANIPOWER.BSE&apikey={API_KEY}'
r = requests.get(url)
data = r.json()

present = dt.datetime.now()
present_date = present.date()

prev = present - dt.timedelta(days=4)
prev_date = str(prev.date())

prev_1 = prev.date() - dt.timedelta(days=3)
prev_2 = str(prev_1)


present_closing_price = (
    data['Time Series (Daily)'].get(prev_date)['4. close'])
previous_day_closing_price = (
    data['Time Series (Daily)'].get(prev_2)['4. close'])

diff = float(present_closing_price) - float(previous_day_closing_price)
percent = (diff/float(present_closing_price))*100
print(percent)


NEWS_API = 'f903fbfa92704ae995e6a37a3c11ec34'


if percent > 3:
    news_url = f'https://newsapi.org/v2/everything?q=ADANI&domains=moneycontrol.com&apiKey={NEWS_API}'
    news_r = requests.get(news_url)
    news_json = news_r.json()

    article1 = news_json['articles'][0]['title']
    article1_url = news_json['articles'][0]['url']
    article1_content = news_json['articles'][0]['content']

    article2 = news_json['articles'][1]['title']
    article2_url = news_json['articles'][1]['url']
    article2_content = news_json['articles'][1]['content']

    article3 = news_json['articles'][2]['title']
    article3_url = news_json['articles'][2]['url']
    article3_content = news_json['articles'][2]['content']

    sms_sid = ''
    sms_auth_token = ''
    twilio_num = number

    account_sid = ""
    auth_token = ''
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        body=f'This is to remind you about your ADANIPWR stocks.\n Why dont you have a look at your account? \n while you are at that here are all the news articles for those stocks. \n {article1}\n{article1_url}\n {article1_content} \n {article2}\n {article2_url}\n {article2_content}\n {article3}\n {article3_url}\n {article3_content}',
        from_='twilio number',
        to='your phone number')


