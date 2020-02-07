# Opdracht 1 - Pyramide
# def pyramid():
#     lengte = int(input("Hoe hoog moet de pyramide worden? "))
#     pyramid = ""
#
#     for i in range(lengte):
#         pyramid += "*"
#         print(pyramid)
#         if len(pyramid) == lengte + 1:
#             break
#     for i in range(lengte):
#         pyramid = pyramid[1:]
#         if len(pyramid) == 0:
#             print("")
#             break
#         print(pyramid)
#

# pyramid()


# Opdracht 2 - Tekstcheck
# def tekstcheck():
#     string1 = str(input("Geef de eerste string om te controleren: "))
#     string2 = str(input("Geef de tweede string om te controleren: "))
#
#     for (i, (a, b)) in enumerate(zip(string1, string2)):
#         if a != b:
#             print(f"het eerste verschil ontstaat bij index: {i}")
#             print("")

# ---------------- werkt ook
#     for (i, x) in zip(enumerate(string1), enumerate(string2)):
#         if i != x:
#             print("Het eerste verschil ontstaat bij index: " + str(x[0]))
#             print("")

# tekstcheck()


# Opdracht 3 - Lijstcheck
# def lijstcheck():
#     import random
#     r = [random.choice(range(10)) for i in range(50)]
#     print(r)
#
#     x = int(input("Geef een getal (0-9) om te controleren hoe vaak deze in de lijst voorkomt: "))
#
#     def count(x):
#         duplicates = 0
#         for i in r:
#             if i == x:
#                 duplicates += 1
#
#         print("Het getal " + str(x) + " komt " + str(duplicates) + " maal voor")
#         return duplicates
#
#     count(x)
#     print("")
#
#     def verschil(r):
#         for (i, j) in zip(r, r[1:]):
#             print("het verschil tussen " + str(i) + " en " + str(j) + " is " + str(abs(i - j)))
#         print("")
#
#     verschil(r)
#
#     def checker1of0():
#         if count(1) > count(0) and count(0) <= 12:
#             print("De lijst is goedgekeurd")
#         else:
#             print("De lijst is niet goedgekeurd")
#
#     print("")
#     checker1of0()
#
#
# lijstcheck()


# opdracht4
# def palingdroom():
#     string = "palingdroom"
#     print("".join(list(reversed(string))))
#
#     print(string[::-1])
#
#     reversedString = ""
#     for i in string:
#         reversedString = i + reversedString
#     print(reversedString)
#     print("")
#
#
# palingdroom()


#opdracht 5
def sorteren():
    import random
    r = [random.choice(range(10)) for i in range(50)]
    print(r)

    newList = []
    for i in r:

s
sorteren()
