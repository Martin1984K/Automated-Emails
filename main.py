import yagmail
import pandas as pd
from news import NewsFeed
import datetime
import time
from api_keys import gmail_app_password

def send_email():
    today = datetime.datetime.now().strftime('%Y-%m-%d')
    yesterday = (datetime.datetime.now() - datetime.timedelta(days=1)).strftime('%Y-%m-%d')
    news_feed = NewsFeed(interest=row['interest'],
                         from_date=yesterday,
                         to_date=today)
    email = yagmail.SMTP(user="dataanarchist1984@gmail.com",
                         password=gmail_app_password)
    email.send(to=row['email'],
               subject=f"Your {row['interest']} news for today",
               contents=f"Hi {row['name']},\n\n See what´s on about {row['interest']} today. {news_feed.get()}\nMartin")


while True:
    if datetime.datetime.now().hour == 15 and datetime.datetime.now().minute == 40:
        df = pd.read_excel('people.xlsx')

        for index, row in df.iterrows():
            send_email()

    time.sleep(60)

