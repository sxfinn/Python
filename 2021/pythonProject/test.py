
# ans = 0
# x = []
# s = 11 * 7
# for i in range(1,50):
#
#     if ans < 3000:
#         list.append(x,ans)
#     else:
#         break
#     ans += s
# print(x)
# b = []
#
# for i in range(3000):
#     if i % 11 == 0 and i % 7 == 0:
#         list.append(b, i)
# print(b)
# import random
# for i in range(50):
#     print(random.randrange(0,100,2))
# cnt1 = 0
# cnt2= 0
# cnt3 = 0
# strs = input('输入字符串：')
# n = len(strs)
# for i in range(n):
#     if '0'<= strs[i] <='9':
#         cnt1 += 1
#     elif 'a' <= strs[i] <= 'z' or 'A' <= strs[i] <= 'Z':
#         cnt2 += 1
#     else:
#         cnt3 += 1

# print(cnt1,cnt2,cnt3)

# for i in range(6):
#     grade = input('请输入成绩')
#     x = int(grade)
#     if x < 60:
#         print('bu及格')
#     elif 60<x<80:
#         print('及格')
#     else:
#         print('优秀')
# import random
# cnt1 = 0
# cnt2 = 0
# for i in range(100):
#     if random.randint(1,100) % 2:
#         cnt1 += 1
#     else:
#         cnt2 += 1
#
# print(cnt1,cnt2)
# i = 17
# while(i < 200):
#     i += 17
# print(i - 17)
# print(not 2)
#
# for i in range(1, 101):
#     if not i % 7 and i % 5:
#         print(i)

# global a
# a = 3
# def f():
#     return a + 3
#
# print(a)
# print(str(456)+'123')
# a = 3
# if a == 4:
#     print('t')
# elif a != 1:
#     print(1)
# x=['123','45','6','ab']
# print(max(x,key = str))
# print(max([23,4.5,60,76,87]))
# f=lambda x,y:x*y
# m = list(map(f,[1,2,3],[4,5,6]))
# print(m)
# x=[2,3,6,0,9,'as','ab']
# a = [4.3,3.4,4.4]
# print(max(x,key=str))
# print(max(a,key=float))
# print(tuple(map(str,[1,2,3])))
# print(sum(range(4)))
# def demo(a,b,c=5):
#     print(b,c,a)
#
# demo(c=7,b=3,a=1)
# def demo(**p):
#     print('This is a dict',p)
#
# demo(7, 3, 1)
# def f(a,b,c):
#     print(c+b+a)
#
# a=[1,2,3]
# f(*a)
# def f():
#     a=[1,2,3]
#
# global a
# a=[4,5,6]
# f()
# a = [1,2,3]
# a = [4,5,6]
# print(a)
# D={'f1':lambda:print('Ok'),'f2':lambda:print('Lambda'),'f3':lambda:print('Python')}
# D['f2']()
# print(1, 2, 3, sep=':')

# global a
# def f():
#     return a +3
#
# a = 1
# a += 1
# print(f())
# print(a)

# print(a)
# def f(p):
#     return(a+p)
#
# global a
# a=6
# b=4
# print(f(b))


# string='Hello World'
# print(string[:-2:-1])
# b=10
# # b + 1 = b + 1
# a=b==10
# print(a)
# a=['a','b','c']
# print(''.join(a))

# def f():
#     print('a')
# print('9'-1)
# a = 'abc.abc.ewjkfd'
# print(a.split('.',1))
# print(a)
# str = 'abcd'
# len = len(str)
# print(len)
# a = {'x':1,'v':2}
#
# a['x'] = 2
# print(a)
# 你 = 1
# print(你)
# is = 1
# print(is)
# for i in range(0,4):
#     print(i)
# print(i)
# print(0 * 0)
# print(True - 1)
# print(False - 1)
# a = list()
# print(list())
# print(tuple(range(1,5)))
# x = {1,2}
# print(x)
# a = 'abcd'
# a[0] = 'K'
# print(a)
# b = set('abc')
# c = {'a','b','c'}
# print(b)
# print(c)
# a = [1,2,3]
# print(2 is a[1])
# if a:
#     print(1)
# else:
#     print(2)
# L=tuple(3,2,1)
# S = (3,2)
# # print(L)
# print(S)


# a = [1,2,3]
# m = max(a)
# print(m)

# a = {'a':1,'b':2}
# print(a.keys())
#
# def f():
#     global x
#     for i in range(6):
#         x += 1
#         b = i
#
# x = 0
# b = 0
# f()
# print(x,b)
# s=[1,2,3]
# s.insert(2,100)
# s.append([4,5,6])
# s.insert(1,7)
# del s[0]
# print(s)
# D={'name':'tom','age':36,'sex':'male','score':76,'f':lambda x,y,z:print(x+y+z)}
# print(D['f'](D['name'],D['sex'],str(D['score'])))

# ac = {'a' : 1, 'b' : 2}
# print(ac['a'])
# T=('Hello',[1,2,3,'World'],{'language':'python','computer':80586},lambda x,y,z:print(x+y+z))
# print(T[-1](T[0],T[1][3],T[2]['language']))
#
# L=[(1,2,3),'abc',{'name':'peter','age':23},[3,4,5]]
# print(str(L[-1][0])+L[1][2])
# print(L[2]['name']+ list(L[2].keys())[1]+'is'+str(L[2]['age']))
# print(L[0][0]+L[3][5]==6)
# def demo(n):
#     return n * n
#
#
# f = lambda x: (demo(x))
# print(f(6))
#
# T = {1: lambda x, y: x ** y, 2: lambda x: x ** 3, 3: lambda x, y, z: x + y + z}
# print(T[3](3, 2, 4))

# T=(lambda x,y:x**y,lambda x:x**3,lambda x,y,z:x+y+z)
# print(T[0](2,3))
#
# f=lambda x,y=2,z=3:x*y*z
#
# print(f(1))
# def f(a, b, c):
#     print(c + b + a)
#
#
# a = [1, 2, 3, 4]
# f(*a)

# def f1(m,b,c):
#     print(c+b+m)
#
# a={'a':1,'b':2,'c':3}
# f1(x=1,b=2,c=3)

# def f1(a,b,c):
#     print(c+b+a)
#
# a = {'a':1,'b':2,'c':3}
# f1(*a.values())

# def f(a, b, c):
#     print(c, b, a)
#
#
# a = [1, 2, 3]
# f(*a)
#
#
#     return (p)
#
#
# print(f(age=23, name='peter', score=78))
#
#
# def f(*p):
#     print(p)
#
#
# f(1, 'abc', 3.6)

# a = [1, 2, 3]
# a = a[::-1]
# print(a)
#
# def f(b):
#     a = b[::--1]
#
#
# print(a)

# a=[3,5,7]
# def f3(b):
#     b[0]=b[1]
#     return b
#
# print(f3(a))

# a = [3, 5, 7]
#
#
# # print(a[::-1])
#
# def f3(b):
#     b = b[::-1]
#     # print(b)
#     return b
#
#
# print(a)
# a = 3
# def f(a):
#     a = 5
#
# f(a)
# print(a)
# def f(a,b):
#     return (a+b)*3
#
#
# print(f((1,2),(3,4)))


# def f2(a):
#     assert isinstance(a,int),'a must be a interger'
#     str_a=str(a)
#     return (int(str_a[::-1]))
# def
# f2(123)


# def f(a):
#     if a == 1:
#         print('123456 is %e' % 123456)
#     elif a == 2:
#         print('the second is{1:} and first is {0:},third is {2:}'.format(1, 2, 3))
#     else:
#         print(f'{a + 1} and {a + 2},{a + 3}')
#
#
# f(30)

# def f(a):
#     if a == 1:
#         print('123456 is %e' % 123456)
#     elif a == 2:
#         print('the second is{1:} and first is {0:},third is {2:}'.format(1, 2, 3))
#     else:
#         print(f'{a + 1} and {a + 2},{a + 3}')
#
#
# f(3)
#
#
# def f(a):
#     if a == 1:
#         print('123456 is %e' % 123456)
#     elif a == 2:
#         print('the second is{1:} and first is {0:},third is {2:}'.format(1, 2, 3))
#     else:
#         print(f'{a + 1} and {a + 2},{a + 3}')
#
#
# f(1)
#
#
# def f(a,b,c):
#     return(a+b+c)
#
# d={'a':1,'b':2,'c':3}
# print(f(**d))
#
#
#
# def f(a,b,c):
#     return(a+b+c)
#
# d={1:'a',2:'b',3:'c'}
# print(f(*d.values()))


# def f(a):
#     global x
#     x = 3 + a
#
#
# x = 6
# f(4)
# print(x)
# def f(a):
#     x = a + 1
#
#
# x = 5
# a = 6
# f(a)
# print(x)
#
# def f(a, b, c):
#     print(c + b + a)
#
#
# a = [1, 2, 3]
# f(*a)
#
#
# def f(a, b, c):
#     print(c,b,a)
#
# a=[1,2,3]
# f(*a)
#
# def f(*p):
#     print(p)
#
#
# f(1, 2)
#
#
# def say1(message, times):
#     print(message * times)
#
#
# say1('hello', 3)
# n = 1 + 1
# print(n)
# def f(x,y,z):
#     print(z,y,x)
#
# f(1,2,3,4)

# a=10
# b='Hello World'
# c=[1,2,3]
# print(f'The first item is {b} and the second item is {c},the last item is {a+20}')
#
#
# print( 'The second number is {1:} and the first number is {0:},the third number is {2:}' .format(0,3,10))
# print('The number 112345 is %e'%112345)
# a = 2
#
# print(--2)
#
# string = 'hello'
# print(string[-1::-2])

# a,b,c=1+2,2+3,3+4
# a,b,c=a+b+c,c+3,a*3
# d=[a,b,c]
# print(d)

# def f(x,y):
#     z = x + y
#
# b = 0
# b = f(3,9)
# print(b)
# a = list(range(4,2,-1))
# print(a)
# f = lambda a, b :a + b
# print(f(3,4))
# a = '中国成都AAA'
# print(len(a))
# print('abcd' is a)
# a = [1,2,3,4]
# print(2 is a)
# print(3 is 3)
# # print(10 > 20 and 1)
# print(-2 < -1 < 0)
# print('abc\kls')
#
# print(int(6.6)/3)
# t = (123,'hello',123)
# print(t[1][0])

#
#
# for i in range(1,5):
#     print(i)
#     if i >= 3:
#         continue

# s = 1
# s += 9
# print(s)
#
# a = {1, 2, 3}
# if a:
#     print('set')
# else:
#     print('empty set')
#
# if 3:
#     print(3)
# else:
#     print(4)

# for i in range(10):
#     print('a')
# s1 = 'abc'
# print(s1 * 3)
#
# s2 = 'efg'
# print(s1 + s2)
# for i in range(10):
#     print(i)
