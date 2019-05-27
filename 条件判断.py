'''
age = 20
if age > 18:
    print('your age is',age)
else:
    print('adult')
'''

'''
s = input('brith:')
birth = int(s)
if birth < 2000:
    print('00前')
else:
    print('00后')
 '''

'''elif判断
height = 1.75
weight = 80.5
BMI = weight/(height*height)
if 25 > BMI > 18.5:
     print('正常')
elif 28 > BMI > 25:
    print('过重')
elif 32 > BMI > 28:
    print('肥胖')
elif BMI > 32:
    print('严重肥胖')
else:
    print('过轻')
'''
'''BMI计算
h = input('height:')
w = input('weight:')
height = float(h)
weight = float(w)
BMI = weight/(height*height)
if 25 > BMI > 18.5:
     print('正常')
elif 28 > BMI > 25:
    print('过重')
elif 32 > BMI > 28:
    print('肥胖')
elif BMI > 32:
    print('严重肥胖')
else:
    print('过轻')
'''
''' for循环

names = ['Michael', 'Bob', 'Tracy']
for name in names:
    print(name)
'''
'''1~10求和
sum = 0 
for x in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]:
    sum = sum + x
print(sum)
'''
'''5~10求和
sum = 0
for x in range(5,10):
    sum = sum + x
print(sum) 
'''
'''
L = ['Bart', 'Lisa', 'Adam']
for name in L:
    print('Hello,',name,'!')
'''
n = 1
while n <= 100:
    if n > 10: # 当n = 11时，条件满足，执行break语句
        break # break语句会结束当前循环
    print(n)
    n = n + 1
print('END')