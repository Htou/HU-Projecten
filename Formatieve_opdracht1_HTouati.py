import random
import math


# Opdracht 1 - Pyramide
def pyramid():
    lengte = int(input("Hoe hoog moet de pyramide worden? "))
    pyramid = ""

    for i in range(lengte):
        pyramid += "*"
        print(pyramid)
        if len(pyramid) == lengte + 1:
            break
    for i in range(lengte):
        pyramid = pyramid[1:]
        if len(pyramid) == 0:
            print("")
            break
        print(pyramid)


pyramid()


# Opdracht 2 - Tekstcheck
def tekstcheck():
    string1 = str(input("Geef de eerste string om te controleren: "))
    string2 = str(input("Geef de tweede string om te controleren: "))

    for (i, (a, b)) in enumerate(zip(string1, string2)):
        if a != b:
            print(f"het eerste verschil ontstaat bij index: {i}")
            print("")

# ---------------- werkt ook
#     for (i, x) in zip(enumerate(string1), enumerate(string2)):
#         if i != x:
#             print("Het eerste verschil ontstaat bij index: " + str(x[0]))
#             print("")

tekstcheck()


# Opdracht 3 - Lijstcheck
def lijstcheck():
    lst = [random.choice(range(10)) for i in range(50)]
    print(lst)

    x = int(input("Geef een getal (0-9) om te controleren hoe vaak deze in de lijst voorkomt: "))

    def count(x):
        duplicates = 0
        for i in lst:
            if i == x:
                duplicates += 1

        print("Het getal " + str(x) + " komt " + str(duplicates) + " maal voor")
        return duplicates

    count(x)
    print("")

    def verschil(r):
        for (i, j) in zip(r, r[1:]):
            print("het verschil tussen " + str(i) + " en " + str(j) + " is " + str(abs(i - j)))
        print("")

    verschil(lst)

    def checker1of0():
        if count(1) > count(0) and count(0) <= 12:
            print("De lijst is goedgekeurd")
        else:
            print("De lijst is niet goedgekeurd")

    print("")
    checker1of0()


# lijstcheck()


# opdracht 4 - reverse
def palingdroom():
    string = "palingdroom"
    print("".join(list(reversed(string))))

    print(string[::-1])

    reversedString = ""
    for i in string:
        reversedString = i + reversedString
    print(reversedString)
    print("")


palingdroom()


# opdracht 5 - sorteren
def sorteren():
    lst = [random.choice(range(10)) for i in range(50)]
    print(lst)

    for i in range(len(lst) - 1):
        for j in range(0, len(lst) - i - 1):
            if lst[j] > lst[j + 1]:
                lst[j], lst[j + 1] = lst[j + 1], lst[j]

            #swap(lst[j], lst[j + 1]) kan ook
    print(lst)
    print("")


sorteren()


# Opdracht 6 - Gemiddelde berekenen
def gemiddelde():
    lst = [random.choice(range(10)) for i in range(50)]
    print(lst)
    print("Het gemiddelde van de lijst is: " + str(sum(lst) / len(lst)))
    print("")

    lst = [[] for x in range(5)]
    print(lst)
    for i in range(5):
        for j in range(3):
            x = int(input(("Geef 3 getallen om verschillende lists in de list te maken: ")))
            lst[i].append(x)
        print(lst)
    newList = sum(lst, [])
    print(newList)
    print("")
    print("Het gemiddelde van de lijst is: " + str(sum(newList) / len(newList)))
    print("")


gemiddelde()

# opdracht 7 - random
def randomGuess():
    # a = 10
    # b = 0
    #
    # c = b / a
    # d = b % a
    #
    # nummer = (a * (nummer % c)) - (d * math.floor(nummer / c))
    # if nummer < 0:
    #     nummer = nummer + b
    # poging eigen nummer generator te maken

    nummer = random.choice(range(11))
    print(nummer)
    while True:
        x = int(input("raad het juiste nummer (0-10): "))
        if x == nummer:
            break
    print("je hebt het juiste nummer geraden")
    print("")


randomGuess()

# opdracht 8 - Compressie meer uitleg nodig
# def compressie:
# compressie()

# Opdracht 9 - Cyclisch verschuiven
def cyclish(ch, n):
    binary = ''.join(format(ord(i), 'b') for i in ch)
    print("Het binare nummer van " + str(ch) + " is: " + str(binary))
    binaryList = list(str(binary))
    if n > 0:
        for i in range(n):
            binaryList.append(binaryList.pop(0))
            print(binaryList)
        print("De binaire bits zijn " + str(n) + " maal naar links geshift: " + ''.join(binaryList))
        print("")
    else:
        for i in range(abs(n)):
            binaryList.insert(0, binaryList.pop(-1))
            print(binaryList)
        print("De binaire bits zijn " + str(abs(n)) + " maal naar rechts geshift: " + ''.join(binaryList))
        print("")

cyclish("a", 4)
cyclish("b", -4)


# Opdracht 10 - Fibonaci
def fibonaci(f):
    lst = []
    a, b = 0, 1
    for i in range(f):
        lst.append(a)
        a, b = b, a + b
    print(lst)
    print("De f" + str(f) + " is uitgrekend n" + str(lst[f - 1]))
    print("")


fibonaci(20)

# def fibonaci(n): prototype
#     lst = [0, 1]
#     a, b = lst[0], lst[1]
#     for i in range(n):
#         lst.append(a+b)
#         a = b
#         b = lst[i+2]
#     print(lst)

#
# fibonaci(20)


# Opdracht 11 - Caesarcijfer weet ik niet
# def ceasarcode():
#     tekst = input("Geef een tekst: ")
#     rotatie = int(input("Geef een rotatie: "))
#
#     letters = list(tekst)
#     encryptie = ""
#     print(letters)
#
#     ceasar = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
#               'v', 'w', 'x', 'y', 'z']
#
#     for i in letters:
#         if i in ceasar:
#
#
# ceasarcode()


# Opdracht 12 - FizzBuzz
def fizzbuzz():
    for i in range(1, 101):
        if (i % 3 == 0 and i % 5 != 0):
            print("Fizz")
        elif (i % 3 != 0 and i % 5 == 0):
            print("Buzz")
        elif i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz")
        else:
            print(i)


fizzbuzz()
