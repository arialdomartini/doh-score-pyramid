<%namespace name="master" file="master.mak"/>
<%master:layout>
    <%def name="pagetitle()">Doh-score!</%def>
    <p>
        ${hint.title}
        <img src="/images/${hint.title_image}" />
    </p>
    <p>
        ${hint.answer}
        <img src="/images/${hint.answer_image}" />
    </p>
</%master:layout>
