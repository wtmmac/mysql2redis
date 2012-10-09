debug=False

from Object import Object

class Location(Object):
    def __init__(self):
        self.sql="""
        select B.CityCode,B.PositionCode,B.MaxCar,B.MaxPeople,A.ShopID,A.Owner from GShopStore A LEFT JOIN CCityPositionRef B ON A.CRefID=B.CRefID 
        """
    def write2Redis(self):
        self.getDataFromDB()
        indexOfOwner = -1
        indexOfShopID= -1

        for i in range(len(self.head)):
            if(self.head[i]=="Owner"):
                indexOfOwner=i
                break
        if(indexOfOwner == -1):
            return False

        for i in range(len(self.head)):
            if(self.head[i]=="ShopID"):
                indexOfShopID=i
                break
        if(indexOfShopID == -1):
            return False

        for iLine in self.results:
            objID="player:"+str(iLine[indexOfOwner])
            objID=objID+":store:"+str(iLine[indexOfShopID])

            command="hMSet "+objID+" "
            for i in range(len(self.head)):
                tem=""
                if(self.head[i]=="MaxCar" or self.head[i] =="MaxPeople"):
                    tem="'"+str(iLine[i])+"' "
                else:
                    tem=str(iLine[i])+" "

                command = command + self.head[i] +" "+ tem 
            from exeRedis import Redis
            redis = Redis()
            redis.exe(command)
            if(debug):
                print command
                print "===================================================="
        return True 

#Test
if(__name__=="__main__"):
    test=Location()
    print test.write2Redis()
