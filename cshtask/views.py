from pyramid.view import view_config
from datetime import datetime
import models as m


def get_user(request):
    username = request.headers.get('X-Webauth-USER', None)
    if username == None:
        raise Exception("OH GOD (no webauth username found)")
    else:
        try:
            user = m.User.query.filter_by(username=username).one()
            return user
        except:
            new_user = m.User(
                    username=username,
                    email="{0}@csh.rit.edu".format(username),
                    )
            m.DBSession.add(new_user)
            return new_user


def get_recent_tasks():
    now = datetime.now()
    todays = filter(lambda dt: (now - dt).days < 1, m.Task.query.all())
    # Needs optimising
    return todays


@view_config(route_name='index', renderer='index.mak')
def index_view(request):
    user = get_user(request)
    recent_tasks = get_recent_tasks()
    return dict(
            title = "index",
            username = user.username,
            r_tasks = recent_tasks,
            )
