from flask import render_template, request, redirect, url_for
from . import main
from ..request import get_news
from ..models import News

@main.route("/")
def index():

    title = 'Home - The hottest news around the globe'
    top_news = get_news('articles')
    print(top_news)
    return render_template('index.html', title=title, top_news = top_news)
