def fileToList(file):
    f = open(file, "r")
    lst = list()
    for x in f:
        lst.append(x)

    f.close()
    return lst

lst1 = fileToList("eval_payload.txt")
for a in lst1:
    print(a)
