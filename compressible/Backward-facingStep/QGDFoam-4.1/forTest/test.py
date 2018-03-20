import sys
task,vvod = (sys.argv)
vvod = float(vvod)

calc_file = open("../postProcessing/sampleDict/10/line_U.csv")
res_file = open("./testBFS")

frun = calc_file.readline()
srun = res_file.readline()
file1= calc_file.readline()
file2= res_file.readline()

a,b,c,d = file1.split(",")
a2 = float(a)
b2 = float(b)
file1= calc_file.readline()

i=0

while file2 :
    e,f = file2.split(" ")
    e = float(e)
    f = float(f)
    if vvod != e :
        file2= res_file.readline()
    else:
        i=1
        break

if i!=0 :
    print('good Re ')
    print(e)
else:
    print('bad Re')
    print(e)
    print('there is no experiment data for this Re')
    print('0')
    sys.exit()

while file1 :
    i=0
    a,b,c,d = file1.split(",")
    a1 = a2
    b1 = b2
    a2 = float(a)
    b2 = float(b)
    
    bb = b1*b2
    if 0 <= bb :
        xs = (a2+a1)/2
        px = abs(a1-f)/f
        if px <= 0.05 :
            i=1
        else:
            print('Bad test. Pogreshnost > 5%')
            print('0')
        break 
    else:
        file1= calc_file.readline()

if i!=0 :
    print('Good test. pogreshnost <= 5%')
    print('1')
else:
    sys.exit()

print("end")

calc_file.close()
