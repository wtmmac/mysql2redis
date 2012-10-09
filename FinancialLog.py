from Object import Object
debug= False
class FinancialLog(Object):
    def __init__(self):
        self.name1= "player:"    
        self.name2= "store:"
        self.name3= "financiallog:"
        self.primarykey1="Owner"   #PlayerID
        self.primarykey2="ShopID"
        self.primarykey3="SAID"
        self.sql="select * from GShopStore,RShopFinancial where GShopStore.ShopID=RShopFinancial.ShopID;"
    def write2Redis(self):
        self.getDataFromDB()
        index1=-1
        index2=-1
        index3=-1
        for i in range(len(self.head)):
            if(self.head[i] == self.primarykey1):
                index1=i
                break
        for i in range(len(self.head)):
            if(self.head[i]==self.primarykey2):
                index2=i
                break
        for i in range(len(self.head)):
            if(self.head[i]==self.primarykey3):
                index3=i
                break
        if(index1==-1):
            return
        if(index2==-1):
            return
        if(index3==-1):
            return
        for iLine in self.results:
            objID1=self.name1+str(iLine[index1])
            objID2=self.name2+str(iLine[index2])
            objID3=self.name3+str(iLine[index3])
            command="hmset "+objID1+objID2+objID3+" "
            for i in range( len(self.head) ):
                command = command + self.head[i]+" "+str(iLine[i])+" "
            if(debug):
                print command
            from exeRedis import Redis
            redis=Redis()
            redis.exe(command)
        return True 
 
#Test
if(__name__=="__main__"):
    t=FinancialLog()
    t.write2Redis()
