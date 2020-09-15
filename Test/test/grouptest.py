import  itchat

itchat.auto_login(hotReload=True)
mpsList=itchat.get_chatrooms(update=True)[1:]
total=0
for it in mpsList:
    print(it['NickName'])
    total=total+1
print(total)

itchat.dump_login_status()

memberList = itchat.update_chatroom(mpsList[1].UserName)

mlist = memberList['MemberList']
for it in mlist:
    print(it['NickName']+':'+it['DisplayName'])