print('Введіть висоту кожної діаграми Ферре, для закінчення двічі нажимайте enter')
a = int(input('-->> '))
rices = []
while True:
    try:
        rices.append(a)
        a = int(input('-->> '))
    
    except:
        break

val = 1
for i in rices:
    val *= i
print("Кількість траєкторій на заданій діаграмі Ферре:")
print(val)
