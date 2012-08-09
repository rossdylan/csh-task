from sqlalchemy import (
    Column,
    Integer,
    Unicode,
    ForeignKey,
    DateTime,
    )

from sqlalchemy.ext.declarative import declarative_base

from sqlalchemy.orm import (
    scoped_session,
    sessionmaker,
    relationship,
    backref,
    )

from zope.sqlalchemy import ZopeTransactionExtension

DBSession = scoped_session(sessionmaker(extension=ZopeTransactionExtension()))
Base = declarative_base()
Base.query = DBSession.query_property()


class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, unique=True, primary_key=True)
    username = Column(Unicode(128), unique=True)
    email = Column(Unicode(128), unique=True)
    created_tasks = relationship("Task",
        primaryjoin="User.id==Task.creator_id")
    assigned_tasks = relationship("Task",
        primaryjoin="User.id==Task.assigned_id")


def status_default(context):
    return 0


class Task(Base):
    __tablename__ = 'tasks'
    id = Column(Integer, unique=True, primary_key=True)
    title = Column(Unicode(128))
    description = Column(Unicode(128))
    body = Column(Unicode(128))
    status = Column(Integer, default=status_default)
    """
    Possible Statuses
    0: Unassigned
    1: assigned
    2: in progress
    3: closed
    4: can not replicate
    5: Not an issue
    """
    creator_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    assigned_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    created_at = Column(DateTime)


