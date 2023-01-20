#import


#var 정리
#var log = null;
#
#var imgPattern = /^.*\.(?:jpg|jpeg|png|gif|webp)$/i;

#swit = input("Choose a task \nzip = 0, unzip = 1 \n")
#print(f"received : {swit}")

path = input("Specify the file path : \n")
print(f"received : {path}")

file = open(path,"rb").read().hex()

print(file)



"""

if(swit==1):#unzip
    # - Path
    path = input("Specify the file path : \n")
    print(f"received : {path}")

    file = open(path,"rb").read().hex()

    #print(file)





elif(swit==0):#zip
    # - Path
    path = input("Specify the file path : \n")
    print(f"received : {path}")



"""



#def upzip():









