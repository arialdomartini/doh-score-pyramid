from pyramid.config import Configurator
from sqlalchemy import engine_from_config

from .models import (
    DBSession,
    Base,
    )
from pyramid.session import UnencryptedCookieSessionFactoryConfig

def main(global_config, **settings):
    engine = engine_from_config(settings, 'sqlalchemy.')
    DBSession.configure(bind=engine)
    Base.metadata.bind = engine

    session_factory = UnencryptedCookieSessionFactoryConfig('yuvstyuiHHKctic276c5267c567c3t2yuiv')

    config = Configurator(settings=settings)
    config.set_session_factory(session_factory)


    uploaddir = settings['images.uploaded']


    config.add_static_view(name='images', path=uploaddir)
    config.add_static_view('static', 'static', cache_max_age=3600)
    config.add_route('home', '/')
    config.add_route('the_end', '/end')
    config.add_route('about', '/about')
    config.add_route('tips.new', '/tips/new')

    config.scan()

    return config.make_wsgi_app()
