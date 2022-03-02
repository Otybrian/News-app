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
    news_source = get_news_sources('sources')
    print(news_source)
    



    return render_template('index.html', title=title, header=header, top_news = top_news, our_sources=our_sources, news_source = news_source)
    
    

