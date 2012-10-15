<%inherit file="master.mak"/>

<div class="container-fluid">
	<div class="row-fluid">
		<div class="span3">
			<div class="well sidebar-nav">
				<ul class="nav navlist">
					<li class="nav-header"> My Tasks </li>
					% if len(u_tasks) == 0:
						<li>
							<b> You No Tasks </b>
						</li>
					% endif
					% for task in u_tasks:
						<li>
						<a href="/tasks/${task.id}"> ${task.id} - ${task.title} </a>
						</li>
					% endfor
				</ul>
			</div>
		</div>
	</div>
</div>
