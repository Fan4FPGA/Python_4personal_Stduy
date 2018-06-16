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
#一个模块被另一个程序第一次引入时，其主程序将运行。如果我们想在模块被引入时，模块中的某一程序块不执行，
#我们可以用__name__属性来使该程序块仅在该模块自身运行时执行。
# Filename: using_name.py
'''
if __name__ == '__main__':
   print('程序自身在运行')
else:
   print('我来自另一模块')
'''
#说明： 每个模块都有一个__name__属性，当其值是'__main__'时，表明该模块自身在运行，否则是被引入。
#说明：__name__ 与 __main__ 底下是双下划线， _ _ 是这样去掉中间的那个空格。

#内置的函数 dir() 可以找到模块内定义的所有名称。以一个字符串列表的形式返回:
'''
import sys, fibo
print(dir(fibo))
print(dir(sys))
'''
#包是一种管理 Python 模块命名空间的形式，采用"点模块名称"


#rjust()
#ljust()
#center()
#zfill()
#rjust() 方法, 它可以将字符串靠右, 并在左边填充空格。
#还有类似的方法, 如 ljust() 和 center()。 这些方法并不会写任何东西, 它们仅仅返回新的字符串。
#另一个方法 zfill(), 它会在数字的左边填充 0


#str.format()
'''
print('{}网址： "{}!"'.format('4FPGA', 'www.4fpga.cn'))
print('{name}网址： {site}'.format(name='4FPGA', site='www.4fpga.cn'))
print('站点列表 {0}, {1}, 和 {other}。'.format('Google', 'Apple',other='Taobao'))
print('{0} 和 {1}'.format('Google', 'Apple'))
print('{1} 和 {0}'.format('Google', 'Apple'))
'''

#'!a' (使用 ascii()), '!s' (使用 str()) 和 '!r' (使用 repr()) 可以用于在格式化某个值之前对其进行转化:
'''
import math
print('常量PI的近似值位：{}'.format(math.pi))
print('常量PI的近似值位：{!a}'.format(math.pi))
print('常量PI的近似值位：{!s}'.format(math.pi))
print('常量PI的近似值位：{!r}'.format(math.pi))
print('常量PI的近似值位：{:.3f}'.format(math.pi))

table = {'Google': 1, 'Runoob': 2, 'Taobao': 3}
for name ,number in table.items():
    print('{0:10}==>{1:10d}'.format(name,number))

'''

#可选项 ':' 和格式标识符可以跟着字段名。 这就允许对值进行更好的格式化。 下面的例子将 Pi 保留到小数点后三位：
#在 ':' 后传入一个整数, 可以保证该域至少有这么多的宽度。 用于美化表格时很有用。
'''
table = {'Google': 1, 'Runoob': 2, 'Taobao': 3}
print('Runoob: {0[Runoob]:d}; Google: {0[Google]:d}; Taobao: {0[Taobao]:d}'.format(table))
'''

#% 操作符也可以实现字符串格式化。 它将左边的参数作为类似 sprintf() 式的格式化字符串,
#而将右边的代入, 然后返回格式化后的字符串. 例如:
'''
import math
print('常量PI的近视值：%10.4f'%math.pi)
'''


#open() 将会返回一个 file 对象，基本语法格式如下:
#open(filename, mode)
#filename：filename 变量是一个包含了你要访问的文件名称的字符串值。
#mode：mode决定了打开文件的模式：只读，写入，追加等。所有可取值见如下的完全列表。
#这个参数是非强制的，默认文件访问模式为只读(r)。

#模式	描述
#r		以只读方式打开文件。文件的指针将会放在文件的开头。这是默认模式。
#rb		以二进制格式打开一个文件用于只读。文件指针将会放在文件的开头。这是默认模式。
#r+		打开一个文件用于读写。文件指针将会放在文件的开头。
#rb+	以二进制格式打开一个文件用于读写。文件指针将会放在文件的开头。
#w		打开一个文件只用于写入。如果该文件已存在则将其覆盖。如果该文件不存在，创建新文件。
#wb		以二进制格式打开一个文件只用于写入。如果该文件已存在则将其覆盖。如果该文件不存在，创建新文件。
#w+		打开一个文件用于读写。如果该文件已存在则将其覆盖。如果该文件不存在，创建新文件。
#wb+	以二进制格式打开一个文件用于读写。如果该文件已存在则将其覆盖。如果该文件不存在，创建新文件。
#a		打开一个文件用于追加。如果该文件已存在，文件指针将会放在文件的结尾。也就是说，新的内容将会被写入到已有内容之后。如果该文件不存在，创建新文件进行写入。
#ab		以二进制格式打开一个文件用于追加。如果该文件已存在，文件指针将会放在文件的结尾。也就是说，新的内容将会被写入到已有内容之后。如果该文件不存在，创建新文件进行写入。
#a+		打开一个文件用于读写。如果该文件已存在，文件指针将会放在文件的结尾。文件打开时会是追加模式。如果该文件不存在，创建新文件用于读写。
#ab+	以二进制格式打开一个文件用于追加。如果该文件已存在，文件指针将会放在文件的结尾。如果该文件不存在，创建新文件用于读写。

'''
f = open("/G/Python_4personal_Stduy/filewrite.txt", "w")

f.write( "Python 是一个非常好的语言。\n是的，的确非常好!!\n" )
f.write( "Python 是一个非常好的语言。\n是的，的确非常好!!\n" )
# 关闭打开的文件
f.close()
'''

# 打开一个文件
'''
f = open("/G/Python_4personal_Stduy/filewrite.txt", "r")

#str = f.readline()
#print(str)
#str = f.read()
#print(str)
#str = f.readlines()
#print(str)
for line in f:
    print(line, end='')
# 关闭打开的文件
f.close()
'''
'''
f = open("/G/Python_4personal_Stduy/filewrite.txt", "w")
num = f.write( "Python 是一个非常好的语言。\n是的，的确非常好!!\n" )#返回写入的字符数
print(num)
value = ('www.runoob.com', 14)
s = str(value)
f.write(s)
print(f.tell())
 															#返回文件对象当前所处的位置, 它是从文件开头开始算起的字节数。

# 关闭打开的文件
f.close()

#如果要改变文件当前的位置, 可以使用 f.seek(offset, from_what) 函数。
'''



'''
file.close()
关闭文件。关闭后文件不能再进行读写操作。
2
file.flush()
刷新文件内部缓冲，直接把内部缓冲区的数据立刻写入文件, 而不是被动的等待输出缓冲区写入。
3
file.fileno()
返回一个整型的文件描述符(file descriptor FD 整型), 可以用在如os模块的read方法等一些底层操作上。
4
file.isatty()
如果文件连接到一个终端设备返回 True，否则返回 False。
5
file.next()
返回文件下一行。
6
file.read([size])
从文件读取指定的字节数，如果未给定或为负则读取所有。
7
file.readline([size])
读取整行，包括 "\n" 字符。
8
file.readlines([sizeint])
读取所有行并返回列表，若给定sizeint>0，返回总和大约为sizeint字节的行, 实际读取值可能比 sizeint 较大, 因为需要填充缓冲区。
9
file.seek(offset[, whence])
设置文件当前位置
10
file.tell()
返回文件当前位置。
11
file.truncate([size])
从文件的首行首字符开始截断，截断文件为 size 个字符，无 size 表示从当前位置截断；截断之后 V 后面的所有字符被删除，其中 Widnows 系统下的换行代表2个字符大小。
12
file.write(str)
将字符串写入文件，没有返回值。
13
file.writelines(sequence)
向文件写入一个序列字符串列表，如果需要换行则要自己加入每行的换行符。

'''





'''
1
os.access(path, mode)

检验权限模式
2
os.chdir(path)

改变当前工作目录
3
os.chflags(path, flags)

设置路径的标记为数字标记。
4
os.chmod(path, mode)

更改权限
5
os.chown(path, uid, gid)

更改文件所有者
6
os.chroot(path)

改变当前进程的根目录
7
os.close(fd)

关闭文件描述符 fd
8
os.closerange(fd_low, fd_high)

关闭所有文件描述符，从 fd_low (包含) 到 fd_high (不包含), 错误会忽略
9
os.dup(fd)

复制文件描述符 fd
10
os.dup2(fd, fd2)

将一个文件描述符 fd 复制到另一个 fd2
11
os.fchdir(fd)

通过文件描述符改变当前工作目录
12
os.fchmod(fd, mode)

改变一个文件的访问权限，该文件由参数fd指定，参数mode是Unix下的文件访问权限。
13
os.fchown(fd, uid, gid)

修改一个文件的所有权，这个函数修改一个文件的用户ID和用户组ID，该文件由文件描述符fd指定。
14
os.fdatasync(fd)

强制将文件写入磁盘，该文件由文件描述符fd指定，但是不强制更新文件的状态信息。
15
os.fdopen(fd[, mode[, bufsize]])

通过文件描述符 fd 创建一个文件对象，并返回这个文件对象
16
os.fpathconf(fd, name)

返回一个打开的文件的系统配置信息。name为检索的系统配置的值，它也许是一个定义系统值的字符串，这些名字在很多标准中指定（POSIX.1, Unix 95, Unix 98, 和其它）。
17
os.fstat(fd)

返回文件描述符fd的状态，像stat()。
18
os.fstatvfs(fd)

返回包含文件描述符fd的文件的文件系统的信息，像 statvfs()
19
os.fsync(fd)

强制将文件描述符为fd的文件写入硬盘。
20
os.ftruncate(fd, length)

裁剪文件描述符fd对应的文件, 所以它最大不能超过文件大小。
21
os.getcwd()

返回当前工作目录
22
os.getcwdu()

返回一个当前工作目录的Unicode对象
23
os.isatty(fd)

如果文件描述符fd是打开的，同时与tty(-like)设备相连，则返回true, 否则False。
24
os.lchflags(path, flags)

设置路径的标记为数字标记，类似 chflags()，但是没有软链接
25
os.lchmod(path, mode)

修改连接文件权限
26
os.lchown(path, uid, gid)

更改文件所有者，类似 chown，但是不追踪链接。
27
os.link(src, dst)

创建硬链接，名为参数 dst，指向参数 src
28
os.listdir(path)

返回path指定的文件夹包含的文件或文件夹的名字的列表。
29
os.lseek(fd, pos, how)

设置文件描述符 fd当前位置为pos, how方式修改: SEEK_SET 或者 0 设置从文件开始的计算的pos; SEEK_CUR或者 1 则从当前位置计算; os.SEEK_END或者2则从文件尾部开始. 在unix，Windows中有效
30
os.lstat(path)

像stat(),但是没有软链接
31
os.major(device)

从原始的设备号中提取设备major号码 (使用stat中的st_dev或者st_rdev field)。
32
os.makedev(major, minor)

以major和minor设备号组成一个原始设备号
33
os.makedirs(path[, mode])

递归文件夹创建函数。像mkdir(), 但创建的所有intermediate-level文件夹需要包含子文件夹。
34
os.minor(device)

从原始的设备号中提取设备minor号码 (使用stat中的st_dev或者st_rdev field )。
35
os.mkdir(path[, mode])

以数字mode的mode创建一个名为path的文件夹.默认的 mode 是 0777 (八进制)。
36
os.mkfifo(path[, mode])

创建命名管道，mode 为数字，默认为 0666 (八进制)
37
os.mknod(filename[, mode=0600, device])
创建一个名为filename文件系统节点（文件，设备特别文件或者命名pipe）。
38
os.open(file, flags[, mode])

打开一个文件，并且设置需要的打开选项，mode参数是可选的
39
os.openpty()

打开一个新的伪终端对。返回 pty 和 tty的文件描述符。
40
os.pathconf(path, name)

返回相关文件的系统配置信息。
41
os.pipe()

创建一个管道. 返回一对文件描述符(r, w) 分别为读和写
42
os.popen(command[, mode[, bufsize]])

从一个 command 打开一个管道
43
os.read(fd, n)

从文件描述符 fd 中读取最多 n 个字节，返回包含读取字节的字符串，文件描述符 fd对应文件已达到结尾, 返回一个空字符串。
44
os.readlink(path)

返回软链接所指向的文件
45
os.remove(path)

删除路径为path的文件。如果path 是一个文件夹，将抛出OSError; 查看下面的rmdir()删除一个 directory。
46
os.removedirs(path)

递归删除目录。
47
os.rename(src, dst)

重命名文件或目录，从 src 到 dst
48
os.renames(old, new)

递归地对目录进行更名，也可以对文件进行更名。
49
os.rmdir(path)

删除path指定的空目录，如果目录非空，则抛出一个OSError异常。
50
os.stat(path)

获取path指定的路径的信息，功能等同于C API中的stat()系统调用。
51
os.stat_float_times([newvalue])
决定stat_result是否以float对象显示时间戳
52
os.statvfs(path)

获取指定路径的文件系统统计信息
53
os.symlink(src, dst)

创建一个软链接
54
os.tcgetpgrp(fd)

返回与终端fd（一个由os.open()返回的打开的文件描述符）关联的进程组
55
os.tcsetpgrp(fd, pg)

设置与终端fd（一个由os.open()返回的打开的文件描述符）关联的进程组为pg。
56
os.tempnam([dir[, prefix]])

Python3 中已删除。返回唯一的路径名用于创建临时文件。
57
os.tmpfile()

Python3 中已删除。返回一个打开的模式为(w+b)的文件对象 .这文件对象没有文件夹入口，没有文件描述符，将会自动删除。
58
os.tmpnam()

Python3 中已删除。为创建一个临时文件返回一个唯一的路径
59
os.ttyname(fd)

返回一个字符串，它表示与文件描述符fd 关联的终端设备。如果fd 没有与终端设备关联，则引发一个异常。
60
os.unlink(path)

删除文件路径
61
os.utime(path, times)

返回指定的path文件的访问和修改的时间。
62
os.walk(top[, topdown=True[, onerror=None[, followlinks=False]]])

输出在文件夹中的文件名通过在树中游走，向上或者向下。
63
os.write(fd, str)

写入字符串到文件描述符 fd中. 返回实际写入的字符串长度


'''

'''
#GUI

# -*- coding: utf-8 -*-

from tkinter import *
import tkinter.messagebox as messagebox

class Application(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.pack()
        self.createWidgets()

    def createWidgets(self):
        self.nameInput = Entry(self)
        self.nameInput.pack()
        self.alertButton = Button(self, text='Hello', command=self.hello)
        self.alertButton.pack()

    def hello(self):
        name = self.nameInput.get() or 'world'
        messagebox.showinfo('Message', 'Hello, %s' % name)

app = Application()
# 设置窗口标题:
app.master.title('Hello World')
# 主消息循环:
app.mainloop()
'''

'''
for i in range(12):
    print(chr(9800+i),end="")
    print(i)
'''


#字符串的处理方法
'''
“方法”在编程中是一个专有名词
“方法”特指<a>.<b>()风格中的函数<b>()
方法本事也是函数，但是与<a>有关，<a>.<b>风格使用
字符串变量也是<a>，存在一些方法
a是对象，b是对象中的一个功能
'''

#常用的8个字符串操作函数

#str.lower() 或 str.upper() 返回字符串的副本，全部字符大写或小写

'''
a="ABCBDJKDBJ"
print(a)
print(a.lower())
b = a.lower()
print(b.upper())
'''

#str.split(sep=None) 返回一个-列表-，由str根据sep被分隔的部分组成

'''
a = "fds,f,dg,d"
b = a.split(",")
print(b)
'''
#str.count(sub) 函数 返回子串sub在str出现的次数,数据类型为int
'''
a = "gf dg fjdkfj a sdsldfldsassssjjdffdd a a as aa aaa"
b = 10000000 + a.count("a")
print(b)
print(type(a.count("f")))
'''

#str.replace(old,new) 函数,返回字符串str副本，所有old子串都被new替换
'''
a = "afgjdfkljglkfdgjlfka"
print(a.replace("a","-"))
'''

#str.center(width,[fillchar]) 字符串str根据宽度width居中(在n个字符宽度中居中)，fillchar可选
'''
print("Center22".center(20,"="))
'''

#str.strip(chars) 从str中去除在其左侧或右侧chars中列出的字符
'''
a = "  aaaabbbabbbcccc"
print(a.strip(" ac"))
'''
#str.join(iter) 在iter变量除最后一个元素外的每个元素后加一个字符串str
'''
a = "fdsfdgdfgf"
b = ",".join(a)
print(b)
'''
#字符串类型格式化 格式化是对字符串格式表达的方式
'''
字符串格式化使用   .format() 方法
<模板字符串>.format(<逗号分隔的参数>)
'''

#槽
#默认
#  0         1              2                  0       1       2
#“{ }：计算机{ }的CPU占有率为{ }%”.format("2018-6-15"."Forrest",10)
#指定
#  2         0               1                  0       1       2
#“{2}：计算机{0}的CPU占有率为{1}%”.format("2018-6-15"."Forrest",10)

#槽内部对格式化配置方式
#{<参数序号>:<格式控制标记>}
#     ：             填充                对齐                    宽度             ，                       .精度                               l类型
#  引导符号    用于填充单个字符   <左对齐，>右对齐 ^居中对齐  槽的设定输出宽度  数字千分位分隔符  浮点数小数精度或字符串最大输出长度   整数类型b,c,d,o,x,X,浮点数类型e,E,f,%
#前三个一组 填充 对齐 宽度
'''
a = "Python"
print("this is a format test {0:=^20}".format(a))
print("this is a format test {0:=>20}".format(a))
print("this is a format test {0:=<20}".format(a))
'''

#后三个一组
'''
a = 185424.545645
b = 65535
print("this is a format \ntest1:{0:,.2f}\ntest2:{1:,d}\ntest3:0x{1:x}".format(a,b))
'''



#time库是python中处理时间的标准库
#计算机时间的表达
#提供获取系统时间的并格式化输出功能
#提供系统级精确计时功能，用于程序性能分析
#主要包括三类函数
#时间获取：time(),ctime(),gmtime()
#时间格式化并输出：strftime(),strptime()
#程序计时：sleep(),perf_countter()

#time 获取当前时间戳，即计算机内部的时间值，浮点数,很难1790年1月1日点0点0到现在的时间长度
'''
import time
print(str(time.time()))         #浮点数
print(time.ctime())             #字符串
print(time.gmtime())            #计算机可处理的格式
'''

#时间格式化 strftime(tpl,ts)
'''
import time
t = time.gmtime()
print(time.strftime("%Y-%m-%d %H:%M:%S === %B %b %A %a %p" ,t))
'''

#程序计时
#测量时间：perf_counter() 使用的是CPU的时钟，ns级
#产生时间：sleep()
'''
import time
start = time.perf_counter()
time.sleep(1)
end = time.perf_counter()
print(str(end - start))
'''

#时间进度条
'''
import time
scale = 50
print("-----执行开始-----")
for i in range(scale + 1):
    a = '='*i
    b = '*'*(scale - i)
    c = (i/scale)*100
    print("{:^3.0f}%[{}->{}]".format(c,a,b))
    time.sleep(0.1)
print("-----执行结束-----")
'''
#单行刷新
#刷新关键/r
'''
import time
scale = 50
for i in range(scale+1):
    a = "="*i
    b = "*"*(scale - i)
    c = (i/scale)*100
    print("\r{:^3.0f}%[{}->{}]".format(c,a,b),end="")
    time.sleep(0.1)
'''
#进度条完整
'''
import time
scale = 50
print("start".center(58,"-"))
start = time.perf_counter()
for i in range(scale+1):
    a = "="*i
    b = "*"*(scale - i)
    c = (i/scale)*100
    dur = time.perf_counter() - start
    print("\r{:^3.0f}%[{}->{}] {:.2f}s".format(c,a,b,dur),end="")
    time.sleep(0.1)
print("\n"+"end".center(58,"-"))
'''
'''
import time
import math
scale = 50
print("start".center(58,"-"))
start = time.perf_counter()
for i in range(scale+1):
    a = "="*i
    b = "*"*(scale - i)
    c = (i/scale)*100
#    d = c + (1-math.sin(c*math.pi*2+math.pi/2)/-8)
    dur = time.perf_counter() - start
    print("\r{:^3.0f}%[{}->{}] {:.2f}s".format(c,a,b,dur),end="")
    time.sleep(1)
print("\n"+"end".center(58,"-"))

#perf_counter计算程序运行的时间
'''

#单分支结构
#二分支结构
#多分支结构
#条件判断及组合
#程序的异常处理

#单分支
'''
if（条件）：
    语句块
'''

#二分支
'''
if（条件）：
    语句块
else：
    语句块
'''
#紧凑形式
'''
guess = eval(input("pls type number:"))
print("猜{}了".format("对" if guess == 99 else "错"))
'''

#多分支
'''
if（条件）：
    语句块
elif：
    语句块
else：
    语句块
'''
#要注意先后关系以及包含关系



#条件判断和组合
'''
and X 与  or X 或 not X 非；
'''


#程序的异常处理
'''
try：
    语句块1
except NameError：
    语句块2
'''

'''
try:
    num = eval(input("请输入一个整数"))
    print(num**2)
except:
    print("输入的不是一个整数")
'''

'''
try：
    语句块1
except NameError：
    语句块2
else：
    语句块3
finaly：
    语句块4
'''

'''
from math import*
height, weight = eval(input("Enter Height(m) and weight(Kg)[Separated by ',']:"))
bmi = weight / pow(height,2)
print("BMI数值为：{:.2f}".format(bmi))
who = ""
if bmi < 18.5:
    who = "偏瘦"
elif 18.5 <= bmi <25:
    who = "正常"
elif 25 <= bmi < 30:
    who = "偏胖"
else:
    who = "肥胖"
print("BMI指标为：国际'{0}'".format(who))
'''

'''
#from math import*
height, weight = eval(input("Enter Height(m) and weight(Kg)[Separated by ',']:"))
bmi = weight / pow(height,2)
print("BMI数值为：{:.2f}".format(bmi))
who, nat = "",""
if bmi < 18.5:
    who, nat = "偏瘦", "偏瘦"
elif 18.5 <= bmi <24:
    who, nat = "正常", "正常"
elif 24 <= bmi < 25:
    who, nat = "正常", "偏胖"
elif 25 <= bmi < 28:
    who, nat = "偏胖", "偏胖"
elif 28 <= bmi < 30:
    who, nat = "偏胖", "肥胖"
else:
    who, nat = "偏胖", "肥胖"
print("BMI指标为：国际'{0}, 国内'{1}''".format(who,nat))
'''

#遍历循环
#计数循环
'''
for i in range(n):
    语句块
for i in range(3,6)
    print(i)
'''

#while
'''
a = 3
while a > 0:
    a = a - 1
    print(a)
'''

#break 跳出并结束当前整个循环并执行循环后的语句。
#continue 结束当次循环，继续执行后续次数循环。
#都可以搭配while 和 for循环


循环与else
'''
for <> in <> :
    <>
else :
    <>
'''

'''
while <> :
    <>
else :
    <>
'''
#else 作为正常循环完成（没有遇到break）后的奖励

#random库
