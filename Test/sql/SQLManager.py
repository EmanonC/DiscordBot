from sqlalchemy import Column, String, create_engine,INTEGER
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sql.models import *


class sql_helper:
    def __init__(self):
        self.db=declarative_base()
        sqlLine = self.readFile("../../Config/sqlconfig")
        self.engine=create_engine(sqlLine, encoding='utf-8',echo=True)
        self.DBSession = sessionmaker(bind=self.engine)
        self.db=self.DBSession()

    def readFile(self,filename):
        filehandle = open(filename)
        S = (filehandle.read())
        filehandle.close()
        return S