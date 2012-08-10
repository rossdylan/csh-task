from pyramid.view import view_config
import util


@view_config(route_name='index', renderer='index.mak')
def index_view(request):
    user = util.get_user(request)
    users_tasks = util.get_assigned_tasks(user.id)
    return dict(
            title = "index",
            user = user,
            u_tasks = users_tasks,
            )
