from sqlalchemy import (
    Column,
    Index,
    Integer,
    Text,
    )

from sqlalchemy.ext.declarative import declarative_base

from sqlalchemy.orm import (
    scoped_session,
    sessionmaker,
    )

from zope.sqlalchemy import ZopeTransactionExtension

DBSession = scoped_session(sessionmaker(extension=ZopeTransactionExtension()))
Base = declarative_base()


class Hint(Base):
    __tablename__ = 'hints'
    id = Column(Integer, primary_key=True)
    question = Column(Text)
    answer = Column(Text)

    def __init__(self, question, answer):
        self.question = question
        self.answer = answer

Index('idx_hint_id', Hint.id, unique=True)
