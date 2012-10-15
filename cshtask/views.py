from pyramid.view import view_config
import util


@view_config(route_name = 'index', renderer = 'index.mak')
def index_view(request):
    """
    View for the index page

    :type request: Request
    :param request: The pyramid request object
    """

    user = util.get_user(request)
    users_tasks = util.get_assigned_tasks(user.id)
    return dict(
            title = "index",
            user = user,
            u_tasks = users_tasks,)

@view_config(route_name = 'tasks_specific', renderer = 'task.mak')
def task_view(request):
    """
    View for a single task

    :type request: Request
    :param request: The pyramid request object
    """

    user = util.get_user(request)
    return dict(
            title = 'tasks',
            user = user)

@view_config(route_name = 'tasks', renderer = 'tasks.mak')
def tasks(request):
    """
    View for all tasks

    :type request: Request
    :param request: The pyramid request object
    """

    user = util.get_user(request)
    return dict(
            title = 'tasks',
            user = user)
