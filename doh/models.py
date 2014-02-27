from sqlalchemy import (
    Column,
    Index,
    Integer,
    Text,
    Binary,
    )

from sqlalchemy.ext.declarative import declarative_base

from sqlalchemy.orm import (
    scoped_session,
    sessionmaker,
    )

from zope.sqlalchemy import ZopeTransactionExtension

DBSession = scoped_session(sessionmaker(extension=ZopeTransactionExtension()))
Base = declarative_base()


class Tip(Base):
    __tablename__ = 'tips'
    id = Column(Integer, primary_key=True)
    title = Column(Text)
    title_image = Column(Text)
    answer = Column(Text)
    answer_image = Column(Text)

    def __init__(self, title, title_image, answer, answer_image):
        self.title = title
        self.title_image = title_image
        self.answer = answer
        self.answer_image = answer_image

Index('idx_tips_id', Tip.id, unique=True)



class Visit(Base):
    __tablename__ = 'visits'
    id = Column(Integer, primary_key=True)
    session = Column(Text)
    tip_id = Column(Integer)

    def __init__(self, session, tip_id):
        self.session = session
        self.tip_id = tip_id

Index('idx_visits_id', Visit.id, unique=True)
