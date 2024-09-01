

even_list=[]
for i in range(0,100,2):
    even_list.append(i)
print(even_list)
    
even_list2=[ i for i in range(0,100,2)]
print(even_list2)


div_5=[]
for i in range(500):
    if i%5==0:
        div_5.append(i)
print(div_5)

div_51=[ i  for i in range(500) if i%5==0]
print(div_51)