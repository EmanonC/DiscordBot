from sqlalchemy import Column, String, create_engine,INTEGER,DateTime
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sql.models import *
from sql.tool import readFile
import datetime

class sql_helper:
    def __init__(self):
        self.db=declarative_base()
        sqlLine = readFile("../../Config/sqlconfig")
        # self.engine = create_engine(sqlLine, encoding='utf-8')
        self.engine = create_engine(sqlLine, encoding='utf-8', echo=True)
        self.DBSession = sessionmaker(bind=self.engine)
        self.db=self.DBSession()

    def addDiscordUser(self,discord_id,discord_name):
        user=User(discord_name=discord_name,discord_id=discord_id)
        self.db.add(user)
        self.db.commit()

    def addCommentfroDiscord(self,discord_id,content,time):
        users = self.db.query(User).filter(User.discord_id ==discord_id).all()
        user=users[0]
        comment=Comments(user_id=user.id,content=content,time=time)
        self.db.add(comment)
        self.db.commit()

    def getAllComments(self):
        comments=self.db.query(Comments).all()
        # for comment in comments:
        #     print(comment.time.timestamp())


    # def add_Indeed_Job_herf(self,herf,job_type=None):
    #     IndeedJob=IndeedJobTable(herf=herf,job_type=job_type)
    #     self.db.add(IndeedJob)
    #     self.db.commit()
    #
    # def add_Job_Description(self,href,job_name,company_name,requirements):
    #     JD=JobDescibtion(href=href,job_name=job_name,company_name=company_name)
    #     self.db.add(JD)
    #     self.db.flush()
    #     jid=JD.id
    #     self.db.commit()
    #     for r in requirements:
    #         JRD=JobRequirementDescibtion(job_id=jid,requirement=r)
    #         self.db.add(JRD)
    #         self.db.commit()
    #
    # def set_indeed_job_is_scrp(self,indeed_job):
    #     indeed_job.is_scrp=1
    #     self.db.commit()
    #
    # def get_indeed_jobs(self):
    #     job_hrefs=self.db.query(IndeedJobTable).filter(IndeedJobTable.is_scrp==0).all()
    #     return job_hrefs

helper=sql_helper()
# helper.addDiscordUser("112","pixia")
# helper.addCommentfroDiscord("112","ooo",time=datetime.datetime.now())
helper.getAllComments()