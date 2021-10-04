import zipfile, itertools, sys

"""Character set is created."""
charset = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz ~`!@#$%^&*()-_=+[{]}\|;:'\"/?.>,<"
minRep = 1
maxRep = 5

"""It generates the passwords."""
def genPassword(zfile):
    back = '.' + zfile +'.data'
    for x in range(minRep, maxRep + 1):
        f = open(back,mode='w')
        f.write(str(x))
        f.close()
        print('Trying passwords of length %d' %x)
        for l in itertools.product(charset,repeat = x):
            yield ''.join(l)

"""extract all the files from the zip"""
def extract(zfile,password):
    try:
        zf = zipfile.ZipFile(zfile)
        files = zf.infolist()
        zf.read(files[0],pwd = password)
        zf.close()
        return True
    except KeyboardInterrupt:
        exit(0)
    except:
        return False

"""Function for bruteforce attack."""
def bruteforce(zfile):
    back = zfile
    password = ''
    try:
        f = open(back,'rb')
        data = f.readline().strip()
        print(data)
        if 'pwd' == data[:3]:
            password = data[4:]
            return password
        else:
            global minRep
            minRep = int(data)
        f.close()
    except:
        pass
    try:
        zf = zipfile.ZipFile(zfile)
        files = zf.infolist()
        data = zf.read(files[0],pwd = password)
        zf.close()
        flag = True
    except KeyboardInterrupt:
        exit(0)
    except:
        flag = False
    if not flag:
        for i in genPassword(zfile):
            try:
                flag = extract(zfile, i)
                if flag:
                    password = i
                    break
            except KeyboardInterrupt:
                exit(0)
    if not flag:
        print('Password Not Found!!!')
        exit(0)
    f = open(back,'w')
    f.write('pwd:' + password)
    f.close()
    return password
    
"""Function for dictionary attack."""
def dictionary(zfile, dic):
    back = '.' + zfile +'.data'
    password = ''
    try:
        f = open(back,'r')
        data = f.readline().strip()
        if 'pwd' == data[:3]:
            password = data[4:]
            return password
        else:
            start = int(data)
        f.close()
    except:
        start = 1
    dictionaryFile = open(dic,'r')
    try:
        zf = zipfile.ZipFile(zfile)
        files = zf.infolist()
        data = zf.read(files[0],pwd = password)
        zf.close()
        flag = True
    except KeyboardInterrupt:
        exit(0)
    except:
        flag = False
    if not flag:
        dlist = dictionaryFile.readlines()
        for i in range(start,len(dlist)):
            try:
                flag = extract(zfile, dlist[i])
                if flag:
                    password = dlist[i]
                    break
            except KeyboardInterrupt:
                exit(0)
    if not flag:
        print('Password Not Found!!!')
        exit(0)
    f = open(back,'w')
    f.write('pwd:' + password)
    f.close()
    return password


if __name__ == '__main__':
    arg = sys.argv[1:]
    if(len(arg) == 0 or arg[0] == '-h' or arg[0] == '--h' or arg[0] == '-help'):
        print("usage script.py filename [-b | -ab charset=charset | -m=[2,5] | -d file=dictionary.txt]")
        print("option:")
        print("-b\t\t\t:Bruteforce attack.")
        print("-ab -file=charset\t:Advance Bruteforce attack from the given charset.")
        print("-d file=dict.txt\t:Dictionary attack. Provide dictionary name in present working directory")
        print("-m=[min, max]\t\t:Minimum and Maximum length of passwords to be consider.")
        exit(0)
    elif arg[1] == '-b':
        print('Processing...')
        if len(arg) > 2:
            length = arg[2].split('=')[1].split(',')
            minRep = int(length[0][1:])
            maxRep = int(length[1][:-1])
        password = bruteforce(arg[0])
    elif arg[1] == '-ab':
        print('Processing...')
        if len(arg) > 3:
            length = arg[3].split('=')[1].split(',')
            minRep = int(length[0][1:])
            maxRep = int(length[1][:-1])
        try:
            charset = arg[2].split('=')[1]
        except:
            print("usage script.py filename [-b | -ab charset=charset | -m=[2,5] | -d file=dictionary.txt]")
            print("option:")
            print("-b\t\t\t:Bruteforce attack.")
            print("-ab -file=charset\t:Advance Bruteforce attack from the given charset.")
            print("-d file=dict.txt\t:Dictionary attack. Provide dictionary name in present working directory")
            print("-m=[min, max]\t\t:Minimum and Maximum length of passwords to be consider.")
            exit(0)
        password = bruteforce(arg[0])
    elif arg[1] == '-d':
        print('Processing...')
        fl = arg[2].split('=')[1]
        password = dictionary(arg[0],fl)
    else:
        print("Invalid input")
        print("usage script.py filename [-b | -ab charset=charset | -m=[2,5] | -d file=dictionary.txt]")
        print("option:")
        print ("-b\t\t\t:Bruteforce attack.")
        print ("-ab -file=charset\t:Advance Bruteforce attack from the given charset.")
        print ("-d file=dict.txt\t:Dictionary attack. Provide dictionary name in present working directory")
        print ("-m=[min, max]\t\t:Minimum and Maximum length of passwords to be consider.")
        exit(0)
    print('Password is "%s" without quotes.' %password)