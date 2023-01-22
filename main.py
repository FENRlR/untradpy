import shutil as sl


def getf(name):
    plist = name.split("/")
    return plist[len(plist) - 1]


def getfname(p):
    return getf(p).split('.')[0]


swit = int(input("- Choose a task \nDecompress = 1, Compress = 0 \n"))
print(f"received : {swit}")

if (swit == 1):
    # - Unzip : jpg to zip result
    path = input("- Specify the jpg file path : \n")
    if open(path, "rb").read() == null:
        print("The path does not exist")
    else:
        print(f"received : {path}")

    file = open(path, "rb").read().hex()
    new = "504b0304" + file.split("ffd9504b0304", 2)[1]  # TODO : error handling
    uznm = getfname(path)
    open("./sample/" + uznm + ".zip", "wb").write(bytes.fromhex(new))  # bytes-like object is required, not 'str'
    print(f"DONE - Check '{uznm}.zip' in './sample'")

    exswit = int(input("Do you want to unzip it?\nYES = 1, No = 0\n"))
    if exswit == 1:
        sl.unpack_archive("./sample/" + uznm + ".zip", "./sample/output/" + uznm)
        print(f"DONE - Check the result in './sample/output/{uznm}'")

elif (swit == 0):
    # - Zip : zip to jpg
    zippath = input("Specify zip file path : \n")

    if open(zippath, "rb").read() == null:
        print("The path does not exist")
    else:
        print(f"received : {zippath}")

    imgpath = input("- Specify the jpg file path : \n")
    if imgpath == null or open(imgpath, "rb").read() == null:
        imgpath = "./default.jpg"
        print("Image not found - proceed with default image")
    else:
        print(f"received : {imgpath}")

    new = open(imgpath, "rb").read().hex() + open(zippath, "rb").read().hex()
    znm = getfname(zippath)
    open("./sample/" + znm + ".jpg", "wb").write(bytes.fromhex(new))
    print(f"DONE - Check '{znm}.jpg' in './sample'")
