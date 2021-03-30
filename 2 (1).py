# заменить буквы x на y
исходная="xdf d f xx l x dnn x nn vd"
новая=""
for i in исходная:
   if i=="x":
       новая += "y"
   else:
       новая += i
print(исходная)
print(новая)


# произведение чисел картных 3 и 5
x=[1,2,3,4,6,7,8,9,3]
y3=1
y5=1
for i in x:
    if i//3==i/3:
        y3+=i
    else:
        i//5==i/5
        y5+=i
print(y3)
print(y5)

# заменить буквы x на y
print('xdf d f xx l x dnn x nn vd'.replace('x', 'y'))
