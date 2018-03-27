res_file = open("./results")

data = res_file.readline()
data = res_file.readline()
data = res_file.readline()

data = res_file.readline()
i = float(data)
su = i

if su!=1 :
    print('BFStest fail')
else :
    print('BFStest OK')

res_file.close()
