res = open("./results")

rs= res.readline()
rs= res.readline()
a0 = float(rs)
rs= res.readline()
rs= res.readline()
b0 = float(rs)
rs= res.readline()
rs= res.readline()
c0 = float(rs)
rs= res.readline()
rs= res.readline()
d0 = float(rs)
rs= res.readline()
rs= res.readline()
e0 = float(rs)

rs= res.readline()

rs= res.readline()
rs= res.readline()
a1 = float(rs)
rs= res.readline()
rs= res.readline()
b1 = float(rs)
rs= res.readline()
rs= res.readline()
c1 = float(rs)
rs= res.readline()
rs= res.readline()
d1 = float(rs)
rs= res.readline()
rs= res.readline()
e1 = float(rs)

rs= res.readline()

rs= res.readline()
rs= res.readline()
a2 = float(rs)
rs= res.readline()
rs= res.readline()
b2 = float(rs)
rs= res.readline()
rs= res.readline()
c2 = float(rs)
rs= res.readline()
rs= res.readline()
d2 = float(rs)
rs= res.readline()
rs= res.readline()
e2 = float(rs)

dx1 = a0 - a1
du1 = b0 - b1
dp1 = c0 - c1
dT1 = d0 - d1
drho1 = e0 - e1

dx2 = a1 - a2
du2 = b1 - b2
dp2 = c1 - c2
dT2 = d1 - d2
drho2 = e1 - e2

i = 0

#if dx1 < 0:
#    print('we do not have mesh independence for ')
#else:
#    if dx2 < 0:
#        print('we do not have mesh independence for ')
#    else:
#         print('mesh independence for ')
#        i=i+1

if du1 < 0:
    print('we do not have mesh independence for u')
else:
    if du2 < 0:
        print('we do not have mesh independence for u')
    else:
        print('mesh independence for u')
        i=i+1

if dp1 < 0:
    print('we do not have mesh independence for p')
else:
    if dp2 < 0:
        print('we do not have mesh independence for p')
    else:
        print('mesh independence for p')
        i=i+1

if dT1 < 0:
    print('we do not have mesh independence for T')
else:
    if dT2 < 0:
        print('we do not have mesh independence for T')
    else:
        print('mesh independence for T')
        i=i+1

if drho1 < 0:
    print('we do not have mesh independence for rho')
else:
    if drho2 < 0:
        print('we do not have mesh independence for rho')
    else:
        print('mesh independence for rho')
        i=i+1
if 4<=i<=4:
    print('SOD test Ok')
else:
    print('smth go bad with mesh independence in SOD test')
    
res.close()
