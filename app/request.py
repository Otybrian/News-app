import urllib.request,json
from .models import News




api_key = None


def configure_request(app):
    
    global api_key
    api_key = app.config['NEWS_API_KEY']

def get_news(articles):

    top_news_url = api_key

    

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
