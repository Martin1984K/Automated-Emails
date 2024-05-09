import requests
from api_keys import news_api_key


class NewsFeed:
    """Representing multiple news titles and links as a single string
    """
    base_url = 'https://newsapi.org/v2/everything?'
    api_key = news_api_key

    def __init__(self, interest, from_date, to_date, language='en'):
        self.interest = interest
        self.from_date = from_date
        self.to_date = to_date
        self.language = language

    def get(self):
        articles = self._get_articles()

        email_body = ''
        for article in articles:
            email_body = email_body + article['title'] + "\n" + article['url'] + '\n\n'

        return email_body

    def _get_articles(self):
        url = self._build_url()
        response = requests.get(url)
        content = response.json()
        articles = content['articles']
        return articles

    def _build_url(self):
        url = f'{self.base_url}' \
              f'qInTitle={self.interest}&' \
              f'from={self.from_date}&' \
              f'to={self.to_date}&' \
              f'language={self.language}&' \
              f'apiKey={self.api_key}'
        return url


if __name__ == '__main__':
    news_feed = NewsFeed(interest="robots",
                         from_date='2024-05-07',
                         to_date='2024-05-08',
                         language='en')
    print(news_feed.get())
