<%namespace name="master" file="master.mak"/>
<%master:layout>
    <%def name="title()">Hello world!</%def>
    this is the project ${project} ${hint.question}

    <p>The src is /images/${hint.question_image}</p>
    <img src="/images/${hint.question_image}" />
</%master:layout>
