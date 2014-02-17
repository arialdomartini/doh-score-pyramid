<%namespace name="master" file="master.mak"/>
<%master:layout>
    <%def name="title()">Doh-score!</%def>
    <p>
        ${hint.question}
        <img src="/images/${hint.question_image}" />
    </p>
    <p>
        ${hint.answer}
        <img src="/images/${hint.answer_image}" />
    </p>
</%master:layout>
