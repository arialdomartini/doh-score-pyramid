import os
import uuid
from pyramid.response import Response
from pyramid.view import view_config
from pyramid.httpexceptions import HTTPFound

from sqlalchemy.exc import DBAPIError

from .models import (
    DBSession,
    Hint,
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

@view_config(route_name='home', renderer='home.mak')
def home(request):
    hint = DBSession.query(Hint).first()
    return {'hint': hint}

@view_config(route_name='hints.new', renderer='hints/new.mak')
def hint_new(request):
    if(request.method == 'GET'):
        return {'error': '', 'question': '', 'answer': ''}
    else:
        question = request.params['question']
        answer = request.params['answer']
        upload_dir = request.registry.settings['images.uploaded']
        question_image_filename = save_uploaded_file(request.POST['question_image'], upload_dir)
        answer_image_filename = save_uploaded_file(request.POST['answer_image'], upload_dir)

        model = Hint(question=question, question_image=question_image_filename, answer=answer, answer_image=answer_image_filename)
        DBSession.add(model)
        return HTTPFound(location = request.route_url('home'))
