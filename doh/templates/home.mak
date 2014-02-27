<%namespace name="master" file="master.mak"/>
<%master:layout>
    <%def name="pagetitle()">Doh-score!</%def>


<%def name="scripts()">

<script>
 $(document).ready(function() {
   $('#answer').hide();
   $('#show-the-solution').click(function() {
       $('#answer').show();
       $('#title-buttons').hide();
   });
});
</script>
</%def>

<div class="jumbotron" >
  <p>${tip.title}</p>
  <p>
    % if tip.title_image != None:
      <img src="/images/${tip.title_image}" />
    % endif
  </p>
  <div id="title-buttons">
    <div class="col-lg-4">
      <a class="btn btn-primary bg-lg" id="show-the-solution" >I don't know</a>
    </div>
    <div class="col-md-pull-4" >
      <a class="btn btn-primary btn-lg" href="/">Next</a>
    </div>
  </div>
</div>
<div class="jumbotron" id="answer">
  <p>${tip.answer}</p>
  <p>
    <img src="/images/${tip.answer_image}" />
  </p>
  <div class="col-md-pull-4" >
    <a class="btn btn-primary btn-lg" href="/">Ok, got it!</a>
  </div>
</div>
</%master:layout>
