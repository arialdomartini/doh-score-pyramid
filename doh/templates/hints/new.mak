<%namespace name="master" file="../master.mak"/>
<%master:layout>
    <%def name="title()">Register a new hint</%def>

    <form method="POST">
          <label for="answer">question</label>
          <textarea name="question" type="text" >${question}</textarea>
          <label for="answer">Answer</label>
          <textarea name="answer" type="text"/>${answer}</textarea>
          <input type="submit" name="save" />
    </form>
</%master:layout>
