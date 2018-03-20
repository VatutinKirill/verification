res_file = open("./results")

data = res_file.readline()
data = res_file.readline()
data = res_file.readline()

data = res_file.readline()
i = float(data)
su = i

data = res_file.readline()
data = res_file.readline()
data = res_file.readline()

data = res_file.readline()
i = float(data)
su = su + i

data = res_file.readline()
data = res_file.readline()
data = res_file.readline()

data = res_file.readline()
i = float(data)
su = su + i

if su!=3 :
    print('BFStest fail')
else :
    print('BFStest OK')

res_file.close()
