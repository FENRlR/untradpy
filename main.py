import shutil as sl


def getf(name):
    plist = name.split("/")
    return plist[len(plist) - 1]


def getfname(p):
    return getf(p).split('.')[0]


swit = int(input("- Choose a task \nDecompress = 1, Compress = 0 \n"))
print(f"received : {swit}")

if (swit == 1):
    # - Unzip : jpg -> zip -> result
    path = input("- Specify the jpg file path : \n")

    try:
        open(path, "rb").read()
        print(f"received : {path}")
    except:
        print("The path does not exist")

    file = open(path, "rb").read().hex()
    new = "504b0304" + file.split("ffd9504b0304", 2)[1]  # TODO : error handling
    uznm = getfname(path)

    open("./sample/" + uznm + ".zip", "wb").write(bytes.fromhex(new))  # bytes-like object is required, not 'str'
    print(f"DONE - Check '{uznm}.zip' in './sample'")

    exswit = int(input("Do you want to unzip it?\nYES = 1, No = 0\n"))

    while(exswit != 1  or exswit != 0 ):
        if exswit == 1:
            sl.unpack_archive("./sample/" + uznm + ".zip", "./sample/output/" + uznm)
            print(f"DONE - Check the result in './sample/output/{uznm}'")
        elif exswit == 0:
            break
        else:
            continue

elif (swit == 0):
    # - Zip : file -> zip -> jpg
    # jpg|jpeg|png|gif|webp
    zippath = input("- Specify the file path : \n")

    try:
        open(zippath, "rb").read()
        print(f"received : {zippath}")
    except:
        print("The path does not exist")

    sp = zippath.split("/")
    nsp = sp.pop()
    ssp = "/".join(map(str, sp))
    nzip = "./sample/temp/" + nsp.split(".")[0] + ".zip"

    sl.make_archive("./sample/temp/" + nsp.split(".")[0], "zip", ssp, nsp)

    imgpath = input("- Specify the jpg file path : \n")
    try:
        open(imgpath, "rb").read()
        print(f"received : {imgpath}")
    except:
        imgpath = "./default.jpg"
        print("Image not found - proceed with default image")

    new = open(imgpath, "rb").read().hex() + open(nzip, "rb").read().hex()
    znm = getfname(zippath)
    open("./sample/" + znm + ".jpg", "wb").write(bytes.fromhex(new))
    try:
        sl.rmtree("./sample/temp/")
    except:
        pass

    print(f"DONE - Check '{znm}.jpg' in './sample'")
