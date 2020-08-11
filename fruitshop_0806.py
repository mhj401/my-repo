source = "a,1,b,1,c,1,d,1,a,1,c,1"
temp_list = source.split(",")
data = []
length = len(temp_list)

for i in range(length):
    sub_list = []
    if i%2 == 1:
        sub_list.append(temp_list[i-1])
        sub_list.append(int(temp_list[i]))
        data.append(sub_list)

print(data)

data2 = []

for i in range(len(data)):
    is_dupl = False

    for j in range(len(data2)):
        if data2[j][0] == data[i][0]:
            is_dupl = True
            break
    if is_dupl:
        sum = data[i][1] + data2[j][1]
        data2[j][1] = sum

    else:
        data2.append(data[i])

print(data2)

