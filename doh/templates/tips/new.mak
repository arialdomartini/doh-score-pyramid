<%namespace name="master" file="../master.mak"/>
<%master:layout>
    <%def name="pagetitle()">Register a new tip</%def>
        <div class="row">
          <div class="col-lg-16">
            <div class="well">
              <form class="bs-example form-horizontal" method="POST" accept-charset="utf-8" enctype="multipart/form-data">
                <fieldset>
                  <legend>New tip</legend>
                  <div class="form-group">
                    <label for="title" class="col-lg-12 control-label">Title</label>
                    <div class="col-lg-12">
                      <textarea class="form-control" name="title" type="text" placeholder="Title">${title}</textarea>
                    </div>
                  </div>
                  <div class="form-group">
                     <label for="title_image" class="col-lg-12 control-label">Image for the title</label>
                    <div class="col-lg-12">
                      <input name="title_image" class="form-control" type="file" value="" />
                    </div>
                  </div>
                  <div class="form-group">
                    <label for="answer" class="col-lg-12 control-label">Answer</label>
                    <div class="col-lg-12">
                      <textarea class="form-control" name="answer" type="text" placeholder="The answer">${answer}</textarea>
                    </div>
                  </div>
                  <div class="form-group">
                     <label for="answer_image" class="col-lg-12 control-label">Image for the answer</label>
                    <div class="col-lg-12">
                      <input name="answer_image" class="form-control" type="file" value="" />
                    </div>
                  </div>
                  <div class="form-group">
                    <div class="col-lg-10 col-lg-offset-2">
                      <button class="btn btn-default">Cancel</button>
                      <button type="submit" class="btn btn-primary">Submit</button>
                    </div>
                  </div>
                </fieldset>
              </form>
            </div>
          </div>
</%master:layout>
