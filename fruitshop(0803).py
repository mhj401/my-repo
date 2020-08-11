import os

report_data = []

###############################################################################
def dir_list(param_string):  #경로를 읽어 와서 파일로 접근하는 함수 만들기
    with os.scandir(param_string) as entries:
        for entry in entries:
            file_name = entry.name
            print(file_name)
            t_list = transform_data("{0}\\{1}".format(param_string, file_name))
            make_report(t_list)
###############################################################################




def transform_data(param): #dir_list의 함수의 결과값을 다시 입력값으로 받고 2차원 리스트(품명, 수량)로 변환하는 함수 만들기
    data_list = []
    with open(param, 'r', encoding='utf8') as f: #r은 파일 읽기
        line1 = f.readline()    #sdf1_20200729
                                #sdf1_20200729
                                #sdf2_20200729
                                #sdf2_20200729

        line2 = f.readline()    #a,1,d,2,s,3,c,4,s,5,d,3
                                #a,2,d,3,d,4,v,3,s,2,a,1,s,2
                                #a,2,d,2,s,4,c,4,s,5,d,3
                                #a,1,d,3,d,6,v,3,s,1,a,2,s,2

        print(line2) #s1_20200729_1 => a,1,d,2,s,3,c,4,s,5,d,3
                     #s1_20200729_2 => a,2,d,3,d,4,v,3,s,2,a,1,s,2
                     #s2_20200729_1 => a,2,d,2,s,4,c,4,s,5,d,3
                     #s2_20200729_2 => a,1,d,3,d,6,v,3,s,1,a,2,s,2

        temp_list = line2.split(",")
        print(temp_list)
        length = len(temp_list)
        length = int(length / 2)
        for i in range(length):
            data_list.append([temp_list[i*2], int(temp_list[i*2+1])])
        print(data_list)    #[['a', 1], ['d', 2], ['s', 3], ['c', 4], ['s', 5], ['d', 3]]
                            #[['a', 2], ['d', 3], ['d', 4], ['v', 3], ['s', 2], ['a', 1], ['s', 2]]
                            #[['a', 2], ['d', 2], ['s', 4], ['c', 4], ['s', 5], ['d', 3]]
                            #[['a', 1], ['d', 3], ['d', 6], ['v', 3], ['s', 1], ['a', 2], ['s', 2]]
        return data_list


def check_joongbok(item_list): #중복 판정하는 함수 만들기
    for i in range(len(report_data)):
        if report_data[i][0] == item_list[0]:
            return True, i #여기에 쓰이는 i는 왜 써야하는지 설명 부탁드립니다.
    return False, None

def make_report(param_list): #중복 처리 후 합산하는 최종파일을 만드는 함수 만들기
    for i in param_list:
        is_joongbok, no_joongbok = check_joongbok(i)
        if is_joongbok:
            report_data[no_joongbok][1] = i[1] + report_data[no_joongbok][1]

        else:
            report_data.append(i)

    print(report_data)  #[['a', 1], ['d', 5], ['s', 8], ['c', 4]]
                        #[['a', 4], ['d', 12], ['s', 12], ['c', 4], ['v', 3]]
                        #[['a', 6], ['d', 17], ['s', 21], ['c', 8], ['v', 3]]
                        #[['a', 9], ['d', 26], ['s', 24], ['c', 8], ['v', 6]]





#################################################################################################
    with open('202007_2.csv', 'w', encoding = 'utf8') as f: #make_report로 만들어진 결과값을 모아서 csv파일로 쓰기
        for i in report_data:
            f.write("{0},{1}\n".format(i[0],i[1]))

dir_list('202007')
#################################################################################################