from sqlalchemy import Column, String, create_engine,INTEGER,TEXT,DateTime
from sqlalchemy.orm import sessionmaker,relationship
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import ForeignKey


Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    __table_args__ = {
        "mysql_charset": "utf8"
    }
    id = Column(INTEGER, primary_key=True,autoincrement=True)
    # herf=Column(TEXT)
    discord_name=Column(String(127))
    discord_id=Column(String(127))
    wechat_name=Column(String(127))
    wechat_id  =Column(String(127))
    #皮币
    p_coin=Column(INTEGER,default=0)
    #皮皮亲密度
    p_value=Column(INTEGER,default=10)

    mentions = relationship("MentionPiTable", backref="user")
    pCoinLogs = relationship("PiCoinLog", backref="user")
    comments= relationship("Comments", backref="user")

class MentionPiTable(Base):
    __tablename__ = 'mention_pi_table'
    __table_args__ = {
        "mysql_charset": "utf8"
    }
    id = Column(INTEGER, primary_key=True, autoincrement=True)
    # href = Column(TEXT)
    user_id=Column(INTEGER, ForeignKey('user.id'))
    mention_time=Column(DateTime)
    trigger_word=Column(String(127))

class PiCoinLog(Base):
    __tablename__ = 'pi_coin_log'
    __table_args__ = {
        "mysql_charset": "utf8"
    }
    id = Column(INTEGER, primary_key=True, autoincrement=True)
    user_id = Column(INTEGER, ForeignKey('user.id'))
    p_coin_change = Column(INTEGER, default=0)
    time = Column(DateTime)
    note = Column(String(127))


class Comments(Base):
    __tablename__ = 'comments'
    __table_args__ = {
        "mysql_charset": "utf8"
    }
    id = Column(INTEGER, primary_key=True, autoincrement=True)
    user_id = Column(INTEGER, ForeignKey('user.id'))
    content = Column(TEXT)
    time = Column(DateTime)




def readFile(filename):
    filehandle = open(filename)
    S= (filehandle.read())
    filehandle.close()
    return S

if __name__ == '__main__':
    sqlLine=readFile("../../Config/sqlconfig")
    engine=create_engine(sqlLine, encoding='utf-8',echo=True)
    DBSession = sessionmaker(bind=engine)
    Base.metadata.create_all(engine)