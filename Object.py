from exeSQL import SQL
#debug=True
debug=False

class Object:
    def __init__(self,primaryKey):
        self.head=[]
        self.results=[]
        self.sql="show databases"

    def getDataFromDB(self):
        self.head=[]
        self.results=[]
        lines=SQL(self.sql).split("\n")

        self.head=lines[0].split("\t");

        for i in range(1,len(lines)) :# the results of i line.i begin from 1
            iLine=lines[i].split("\t")
            if(debug):
                print "iLine:", iLine
            line=[]
            for word in iLine:#if the word is a null string ,replace it as ''
                if(word.strip() == ""):
                    word="''"
                line.append(word)
            if(debug):
                print "line:",line
            self.results.append( line )
    

