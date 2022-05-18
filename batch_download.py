import os


f1 = open('./urls.txt')
content = f1.readlines()
f1.close()

f2 = open('./config.txt')
configs = f2.readlines()
f2.close()


start = int(configs[0].strip())
end = int(configs[1].strip())
openssh = configs[2].strip()

while True:
    for i in range(start-1,end):
        url = content[i].split('uk/')[1].strip()
        os.system(f'ascp -i {openssh} -v -QT -l 100m -P33001 -k1 era-fasp@fasp.sra.ebi.ac.uk:/{url} ./')
        