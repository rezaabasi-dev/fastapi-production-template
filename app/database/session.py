from sqlalchemy import create_engine

def get_engine(url):
    return create_engine(url)
