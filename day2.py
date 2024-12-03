#Day2
#Part1
with open('day2.txt', 'r') as file:
    datas = [list(map(int, line.split())) for line in file]
print(len(datas))
safe_list= []
unsafe_list = []
safty_num = 0
for data in datas:
    decline = False
    if data[0] > data[1]:
        decline = True
    safe = True
    if decline:
        for i in range(1,len(data)):
            diff = abs(data[i]-data[i-1])
            if data[i] < data[i-1] and diff <= 3 and diff >= 1:
                continue
            else:
                safe = False
    else:
        for i in range(1,len(data)):
            diff = abs(data[i]-data[i-1])
            if data[i] > data[i-1] and diff <= 3 and diff >= 1:
                continue
            else:
                safe = False
    if safe:
        safty_num += 1
        safe_list.append(data)
    else:
        unsafe_list.append(data)

print(safty_num)

#Part2
def check_list_safe(data):    
    decline = False
    if data[0] > data[1]:
        decline = True
    safe = True
    if decline:
        for i in range(1,len(data)):
            diff = abs(data[i]-data[i-1])
            if data[i] < data[i-1] and diff <= 3 and diff >= 1:
                continue
            else:
                safe = False
    else:
        for i in range(1,len(data)):
            diff = abs(data[i]-data[i-1])
            if data[i] > data[i-1] and diff <= 3 and diff >= 1:
                continue
            else:
                safe = False
    return safe

# Adding Problem Dampener
safe_list= []
unsafe_list = []
safty_num_new = 0
for data in datas:
    safe = False
    results = [data[:i] + data[i+1:] for i in range(len(data))]
    for result in results:
        if check_list_safe(result):
            safe = True
    if safe:
        safty_num_new += 1
        safe_list.append(data)
    else:
        unsafe_list.append(data)
print(safty_num_new)
