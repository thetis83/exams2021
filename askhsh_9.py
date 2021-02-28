import math

filename = input('Δώσε αρχείο: ')
f = open(filename, 'r')
f = f.read()

file = []

for j in range (len(f)):
    l = ord(f[j])
    if((l % 2) != 0):
        file.append(l)

a = file.copy()
a.sort()

x = []
k = []
n = 0;

while (n < len(a)):
    letter = a[n]
    if((letter >= 65 and letter <= 90) or (letter >= 97 and letter <= 122)):
        arithmos = a.count(letter)
        x.append(arithmos)
        n += arithmos
        k.append(letter)
    else:
        n += 1

print('Στατιστικά κάθε γράμματος:')

for i in range (len(k)):
    rate = (x[i] / len(a)) * 100
    rate = math.ceil(rate)
    allrate = rate * '*'
    print(chr(k[i]),':', allrate, rate,'%')
