<%
	pages = [("Tasks", "/tasks"), ("Search", "/search"), ("Create", "/create")]
%>
<!DOCTYPE html>
<html>
	<head>
		<meta charset="UTF-8">
		<link rel="stylesheet" href="/static/bootstrap/css/bootstrap.min.css" />
		<link rel="stylesheet" href="/static/bootstrap/css/bootstrap-responsive.min.css" />
	</head>

	<body>
		<div class="navbar navbar-fixed-top">
			<div class="navbar-inner">
				<div class="container-fluid">
					<a class="btn btn-navbar" data-target=".nav-collapse" data-toggle="collapse">
						<span class="icon-bar"></span>
						<span class="icon-bar"></span>
						<span class="icon-bar"></span>
					</a>
					<a class="brand" href="/"> CSH Tasks </a>
					<div class="btn-group pull-right">
						<a class="btn dropbown-toggle" href="#" data-toggle="dropdown">
							<i class="icon-user"></i>
							${username}
							<span class="caret"> </span>
						</a>
						<ul class="dropdown-menu">
							<li>
								<a href="/Assigned"> Assigned Tasks </a>
							</li>
							<li class="divider"> </li>
							<li>
								<a href="/created"> Created Tasks </a>
							</li>
						</ul>
					</div>
					<div class="nav-collapse">
						<ul class="nav">
							% for page in pages:
								% if page[0] == title:
									<li class="active">
								% else:
									<li>
								% endif
								<a href=${page[1]}> ${page[0]} </a>
								</li>
							% endfor
						</ul>
					</div>
				</div>
			</div>
		</div>

		${self.body}
	</body>
</html>
