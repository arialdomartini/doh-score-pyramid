from pyramid.response import Response
from pyramid.view import view_config

from sqlalchemy.exc import DBAPIError

from .models import (
    DBSession,
    Hint,
    )


@view_config(route_name='home', renderer='home.mak')
def home(request):
    hint = DBSession.query(Hint).first()
    return {'project': 'doh', 'hint': hint.question}


