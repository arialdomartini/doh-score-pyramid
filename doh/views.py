from pyramid.response import Response
from pyramid.view import view_config
from pyramid.httpexceptions import HTTPFound


from sqlalchemy.exc import DBAPIError

from .models import (
    DBSession,
    Hint,
    )


@view_config(route_name='home', renderer='home.mak')
def home(request):
    hint = DBSession.query(Hint).first()
    return {'project': 'doh', 'hint': hint.question}

@view_config(route_name='hints.new', renderer='hints/new.mak')
def hint_new(request):
    if(request.method == 'GET'):
        return {'error': '', 'question': '', 'answer': ''}
    else:
        question = request.params['question']
        answer = request.params['answer']
        #try:
        model = Hint(question=question, answer=answer)
        DBSession.add(model)
        return HTTPFound(location = request.route_url('home'))
        #except error:
        #    return {'error': error, 'question': question, 'answer': answer}
