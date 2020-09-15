from pipicheck import PiPiChecker
from pipiTimmer import *
from BulletinBoard import *
import BulletinBoardSQL
import re



class PipiBot:

    def __init__(self,isDiscord):
        self.bboardsql = BulletinBoardSQL.BulletinBoardSQL()
        self.isDiscord=isDiscord

    def phraseString(self,s,userName,uid):
        backTexts=[]
        if self.isStartWith("!pipimeal",s):
            pptimmer = PiPiTimmer()
            backTexts.append(pptimmer.getNextMealTime())

        if self.isStartWith("!comment",s):
            if self.isDiscord:
                pass
            else:
                content = s
                content = content.replace("!comment", "", 1)
                content = content.strip()
                ref=self.bboardsql.addCommentFromWeChat(userName,content)
                backTexts.append(ref)
            # UID=uid
            # self.bboard.addComment(UID, userName, content)
            # backTexts.append(f"留言成功！现在已经有{self.bboard.index}条留言了 \n"+"想看看别人的留言吗？试试 \"!read 数字\" \n"+"ex: !read 3 会随机朗读3条留言")


        if self.isStartWith("!pipiwyy", s):
            pptimmer = PiPiTimmer()
            backTexts.append(pptimmer.getTime(datetime.datetime.now())+"\n"+pptimmer.getWYY())

        if self.isStartWith("!misspipi", s):
            back=""
            back+=PiPiTimmer().getTime(datetime.datetime.now())+"\n"
            back+=PiPiTimmer().getSaoHua()+"\n"
            back+=f"有什么想留言的吗？请以 \"comment+留言\" 格式留言，现在已经有{self.bboardsql.getCommentsN()}条留言了"+"\n"
            back+="ex: !comment 皮皮虾再见！"
            backTexts.append(back)

        if self.isStartWith("!read", s):
            num = re.findall(r"\d+", s)
            if (len(num) > 0):
                num = int(num[0])
            else:
                num = 1

            backTexts.append(self.bboardsql.readSomeComments(num))

        return backTexts

    def isStartWith(self,s,text):
        if (len(s)>len(text)):
            return False

        return s==text[:len(s)]

