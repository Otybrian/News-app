class Config:
    '''
    General configuration parent class
    '''
    ALL_NEWS_API_BASE_URL='https://newsapi.org/v2/everything?q=keyword&apiKey'
    MY_API_KEY = '96519c65e70642e695e6cd44b70f0d5e'
    TOP_NEWS = 'https://newsapi.org/v2/top-headlines?country=us&apiKey=96519c65e70642e695e6cd44b70f0d5e'
    NEWS_SOURCES = 'https://newsapi.org/v2/top-headlines?sources=bbc-news&apiKey=96519c65e70642e695e6cd44b70f0d5e'



class ProdConfig(Config):
    '''
    Production  configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''
    pass


class DevConfig(Config):
    '''
    Development  configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''

    DEBUG = True