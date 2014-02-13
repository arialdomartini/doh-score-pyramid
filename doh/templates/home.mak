<%namespace name="master" file="master.mak"/>
## calls the layout def
<%master:layout>
    <%def name="title()">Hello world!</%def>
    this is the project ${project} ${hint}
</%master:layout>
