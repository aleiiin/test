glist = []
count = int(input())
for i in range(count):
    glist.append(input())
for elem in glist:
    if 'лук' in elem:
        continue
    elif elem != glist[count - 1]:
        print(elem, end=', ')
if 'лук' not in elem:
    print(elem)

