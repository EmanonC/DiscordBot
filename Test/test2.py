def readFile(filename):
    filehandle = open(filename)
    S= (filehandle.readlines())
    filehandle.close()
    return S

s=readFile("goodbyeWords")
print(s)