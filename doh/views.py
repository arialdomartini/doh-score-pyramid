import os
import uuid
from pyramid.response import Response
from pyramid.view import view_config
from pyramid.httpexceptions import HTTPFound

from sqlalchemy.exc import DBAPIError

from .models import (
    DBSession,
    Tip,
    )

from .domain import TipsRepository

def save_uploaded_file(form_field, upload_dir):
    input_file = form_field.file
    original_filename = form_field.filename
    the_name = "%s.%s" %( uuid.uuid4(), os.path.basename(original_filename) )
    file_path = os.path.join(upload_dir, the_name)
    
    temp_file_path = file_path + '~'
    
    output_file = open(temp_file_path, 'wb')

    input_file.seek(0)
    while True:
        data = input_file.read(2<<16)
        if not data:
            break
        output_file.write(data)

    output_file.close()

    os.rename(temp_file_path, file_path)

    return the_name

@view_config(route_name='about', renderer='about.mak')
def about(request):
    return {}


def get_current_session(request):
    session = request.session
    if 'usr' not in session:
        request.session['usr'] = uuid.uuid4()
#        request.session.save()

    return request.session['usr']


@view_config(route_name='home', renderer='home.mak')
def home(request):
    session = get_current_session(request)

    repo = TipsRepository()
    tip = repo.get_next()

    return {'tip': tip, 'session': session}


@view_config(route_name='tips.new', renderer='tips/new.mak')
def tips_new(request):
    if(request.method == 'GET'):
        return {'error': '', 'title': '', 'answer': ''}
    else:
        title = request.params['title']
        answer = request.params['answer']
        upload_dir = request.registry.settings['images.uploaded']
        title_image = request.POST.get('title_image')
        if hasattr(title_image, 'filename'):
                title_image_filename = save_uploaded_file(request.POST['title_image'], upload_dir)
        else:
                title_image_filename = None
        answer_image_filename = save_uploaded_file(request.POST['answer_image'], upload_dir)

        model = Tip(title=title, title_image=title_image_filename, answer=answer, answer_image=answer_image_filename)
        DBSession.add(model)
        return HTTPFound(location = request.route_url('home'))
