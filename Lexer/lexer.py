import os
os.chdir('c:\\Users\\Victor\\Desktop\\Lexer')
class tok (object):
    pal = ""


sint = open("sintaxis.vx")
ln = sint.readline()
vec = [0] *100
c = 0
while ln != '':
    c = c+1
    a = tok()
    a.pal = ln
    vec[c] = a
    ln = sint.readline()
sint.close()
file = open("trial.vx")
l = file.readline()
v2 = [0] *100
c2 = 0
log = open("log.vx", "x")
while l != '':
    flag = 0;
    c2 = c2+1
    for i in range (1,c):
        if l == vec[i].pal:
            flag = 1
            b = tok()
            b.pal = l
            v2[c2] = b
    if flag == 0:
        if l[0] == "/" or l[0] == "&":
            if l[1].isdigit():
                log.write("Error Linea" + str(c2) + "\n")
            else:
                flag = 1
                b = tok()
                b.pal = l
                v2[c2] = b
        else:
            if l[0] == "/" and l[1] == "/":
                flag = 1
                b = tok()
                b.pal = l
                v2[c2] = b
            else:
                log.write("Error Linea" + str(c2) + "\n")
    l = file.readline()
file.close()
log.close()
