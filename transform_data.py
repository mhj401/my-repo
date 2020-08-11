# 전달받은 파일을 읽어 2차원 리스트로 만든다

# 입력은 파일이름
# 출력은 2차원 리스트 [['a',1],['b',1]]


def transform_data(param):
    data_list = []
    with open(param, 'r', encoding='utf8') as f:
        line1 = f.readline()
        line2 = f.readline()
        print(line2)

        temp_list = line2.split(",")
        length = len(temp_list)
        length = int(length/2)
        for i in range(length):
            data_list.append([temp_list[i*2],int(temp_list[i*2+1])])
    return data_list


print(transform_data('202007\\s1_20200729_1.txt'))
