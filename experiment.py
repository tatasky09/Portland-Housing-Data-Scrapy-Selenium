line_lst = []
with open('add_id_new.txt', 'r', 1) as f:
    for line in f:
        if not line.startswith('\n'):
            line_lst.append(line)
# print(line_lst[2:15])
web_lst1 = []
for i in line_lst:
    i = i.strip('\n')
    # i = i.strip('/')
    # i = i.replace(' ', '-')
    # i = i.replace('&', '-')
    # i = i.replace(';', '/')
    # add = '/detail/assessor/' + i + '_did/'
    web_lst1.append(i)
web_lst = web_lst1[:]
print(web_lst.index('3658 SE BYBEE BLVD;R114981'))