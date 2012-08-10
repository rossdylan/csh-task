from pyramid.view import view_config
import util


@view_config(route_name='index', renderer='index.mak')
def index_view(request):
    user = util.get_user(request)
    recent_tasks = util.get_recent_tasks()
    return dict(
            title = "index",
            user = user,
            r_tasks = recent_tasks,
            )
