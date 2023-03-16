import shutil as sl


def getf(name):
    plist = name.split("/")
    return plist[len(plist) - 1]


def getfname(p):
    try:
        return getf(p).split('.')[0]
    except:
        return getf(p)

#TODO: make it in a loop
#while():



swit = int(input("- Choose a task \nDecompress = 1, Compress = 0 \n"))
print(f"received : {swit}")

if (swit == 1):
    # - Unzip : jpg -> zip -> result
    path = input("- Specify the jpg file path : \n")

    try:
        open(path, "rb").read()
        print(f"received : {path}")

        file = open(path, "rb").read().hex()
        new = ""
        try:
            new = "504b0304" + file.split("ffd9504b0304", 2)[1]
        except:
            print("Could not distinguish the separation point")

        uznm = getfname(path)

        open("./sample/" + uznm + ".zip", "wb").write(bytes.fromhex(new))  # bytes-like object is required, not 'str'
        print(f"DONE - Check '{uznm}.zip' in './sample'")

        exswit = int(input("Do you want to unzip it?\nYES = 1, No = 0\n"))

        if exswit == 1:
            sl.unpack_archive("./sample/" + uznm + ".zip", "./sample/output/" + uznm)
            print(f"DONE - Check the result in './sample/output/{uznm}'")
        elif exswit == 0:
            print("Exiting...")#dummy

    except:
        print("The path does not exist")

elif (swit == 0):
    # - Zip : target file -> zip -> jpg
    # jpg|jpeg|png|gif|webp
    zippath = input("- Specify the file/folder path : \n")
    #psw = 0

    sp = ""
    nsp = ""
    ssp = ""
    nzip = ""

    #- Probe
    if zippath.split("/").pop() == getfname(zippath): # folder case
        try:
            temp = os.listdir(zippath)
            print(f"received : {zippath}")
            #psw = 1

            sp = zippath.split("/")
            nsp = sp.pop()#폴더명
            ssp = "/".join(map(str, sp))

            nzip = "./sample/temp/" + nsp + ".zip"#최종 파일의 경로

            sl.make_archive("./sample/temp/" + nsp, "zip", ssp, nsp)

        except:
            print("The path does not exist")

    else: # file case
        try:
            open(zippath, "rb").read()
            print(f"received : {zippath}")
            #psw = 2

            sp = zippath.split("/")
            nsp = sp.pop()#파일명
            ssp = "/".join(map(str, sp))
            nzip = "./sample/temp/" + nsp.split(".")[0] + ".zip"

            sl.make_archive("./sample/temp/" + nsp.split(".", 2)[0], "zip", ssp, nsp)  # 파일인 경우
        except:
            print("The path does not exist")


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
