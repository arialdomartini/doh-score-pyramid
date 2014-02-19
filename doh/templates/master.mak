<%def name="layout()">
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <title>${caller.pagetitle()}</title>
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <link rel="stylesheet" href="/static/css/bootstrap.css" media="screen">
    <link rel="stylesheet" href="/static/css/bootswatch.min.css">
    <!-- HTML5 shim and Respond.js IE8 support of HTML5 elements and media queries -->
    <!--[if lt IE 9]>
      <script src="/static/js/html5shiv.js"></script>
      <script src="/static/js/respond.min.js"></script>
    <![endif]-->
  </head>
  <body>
    <div class="navbar navbar-default navbar-fixed-top">
      <div class="container">
        <div class="navbar-header">
          <a href="../" class="navbar-brand">Doh-score</a>
          <button class="navbar-toggle" type="button" data-toggle="collapse" data-target="#navbar-main">
            <span class="icon-bar"></span>
            <span class="icon-bar"></span>
            <span class="icon-bar"></span>
          </button>
        </div>
        <div class="navbar-collapse collapse" id="navbar-main">
          <ul class="nav navbar-nav">
            <li class="dropdown">
              <a class="dropdown-toggle" data-toggle="dropdown" href="#" id="tags">Tags <span class="caret"></span></a>
              <ul class="dropdown-menu" aria-labelledby="themes">
                <li><a href="#">All</a></li>
                <li class="divider"></li>
                <li><a href="#">Photoshop</a></li>
                <li><a href="#">Illustrator</a></li>
                <li><a href="#">InDesign</a></li>
                <li><a href="#">Acrobat</a></li>
                <li><a href="#">WebStorm</a></li>
                <li><a href="#">Flash</a></li>
              </ul>
            </li>
            <li>
              <a href="/about">About</a>
            </li>
          </ul>

          <ul class="nav navbar-nav navbar-right">
            <li><a href="http://builtwithbootstrap.com/" target="_blank">Built With Bootstrap</a></li>
            <li><a href="https://wrapbootstrap.com/?ref=bsw" target="_blank">WrapBootstrap</a></li>
          </ul>

        </div>
      </div>
    </div>


    <div class="container">
      ${caller.body()}
    </div>
    

</div>
<script src="/static/js/jquery-1.10.2.min.js"></script>
<script src="/static/js/bootstrap.min.js"></script>
<script src="/static/js/bootswatch.js"></script>
</body>
</html>
</%def>
