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


def save_uploaded_file(form_field, upload_dir):
        input_file = form_field.file
        the_name = "%s.pic" % uuid.uuid4()
        file_path = os.path.join(upload_dir, the_name)

        temp_file_path = file_path + '~'

        output_file = open(temp_file_path, 'wb')
        # Finally write the data to a temporary file
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

@view_config(route_name='home', renderer='home.mak')
def home(request):
    tip = DBSession.query(Tip).order_by("RANDOM()").first()
    return {'tip': tip}

@view_config(route_name='tips.new', renderer='tips/new.mak')
def tips_new(request):
    if(request.method == 'GET'):
        return {'error': '', 'title': '', 'answer': ''}
    else:
        title = request.params['title']
        answer = request.params['answer']
        upload_dir = request.registry.settings['images.uploaded']
        if request.POST['title_image'] != None:
                title_image_filename = save_uploaded_file(request.POST['title_image'], upload_dir)
        else:
                title_image_filename = None
        answer_image_filename = save_uploaded_file(request.POST['answer_image'], upload_dir)

        model = Tip(title=title, title_image=title_image_filename, answer=answer, answer_image=answer_image_filename)
        DBSession.add(model)
        return HTTPFound(location = request.route_url('home'))
