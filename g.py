dict = [{'product': 'leather_wallet', 'unit_price': 1100, 'GST': 18, 'quantity':1},
        {'product': 'umbrella', 'unit_price': 900, 'GST': 12, 'quantity':4},
        {'product': 'cigrate', 'unit_price': 200, 'GST': 28, 'quantity':3},
        {'product': 'honey', 'unit_price': 100, 'GST': 0, 'quantity':2}]
GST = []
t=[]
ct=0
for i in range (0,4):
    
    t.append(dict[i]['unit_price']*dict[i]['quantity'])
    if dict[i]['GST'] != 0:
        GST.append(t[i]*dict[i]['GST']/100)
    else:
        GST.append(0)

max=GST[0]
for i in range(1,4):
    if GST[i]>max:
        max=GST[i]
        ct=i

print("maximum",dict[ct],"amt",GST[ct])

sum=0
for i in range(4):
    sum += GST[i]+t[i]

print(sum)      

