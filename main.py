import shutil as sl


swit = input("Choose a task \nzip = 0, unzip = 1 \n")
print(f"received : {swit}")

#"""

if(swit==1):#unzip
    # - Path
    path = input("Specify the file path : \n")
    print(f"received : {path}")

    file = open(path, "rb").read().hex()
    new = "504b0304" + file.split("ffd9504b0304", 2)[1]
    result = open("./sample/result.zip", "wb").write(bytes.fromhex(new))  # bytes-like object is required, not 'str'
    sl.unpack_archive("./sample/result.zip", "./sample/output")

elif(swit==0):#zip
    # - Path
    imgpath = input("Specify img file path : \n")
    print(f"received : {imgpath}")

    zippath = input("Specify zip file path : \n")
    print(f"received : {zippath}")

    new = open(imgpath, "rb").read().hex() + open(zippath, "rb").read().hex()

    result = open("./sample/zipresult.jpg", "wb").write(bytes.fromhex(new))

#"""








