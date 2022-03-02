import unittest
from models import news_sources

News_sources = news_sources.News_sources


class News_sourcesTest(unittest.TestCase):

    def setUp(self):

        self.new_news_sources = News_sources('abc-news', 'name', 'Your trusted source for breaking news, analysis, exclusive interviews, headlines, and videos at ABCNews.com',
        'https://abcnews.go.com', 'general', 'en', 'us')





    def test_instance(self):

        self.assertTrue(isinstance(self.new_news_sources, News_sources))

if __name__=='__main__':
    unittest.main()

