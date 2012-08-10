from datetime import datetime
import models as m


def get_user(request):
    """
    Get the user from the webauth username contained within the request

    :type request: Request
    :param request: The pyramid request object
    """
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


def get_assigned_tasks(user_id):
    """
    Return all assigned tasks

    :type user_id: int
    :param user_id: User's ID, used to filter tasks
    """

    tasks = m.Task.query.filter_by(assigned_id=user_id)
    return sorted(lambda t: t.id, tasks)


def get_recent_tasks():
    """
    Return <= 20 Tasks created today
    """
    now = datetime.now()
    todays = sorted(
                lambda t: t.id,
                filter(
                    lambda dt: (now - dt).days < 1,
                    m.Task.query.all()))
    if len(todays) > 20:
        todays = todays[:20]
    # Needs optimising
    return todays



