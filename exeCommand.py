from os import popen

def exe(comd):
    return popen(comd).read();

#test
if(__name__ =="__main__"):
    print exe("echo hello"),
