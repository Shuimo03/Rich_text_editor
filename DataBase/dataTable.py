from DataBase.database_config import the_engine
from sqlalchemy.ext.declarative import  declarative_base
from sqlalchemy import Column, INT,VARCHAR, TIMESTAMP
from sqlalchemy.orm import sessionmaker

Base = declarative_base()
class Text(Base):
    __tablename__ = 'notice'
    ID = Column(INT,primary_key=True)
    Content = Column(VARCHAR(500),default=None)
    DataCreateTime = Column(TIMESTAMP)
    EndShowDate = Column(TIMESTAMP)


def __init__(self, ID,Content,DataCreateime,EndShowDate):
    self.ID = ID
    self.Content = Content
    self.DataCreateime = DataCreateime
    self.EndShowDate = EndShowDate
#Base.metadata.create_all(the_engine)
DBSsession = sessionmaker(bind=the_engine)
session = DBSsession()