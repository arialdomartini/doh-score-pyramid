<%namespace name="master" file="../master.mak"/>
<%master:layout>
    <%def name="title()">Register a new hint</%def>

    <form method="POST" accept-charset="utf-8" enctype="multipart/form-data">
          <label for="answer">question</label>
          <textarea name="question" type="text" >${question}</textarea>

          <label for="question_image">Image for the question</label>
          <input name="question_image" type="file" value="" />

          <label for="answer">Answer</label>
          <textarea name="answer" type="text"/>${answer}</textarea>

          <label for="answer_image">Image for the answer</label>
          <input name="answer_image" type="file" value="" />

          <input type="submit" name="save" />
    </form>
</%master:layout>
