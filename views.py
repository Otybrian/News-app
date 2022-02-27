from flask import render_template
from app import app
from .request import get_news, get_news_sources


@app.route('/')
def index():


    header="Welcome to the best news application online"
    title= "Home - Welcome to the best news application online"
    top_news = get_news('articles')
    print(top_news)
    our_sources = 'News Sources'
    newsSource = get_news_sources('sources')
    print(newsSource)
    



    return render_template('index.html', title=title, header=header, top_news = top_news, ur_sources=our_sources, newsSource = newsSource)

# @app.route('/sources.html')
# def sources():



#     our_sources = 'News Sources'
#     newsSource = get_news_sources('sources')
#     print(newsSource)

#     return  render_template('sources.html', our_sources=our_sources, newsSource = newsSource)
    

