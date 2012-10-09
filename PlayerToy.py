from Object import Object
debug= False
class PlayerToy(Object):
    def __init__(self):
        self.name1= "player:"
        self.name2= "playertoy:"
        self.primarykey1="AccountID"
        self.primarykey2="CardCode"
        self.sql="select * from RPlayerPropsCard A join GPropsCard B on A.CardCode=B.CardCode;"
 
    def write2Redis(self):
        self.getDataFromDB()
        index1=-1
        index2=-1
        for i in range(len(self.head)):
            if(self.head[i] == self.primarykey1):
                index1= i
                break
        for i in range(len(self.head)):
            if(self.head[i] == self.primarykey2):
                index2=i
                break
        if(index1== -1):
            return
        if(index2== -1):
            return
        for iLine in self.results:
            objID1=self.name1+str(iLine[index1])
            objID2=self.name2+str(iLine[index2])
            command="hmset "+objID1+objID2+" "
            for i in range( len(self.head) ):
                command = command + self.head[i]+" "+str(iLine[i])+" "
            if(debug):
                print command
            from exeRedis import Redis
            redis = Redis()
            redis.exe(command)
        return True 
 
#Test
if(__name__=="__main__"):
    t=PlayerToy()
    t.write2Redis()
