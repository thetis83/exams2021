import datetime
import urllib.request
import json

date = datetime.datetime.now()      
year = date.strftime('%Y')   
month = date.strftime('%m')  
day = date.strftime('%d')    

listDays = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20','21', '22', '23', '24', '25', '26', 
            '27', '28', '29', '30', '31']
d = day   
if (d[0] == '0'):  
    d = list(d)   
    d.pop(0)       
    d = str(d) 
    d = d.replace('[', '' )
    d = d.replace(']', '' )
    d = d.replace("'", '' )
array_day = []     

for i in listDays:     
    if(i > d):
        break      
    else:          
        array_day.append(i)
number = []        
d = int(d)

for i in range (d): 
    maximum = 0       
    days = array_day[i]  
    Dates = year + '-' + month + '-' +days  
    url_a = 'https://api.opap.gr/draws/v3.0/1100/draw-date/' + Dates + '/' + Dates + '/draw-id' 
    r_a= urllib.request.urlopen(url_a)
    id = r_a.read()              
    id = id.decode()
    id = list(id)   
    id.pop(0)            
    id.pop()             

    array_id = []                  
    times = ''                

    for j in range (len(id)):
        if(id[j] != ','):
                times += id[j]  
        else:
            array_id.append(times)        
            times = ''
    all_numbers = []                           

    for a in range (len(array_id)):       
        ids = array_id[a]
        url_b = 'https://api.opap.gr/draws/v3.0/1100/' + ids
        r_b = urllib.request.urlopen(url_b)
        link = r_b.read()
        link = link.decode()
        dict = json.loads(link)        
        all_numbers.extend(dict['winningNumbers']['list'])

    for b in range (len(all_numbers)):  
        x = all_numbers[b]              
        y = all_numbers.count(x)        
        if (maximum < y):
            maximum = y          
            thesi = b           

    number.append(all_numbers[thesi])     

print('\n Ο συχνότερα εμφανιζόμενος αριθμός του ΚΙΝΟ κάθε μέρα του μήνα είναι:\n')

for c in range (len(number)):
    print( c + 1,'η μέρα ο αριθμός είναι:', number[c])
