countries=[]
for line in open('QAPYTH3 v.19/Labs/QAPYTH3 v1_9 labs/country.txt') :
    countries.append(line.split(','))

def sort_by_index_1(raw_country_data):
    return raw_country_data[2]

countries.sort(key=sort_by_index_1)


def sort_by_index1(line) -> int:
    return int(line[1])




countries.sort(key=sort_by_index1)

countries.sort(key=lambda c: (int(c[1])))
for line in countries:
    print(','.join(line),end="")