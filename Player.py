from Object import Object
debug= False
class Player(Object):
    def __init__(self):
        self.name = "player:"
        self.sql="select UAccount.AccountID as AccountID,  SinaNickName, AccountName,TotalMoney,ALevel , Experience,TotalSumMoney,Avatar,PlayMap  from USetting ,UAccount ,UDetail where USetting.AccountID = UAccount.AccountID And UDetail.AccountID=UAccount.AccountID"
 
    def write2Redis(self):
        self.getDataFromDB()
        index = -1
        for i in range(len(self.head)):
            if(self.head[i] == "AccountID") :
                index = i
                break
        if(index == -1):
            return False
        for iLine in self.results:
            objID=self.name+str(iLine[index])
            command="hMSet "+objID+" "
            for i in range(len(self.head)):
                command = command + self.head[i] +" " +str(iLine[i])+" "
            if(debug):
               print command
            from exeRedis import Redis
            redis = Redis()
            redis.exe(command)
        return True 
 
#Test
if(__name__=="__main__"):
    t=Player()
    t.write2Redis()
