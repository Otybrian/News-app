from flask import render_template
from app import app
from .request import get_news, get_news_sources


@app.route('/')
def index():


    header="Welcome to the best news application online"
    title= "Home - Welcome to the best news application online"
    top_news = get_news('articles')
    print(top_news)
    



    return render_template('index.html', title=title, header=header, top_news = top_news)

@app.route('/bbc')
def bbc():


    
    news_sources = get_news_sources('bbc')
    print(news_sources)

    return render_template('bbc.html',news_sources = news_sources)

