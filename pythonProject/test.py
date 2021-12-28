a = {'a':1,'b':2}
print(a.keys())

def f():
    global x
    for i in range(6):
        x += 1
        b = i

x = 0
b = 0
f()
print(x,b)
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
