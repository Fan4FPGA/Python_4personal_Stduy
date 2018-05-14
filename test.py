#import sys
#print('================Python import mode==========================');
#print ('命令行参数为:')
#for i in sys.argv:
#    print (i)
#print ('\n python 路径为',sys.path)
#from sys import argv,path  #  导入特定的成员
 
#print('================python from import===================================')
#print('path:',path) # 因为已经导入path成员，所以此处引用时不需要加sys.path
#a, b, c = 1, 2, "runoob"
#print(c)
#a, b, c, d = 20, 5.5, True, 4+3j
#print(type(a),type(b),type(c),type(d))
#a = 111
#print(isinstance(a,int))

#a = "3+5*3"
#print(a)

#Fibonacci Series 斐波那契数列
#两个元素的总和确定下一个数
'''a,b = 0,1
while b < 10:
    print(b,"--",a, end = ',')
    a, b = b, a+b'''
	

	
#TempConvert
#温度转换
'''
TempStr = input("请输入温度值：")
if TempStr[-1] in ['F', 'f']:
   C = eval(TempStr[0:-1])*1.8 + 32
   print("摄氏温度值:{:.2f}C".format(C))
elif TempStr[-1] in ['C', 'c']:
   F = (eval(TempStr[0:-1])-32)/1.8
   print("华氏温度值:{:.2f}F".format(F))
else:
    print("输入格式错误")
input("点击ENTER键退出")
'''




#测试返回值得类型
'''
x = 5
y = 4
print(type(x == y))
'''

'''
x = 5
y = 4
print(type(x + y))
'''

'''
x = 5
y = 4.5
print(type(x + y))
'''





#猜数字字谜游戏
'''
num = 8
guess = -1
print("---NUMBER GAME---")
while num != guess:
   guess = int(input("Please typein your guess number！\n"))
   if guess == num:
       print("congratulation！you are right！")
   elif guess < num:
       print("the number is small...\n")
   elif guess > num:
       print("the number is big...\n")

input("Type Enter for Exiting!")

'''

#if语句嵌套
'''
num=int(input("输入一个数字："))
if num%2==0:
    if num%3==0:
        print ("你输入的数字可以整除 2 和 3")
    else:
        print ("你输入的数字可以整除 2，但不能整除 3")
else:
    if num%3==0:
        print ("你输入的数字可以整除 3，但不能整除 2")
    else:
        print  ("你输入的数字不能整除 2 和 3")
'''


#使用while计算1到100的总和
'''
n = 101
sum = 0
counter = 1
while counter <= n:
    sum = sum + counter
    counter += 1
print("1到%d之和为:%d"%(n,sum))
'''


#无限循环,Ctrl+C 退出循环
'''
var = 1
while var == 1:
    num = int(input("输入一个数字:"))
    print("你输入的数字是",num)
print("Good Bye")
'''

#while...else...
'''
count = 0
while count<10:
    print(count,"小于10")
    count = count + 1
else:
    print(count,"大于等于10")
'''



#PythonDraw.py
'''
import turtle                           #import库
turtle.setup(650, 350, 200, 200)		#设置窗口大小和位置turtle.setup(width, height, startx, starty)	
turtle.penup()							#提笔，之和的运动不留下轨迹
turtle.fd(-250)							#前进，按照turtle当前的方向前进，参数为负值则为倒退
turtle.pendown()						#落笔，之后的云运动留下轨迹
turtle.pensize(25)						#画笔大小
turtle.pencolor("purple")				#画笔颜色	
turtle.seth(-40)						#设置海龟朝向，turtle.setheading(angle)
for i in range(4):						#固定循环搭配，range函数表示的含义为生成一个0,1,2,3的序列，若range(2,5)则为2,3，4	
    turtle.circle(40, 80)				#角度坐标体系，turtle.circle(r,angle)以turtle左侧半径为r的地方为圆心行走angle度，若不填写angle值则默认360°
    turtle.circle(-40, 80)
turtle.circle(40, 80/2)
turtle.fd(40)
turtle.circle(16, 180)
turtle.fd(40 * 2/3)
turtle.done()
'''

#draw 'Z'
'''
import turtle as t
t.setup(650, 350, 0, 0)
t.pu()
t.seth(90)
t.fd(50)
t.seth(0)
t.pd()
t.pensize(10)
t.pencolor(1,0.5,0.3)
t.fd(100)
t.right(135)
t.fd(200)
t.left(135)
t.fd(100)
t.done()
'''

#turtle.goto(x,y)
#draw 口
'''
import turtle as t
t.setup(650, 350, 0, 0)
t.pu()
t.pensize(10)
t.pencolor(1,0.5,0.3)
t.goto(100,100)
t.pd()
t.goto(100,-100)
t.goto(-100,-100)
t.goto(-100,100)
t.goto(100,100)
t.done()
'''


#for
'''
languages = ["C", "C++", "Perl", "Python"]
for x in languages:
    print(x)
'''

'''
for i in range(10):
    print(i)
'''

'''
for i in range(5,9):
    print(i)
'''

'''
for i in range(0,10,3):     #3为步长，结果为0、3、6、9
    print(i)
'''

'''
sites = ["Baidu", "Google","Runoo1","Taobao"]
for site in sites:
    if site == "Runoob":
        print("菜鸟教程!")
        break						#跳出for循环
    print("循环数据 " + site)
else:													#循环语句可以有 else 子句，它在穷尽列表(以for循环)或条件变为 false (以while循环)导致循环终止时被执行,但循环被break终止时不执行。
    print("没有循环数据!")
print("完成循环!")
'''

#continue的使用
'''
for letter in 'assoofofgofd':     # 第一个实例
   if letter == 'o':        # 字母为 o 时跳过输出
      continue
   print ('当前字母 :', letter)
'''

#使用range()与len()函数
'''
a = ['Google', 'Baidu', 'Apple', 'Taobao', 'QQ']
for i in range(len(a)):
    print(i,a[i])
'''

#python  pass是空语句，不做任何事情一般做占位语句
#ex		等待键盘中断(Ctrl+C)
'''
while True:
    pass
'''

#最小的类
'''
class MyEmptyClass:
   pass
'''

#在字母为o是执行pass语句
'''
for letter in 'Runoob': 
   if letter == 'o':
      pass
      print ('执行 pass 块')
   print ('当前字母 :', letter)
 
print ("Good bye!")
'''


#Python3迭代器与生存器
#迭代器有两个基本方法iter()和next()
'''
list = [1,2,3,4]
it = iter(list)		#创建迭代器对象
print(next(it))		#输出迭代器的下一个对象
print(next(it))
print(next(it))
print(next(it))
'''

'''
import sys         # 引入 sys 模块
list=[1,2,3,4]
it = iter(list)    # 创建迭代器对象 
while True:
    try:
        print (next(it))
    except StopIteration:
        sys.exit()
'''

#使用yield实现斐波那契数列
'''
import sys
#----------------------------------------------------	 
def fibonacci(n): # 生成器函数 - 斐波那契
    a, b, counter = 0, 1, 0
    while True:
        if (counter > n): 
            return
        yield a	  #返回a的迭代器			
        a, b = b, a + b
        counter += 1
#----------------------------------------------------		
f = fibonacci(10) # f 是一个迭代器，由生成器返回生成
while True:
    try:
        print (next(f), end=" ")
    except StopIteration:
        sys.exit()
'''

#定义一个最简单的无返回值的函数
'''
def hello():
	print('hello,world')

hello()
'''
'''
def area(width,height):
    return width*height
print(area(6,5))
'''



#变量没有类型，类型属于对象
#trings, tuples, 和 numbers 是不可更改的对象，而 list,dict 等则是可以修改的对象。
#不可变类型：变量赋值 a=5 后再赋值 a=10，这里实际是新生成一个 int 值对象 10，再让 a 指向它，而 5 被丢弃，不是改变a的值，相当于新生成了a。
#可变类型：变量赋值 la=[1,2,3,4] 后再赋值 la[2]=5 则是将 list la 的第三个元素值更改，本身la没有动，只是其内部的一部分值被修改了。

# 可写函数说明
'''
def changeme( mylist ):
   "修改传入的列表"
   mylist.append([1,2,3,4])
   print ("函数内取值: ", mylist)
   return
 
# 调用changeme函数
mylist = [10,20,30]
changeme( mylist )
print ("函数外取值: ", mylist)

'''
'''
from Tkinter import *  
root = Tk()  
root.mainloop()  
'''

#python 使用 lambda 来创建匿名函数。
#lambda 只是一个表达式，函数体比 def 简单很多。
#lambda的主体是一个表达式，而不是一个代码块。仅仅能在lambda表达式中封装有限的逻辑进去。
#lambda 函数拥有自己的命名空间，且不能访问自己参数列表之外或全局命名空间里的参数。
#虽然lambda函数看起来只能写一行，却不等同于C或C++的内联函数，后者的目的是调用小函数时不占用栈内存从而增加运行效率。


# 可写函数说明
'''sum = lambda arg1, arg2: arg1 + arg2
 
# 调用sum函数
print ("相加后的值为 : ", sum( 10, 20 ))
print ("相加后的值为 : ", sum( 20, 20 ))
'''


#Python 中，程序的变量并不是在哪个位置都可以访问的，访问权限决定于这个变量是在哪里赋值的。
#变量的作用域决定了在哪一部分程序可以访问哪个特定的变量名称。Python的作用域一共有4种，分别是：
#L （Local） 局部作用域
#E （Enclosing） 闭包函数外的函数中
#G （Global） 全局作用域
#B （Built-in） 内建作用域

#以 L –> E –> G –>B 的规则查找，即：在局部找不到，便会去局部外的局部找（例如闭包），再找不到就会去全局找，再者去内建中找。
#Python 中只有模块（module），类（class）以及函数（def、lambda）才会引入新的作用域，其它的代码块（如 if/elif/else/、try/except、for/while等）
#是不会引入新的作用域的，也就是说这些语句内定义的变量，外部也可以访问

#实例中 msg 变量定义在 if 语句块中，但外部还是可以访问的。
#如果将 msg 定义在函数中，则它就是局部变量，外部不能访问：


#实例
'''
total = 0 # 这是一个全局变量
# 可写函数说明
def sum( arg1, arg2 ):
    #返回2个参数的和."
    total = arg1 + arg2 # total在这里是局部变量.
    print ("函数内是局部变量 : ", total)
    return total

#调用sum函数
sum( 10, 20 )
print ("函数外是全局变量 : ", total)
'''

#函数内是局部变量 :  30
#函数外是全局变量 :  0


#当内部作用域想修改外部作用域的变量时，就要用到global和nonlocal关键字了。
'''
num = 1
def fun1():
    global num  # 需要使用 global 关键字声明
    print(num) 
    num = 123
    print(num)
fun1()
'''

#如果要修改嵌套作用域（enclosing 作用域，外层非全局作用域）中的变量则需要 nonlocal 关键字了，如下实例：
'''
def outer():
    num = 10
    def inner():
        nonlocal num   # nonlocal关键字声明
        num = 100
        print(num)
    inner()
    print(num)
outer()
'''


#另外有一种特殊情况，假设下面这段代码被运行：
'''
a = 10
def test():
    a = a + 1
    print(a)
test()
'''
#报错
#因为 test 函数中的 a 使用的是局部，未定义，无法修改。


#方法				描述
#list.append(x)		把一个元素添加到列表的结尾，相当于 a[len(a):] = [x]。
#list.extend(L)		通过添加指定列表的所有元素来扩充列表，相当于 a[len(a):] = L。
#list.insert(i, x)	在指定位置插入一个元素。第一个参数是准备插入到其前面的那个元素的索引，例如 a.insert(0, x) 会插入到整个列表之前，而 a.insert(len(a), x) 相当于 a.append(x) 。
#list.remove(x)		删除列表中值为 x 的第一个元素。如果没有这样的元素，就会返回一个错误。
#list.pop([i])		从列表的指定位置移除元素，并将其返回。如果没有指定索引，a.pop()返回最后一个元素。元素随即从列表中被移除。（方法中 i 两边的方括号表示这个参数是可选的，而不是要求你输入一对方括号，你会经常在 Python 库参考手册中遇到这样的标记。）
#list.clear()		移除列表中的所有项，等于del a[:]。
#list.index(x)		返回列表中第一个值为 x 的元素的索引。如果没有匹配的元素就会返回一个错误。
#list.count(x)		返回 x 在列表中出现的次数。
#list.sort()		对列表中的元素进行排序。
#list.reverse()		倒排列表中的元素。
#list.copy()		返回列表的浅复制，等于a[:]。


#列表方法使得列表可以很方便的作为一个堆栈来使用，堆栈作为特定的数据结构，
#最先进入的元素最后一个被释放（后进先出）。
#用 append() 方法可以把一个元素添加到堆栈顶。用不指定索引的 pop() 方法可以把一个元素从堆栈顶释放出来。例如：
'''
stack = [3, 4, 5]
stack.append(6)
stack.append(7)

print(stack.pop())
print(stack.pop())
print(stack.pop())
print(stack.pop())
print(stack.pop())
'''
#也可以把列表当做队列用，只是在队列里第一加入的元素，第一个取出来；但是拿列表用作这样的目的效率不高。
#在列表的最后添加或者弹出元素速度快，然而在列表里插入或者从头部弹出速度却不快（
#因为所有其他的元素都得一个一个地移动）。
'''
from collections import deque
queue = deque(["Eric", "John", "MIchael"])
queue.append("Terry")
queue.append("Graham")

print(queue.popleft())
print(queue.popleft())
print(queue.popleft())
print(queue.popleft())
print(queue.popleft())
'''

#列表推导式
'''
vec = [2, 4, 6]
print([3*x for x in vec])

print([[x, x**2] for x in vec])

freshfruit = ['banana', 'loganberry', 'passion fruit']
a = [weapon.strip() for weapon in freshfruit]
print(a)

b = [3*x for x in vec if x>3]
print(b)

c = [3*x for x in vec if x==2]
print(c)

vec1 = [2,3,4]
vec2 = [5,6,7]
d = [x*y for x in vec1 for y in vec2]
print(d)
e = [vec1[i]*vec2[i] for i in range(len(vec1))]
print(e)

f = [str(round(355/113, i)) for i in range(1,6)]
print(f)
'''


#嵌套列表解析
'''
matrix = [
     [1, 2, 3, 4],
     [5, 6, 7, 8],
     [9, 10, 11, 12],
 ]
#means_1
a = [[row[i] for row in matrix] for i in range(4)]
print(a)
#means_2
transposed = []
for i in range(4):
    transposed.append([row[i] for row in matrix])
print(transposed)
#means_3
transposed1 = []
for i in range(4):
    transposed1_row = []
    for row in matrix:
	    transposed1_row.append(row[i])
    transposed1.append(transposed1_row)
print(transposed1)
'''

#del语句

#使用 del 语句可以从一个列表中依索引而不是值来删除一个元素。这与使用 pop() 返回一个值不同。
#可以用 del 语句从列表中删除一个切割，或清空整个列表（我们以前介绍的方法是给该切割赋一个空列表）。
#例如：
#也可以用del删除实体变量
'''
a = [3, 6, 7, -8, 8, 4, 1, 0, 5]
del a[0]
print(a)
del a[3:5]
print(a)
del a[:]
print(a,"这是一个空列表")
'''


#元组和序列
'''
t = 12345, 54321, 'hello'
print(t[0])
print(t)
u = t, (3,3,3,3,3)
print(u)
'''

#集合
#集合是一个无序不重复元素的集。基本功能包括关系测试和消除重复元素。
#可以用大括号({})创建集合。注意：如果要创建一个空集合，你必须用 set() 而不是 {} ；后者创建一个空的字典，
#下一节我们会介绍这个数据结构。
#以下是一个简单的演示：
'''
basket = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}
print(basket)
if 'orange' in basket:
    print("basket have orange")
if 'crabgrass' in basket:
    print("basket have crabgrass")
else:
    print("basket have not crabgrass") 
'''

#以下演示了两个集合的操作
'''
a = set('abracadabra')
b = set('alacazam')
print(a - b)		# 在 a 中的字母，但不在 b 中
print(a | b)		# 在 a 或 b 中的字母
print(a & b)		# 在 a 和 b 中都有的字母
print(a ^ b)		 # 在 a 或 b 中的字母，但不同时在 a 和 b 中

#集合也支持推导式：

a = {x for x in 'abracadabra' if x not in 'abcd'}
print(a)
'''

#字典
#另一个非常有用的 Python 内建数据类型是字典。
#序列是以连续的整数为索引，与此不同的是，字典以关键字为索引，关键字可以是任意不可变类型，通常用字符串或数值。
#理解字典的最佳方式是把它看做无序的键=>值对集合。在同一个字典之内，关键字必须是互不相同。  
#一对大括号创建一个空的字典：{}。
#这是一个字典运用的简单例子：
'''
tel = {'jack':4098, 'sape':4013}
tel['guido'] = 4214
print(tel)
print(tel['jack'])
del tel['sape']
tel['irv'] = 4421
print(tel)
print(list(tel.keys()))
print(sorted(tel.keys()))
print('guido' in tel)
'''


#构造函数 dict() 直接从键值对元组列表中构建字典。如果有固定的模式，列表推导式指定特定的键值对：
'''
print(dict([('sace',4154), ('jack',4331), ('guido',4514)]))
print(dict(sace=4154, jack=4331, guido=4514))
print({x: x**2 for x in (2, 4, 6)})
'''

#在字典中遍历时，关键字和对应的值可以使用 items() 方法同时解读出来：
'''
knights = {'gallahad': 'the pure', 'robin': 'the brave'}
for k,v in knights.items():
    print(k,v)
'''

#在序列中遍历时，索引位置和对应值可以使用 enumerate() 函数同时得到：
'''
for i, v in enumerate(['tic', 'tac', 'toe']):
    print(i,v)
'''

#同时遍历两个或更多的序列，可以使用 zip() 组合：
'''
questions = ['name', 'quest', 'favorite color']
answers = ['lancelot', 'the holy grail', 'blue']
print(a)
for q, a in zip(questions, answers):
    print('What is your {0}?  It is {1}.'.format(q, a))
'''
	
#要反向遍历一个序列，首先指定这个序列，然后调用 reversed() 函数：
'''
for i in reversed(range(1, 10, 2)):
    print(i)
'''


#Python3模块
'''
import sys

print('命令行参数如下:')
for i in sys.argv:
   print(i)

print('\n\nPython 路径为：', sys.path, '\n')	
'''
#1、import sys 引入 python 标准库中的 sys.py 模块；这是引入某一模块的方法。
#2、sys.argv 是一个包含命令行参数的列表。
#3、sys.path 包含了一个 Python 解释器自动查找所需模块的路径的列表。


#一个模块只会被导入一次，不管你执行了多少次import。这样可以防止导入模块被一遍又一遍地执行
'''
import support
support.print_func("Fan Dongshan")
'''
'''
import fibo

fibo.fib(1000)
print(fibo.fib2(100))
'''
'''
from fibo import fib,fib2
fib(1000)
print(fib2(100))
'''
'''
from fibo import *
fib(1000)
print(fib2(100))
'''

#__name__属性
#内置的函数 dir() 可以找到模块内定义的所有名称。以一个字符串列表的形式返回:
































