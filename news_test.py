import unittest
from models import news

News = news.News


class NewsTest(unittest.TestCase):


    def setUp(self):

        self.new_news = News('source','Timothy Carter', 'What You Need to Know Before Trying SEO On Your Own',
        "Search engine optimization (SEO) has something of an allure to it. It’s a kind of digital magic that allows businesses to rank higher in search engine results pages (SERPs) and earn more organic traffic as a result. It’s also alluring because it’s ridiculousl…"
        ,"https://readwrite.com/what-you-need-to-know-before-trying-seo-on-your-own/","https://images.readwrite.com/wp-content/uploads/2022/02/Know-Before-Trying-SEO.jpg",
        "2022-02-24T00:00:50Z", 
        "Search engine optimization (SEO) has something of an allure to it. Its a kind of digital magic that allows businesses to rank higher in search engine results pages (SERPs) and earn more organic traff… [+7737 chars]")


    def test_instance(self):
        self.assertTrue(isinstance(self.new_news, News))


if __name__ == '__main__':
    unittest.main()