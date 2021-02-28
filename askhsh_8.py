import urllib.request
import json

arxeio = input('Δώσε ένα αρχείο: ')

a = open(arxeio, 'r')

b = json.loads(a.read())

a.close()

y = len(b)

c = list(b.keys())
v = list(b.values())

for i in range (y):
    str = c[i]
    url = "https://min-api.cryptocompare.com/data/pricemulti?fsyms="+str+"&tsyms=EUR"
    r = urllib.request.urlopen(url)
    z = r.read()
    z = z.decode()
    d = json.loads(z)
    euro = str + ' σε ευρω:'
    euros = int(d[str]['EUR']) * v[i]
    print(euro, euros)
