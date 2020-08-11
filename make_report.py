

report_data = []

def check_dupl(item_list):

    for i in range(len(report_data)):
        if report_data[i][0] == item_list[0]:
            return True, i
    return False, None


def make_report(param_list):

    for i in param_list:

        is_dupl, no_dupl = check_dupl(i)
        if is_dupl:
            report_data[no_dupl][1] = i[1] + report_data[no_dupl][1]
        else:
            report_data.append(i)

    with open('202007.csv', 'w', encoding='utf8') as f:
        for i in report_data:
            f.write("{0},{1}\n".format(i[0],i[1]))

make_report([['a',1], ['b',1], ['a',1], ['c',1]])
make_report([['r',1], ['b',1], ['a',1], ['c',1]])
print(report_data)
