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
    pValueLogs = relationship("PiValueLog", backref="user")
    comments= relationship("Comments", backref="user")
    pLogs=relationship("PiLog",backref="user")
    pFoods=relationship("PiFood",backref="user")

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

class PiValueLog(Base):
    __tablename__ = 'pi_value_log'
    __table_args__ = {
        "mysql_charset": "utf8"
    }
    id = Column(INTEGER, primary_key=True, autoincrement=True)
    user_id = Column(INTEGER, ForeignKey('user.id'))
    p_value_change = Column(INTEGER, default=0)
    time = Column(DateTime)
    remark = Column(String(127))

class PiLog(Base):
    __tablename__ = 'pi_log'
    __table_args__ = {
        "mysql_charset": "utf8"
    }
    id = Column(INTEGER, primary_key=True, autoincrement=True)
    user_id = Column(INTEGER, ForeignKey('user.id'))
    action=Column(String(127))
    time = Column(DateTime)
    remark = Column(String(127))


class PiFood(Base):
    __tablename__ = 'pi_food'
    __table_args__ = {
        "mysql_charset": "utf8"
    }
    id = Column(INTEGER, primary_key=True, autoincrement=True)
    user_id = Column(INTEGER, ForeignKey('user.id'))
    food_name = Column(String(127))
    time = Column(DateTime)
    eat_time = Column(DateTime)
    remark = Column(String(127))
    has_eat=Column(INTEGER)


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
    engine=create_engine(sqlLine, encoding='utf-8')
    DBSession = sessionmaker(bind=engine)
    Base.metadata.create_all(engine)