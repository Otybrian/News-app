from app import app
import urllib.request, json
from .models import news
from .models import news_sources


News = news.News
News_sources = news_sources.News_sources


top_news_url = app.config['TOP_NEWS']
news_sources_url = app.config['NEWS_SOURCES']

def get_news(articles):

    

    with urllib.request.urlopen(top_news_url) as url:
        get_news_data = url.read()
        get_news_response = json.loads(get_news_data)


        news_results = None

        if get_news_response['articles']:

            news_results_list = get_news_response['articles']

            news_results = process_results(news_results_list)


        
    return news_results




def process_results(news_list):

    news_results = []
    for news_item in news_list:
        source_name = news_item.get('source')
        author = news_item.get('author')
        title = news_item.get('title')
        description = news_item.get('description')
        url = news_item.get('url')
        urlToImage = news_item.get('urlToImage')
        publishedAt = news_item.get('publishedAt')
        content = news_item.get('content')


        if source_name:

            news_object = News(source_name, author, title, description, url, urlToImage, publishedAt, content)
            news_results.append(news_object)



    return news_results



def get_news_sources(bbc):



    with urllib.request.urlopen(news_sources_url) as url:
        get_news_sources_data = url.read()
        get_news_sources_response = json.loads(get_news_sources_data)


        news_sources_results = None

        if get_news_sources_response['bbc']:

            news_sources_results_list = get_news_sources_response['bbc']

            news_sources_results = display_results(news_sources_results_list)

    return news_sources_results


def display_results(news_sources_list):

    news_sources_results = []
    for news_sources_item in news_sources_list:
        id = news_sources_item.get('id')
        name = news_sources_item.get('name')
        description = news_sources_item.get('description')
        url = news_sources_item.get('url')
        category = news_sources_item.get('category')
        language = news_sources_item.get('language')
        country = news_sources_item.get('country')

        if id:

            news_sources_object = News(id, name, description, url, category, language, country)
            news_sources_results.append(news_sources_object)

        return news_sources_results
