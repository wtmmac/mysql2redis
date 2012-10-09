from Object import Object
debug= False
class Employee(Object):
    def __init__(self):
        self.name1= "player:"
        self.name2= "store:"
        self.name3= "employee:"
        self.primarykey1="RoleID"  
        self.primarykey2="ShopID"
        self.primarykey3="SNID"
        self.sql="select ShopID,SNID,Rank,Proficiency,Salary,EmployFee as Fee,Gender,SeqID as RoleID,  NpcName as RoleName, Patience as Tired from RShopNPC,GNpc where GNpc.NpcCode=RShopNPC.NpcCode;"
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
        if(index1== -1):
            return
        if(index2== -1):
            return
        for iLine in self.results:
            objID1=self.name1+str(iLine[index1])
            objID2=self.name2+str(iLine[index2])
            objID3=self.name3+str(iLine[index3])
            command="hmset "+objID1+objID2+objID2+" "
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
    t=Employee()
    t.write2Redis()
