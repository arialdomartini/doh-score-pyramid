<%namespace name="master" file="../master.mak"/>
<%master:layout>
    <%def name="title()">Register a new hint</%def>
        <div class="row">
          <div class="col-lg-16">
            <div class="well">
              <form class="bs-example form-horizontal" method="POST" accept-charset="utf-8" enctype="multipart/form-data">
                <fieldset>
                  <legend>New hint</legend>
                  <div class="form-group">
                    <label for="question" class="col-lg-12 control-label">Question</label>
                    <div class="col-lg-12">
                      <textarea class="form-control" name="question" type="text" placeholder="The question">${question}</textarea>
                    </div>
                  </div>
                  <div class="form-group">
                     <label for="question_image" class="col-lg-12 control-label">Image for the question</label>
                    <div class="col-lg-12">
                      <input name="question_image" class="form-control" type="file" value="" />
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
