def generateCode():
    global gCode
    gCode = random.choices(kleuren, k=4)
    print(gCode)

generateCode()

