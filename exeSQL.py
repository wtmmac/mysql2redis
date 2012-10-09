#!/usr/bin/python
from exeCommand import  exe 
mysql="mysql -ugame_user -p123456 -h 192.168.1.110 -e "
def SQL(sql):
    result=exe(mysql +"'use Game_Boss;"+ sql+"'")
    result= result[0:-1];
    return result


#test
if(__name__ == "__main__"):
    result=SQL("select  SinaNickName, AccountName,TotalMoney,ALevel , Experience,TotalSumMoney,Avatar,PlayMap  from USetting ,UAccount ,UDetail where USetting.AccountID = UAccount.AccountID And UDetail.AccountID=UAccount.AccountID And UAccount.AccountID=1");
    print "title",result[0]
    for i in range(1,len(result)):
            print "%d :%s"%(i,result[i])
