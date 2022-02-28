# print(divmod(7, 4))
#
# print(divmod(23, 5))
#
# print(23//5)
#
# print(type(divmod(8.0, 2.5)))
#
# quot, rem = divmod(23, 10)
#
# print(quot)
# print(rem)

# side1 = float(input('한 변의 길이를 입력하라: '))
# side2 = float(input('다른 한 변의 길이를 입력하라: '))
# hyp = ((side1 * side1) + (side2 * side2)) ** 0.5
# print('빗변의 길이는 다음과 같다:', hyp)

# def add(a, b):
#     return a + b

# print(add(3, 4))
#
# print(add([1,2,3], [4,5,6]))
#
# print(add("가나다","라마바사"))

# f = add #함수를 변수에 대입해서 사용할 수 있다.
# print(f(4, 5))
#
# print(f)
#
# print(f is add)
#

#함수의 몸체에는 최소한 한개 이상의 statement가 존재해야 함
#그러므로, 아무런 내용이 없는 몸체를 지닌 함수를 만들 때에는 pass 라는 키워드를 몸체에 적어주어야 함
# def simple():
#     pass
#
# print(simple())

#인자의 디폴트 값을 지정할 수 있다.
# def incr(x, y=1):
#     return x + y
#
# print(incr(5))
#
# print(incr(5, 10))

#두 개 이상의 값을 동시에 반환할 수 있다, 튜플의 형태로 값을 반환한다
# def calc(x, y):
#     return x + y, x - y, x * y, x / y
#
# print(calc(10, 2))

# def f1(b):
#     b = 100
#
# a = 200
# f1(a)
# print(a)
#
# def f2(b):
#     b = "abc"
#
# a = "def"
# f2(a)
# print(a)

#위의 정수, 튜플, 문자열은 함수인자의 변경이 불가능한 객체이기 때문에 의미없는 함수가 되지만
#아래와 같이 리스트와 사전은 함수인자의 변경이 가능하기 때문에 객체의 내용이 수정이 된다.

# def f4(b):
#     b[1] = 10
#
# a = [4,5,6]
# f4(a)
# print(a)
#
# def f5(b):
#     b['a'] = 10
#
# a = {"a":1, "b":2}
# f5(a)
# print(a)

# def pr_fibo(n):
#     a, b = 1, 0
#     while a < n:
#         print(a, sep=' ')
#         a, b = a + b, a
#
# n = int(input('Input n: '))
# pr_fibo(n)

# age = int(input("몇살임? "))
# if not (12 < age < 20):
#     print('당신은 십대가 아니다.')
# else : print('당신은 십대군요')

# print(True + 1)
# print(False + 1)
# print(False * 75)
# print(True * 75)

# print(bool(0)) # 정수 0은 거짓
# print(bool(1))
# print(bool(100))
# print(bool(-100))
# print()
# print(bool(0.0)) # 실수 0.0은 거짓
# print(bool(0.1))
# print(bool(0.00000000000000000000000000000000000000000001))

# s1 = 'Abe'
# s2 = 'Lincoln'
# s1 = s1 + ' ' + s2
# print(s1)

# a = [1,2,3]
# b = [10, a, 20]
# c = ['x', a, 'y']
#
# print(a)
# print(b)
# print(c)

# grade_dict = { '단아':3.9, '민채':3.9, '예준':2.5 }
# grade_dict['건아'] = 4.0
# print(grade_dict['건아'])
# print(grade_dict)
#
# s = (input('문자열을 입력하라 : ')).split()
# wrd_counter = {}
# for wrd in s:
#     wrd_counter[wrd] = wrd_counter.get(wrd, 0) + 1
# print(wrd_counter)

# setA = {1, 2, 3, 4}
# setB = {3, 4, 5}
# setUnion = setA | setB          # {1, 2, 3, 4, 5}
# setIntersect = setA & setB      # {3, 4}
# setXOR = setA ^ setB            # {1, 2, 5}
# setSub = setA - setB            # {1, 2}
#
# print(setUnion)
# print(setIntersect)
# print(setXOR)
# print(setSub)

# 키워드 인수
# 인수 값 전달 시에 인수 이름과 함께 값을 전달하는 방식을 일컫는다.
# def area(height, width):
#     return height * width
#
# #순서가 아닌 이름으로 값이 전달
# a = area(height='height string ', width=3)
# print(a)
#
# b = area(width=20, height=10)
# print(b)

# 가변 인수 리스트
# 함수 정의시에 일반적인 인수 선언 뒤에 *args 형식의 인수로 가변 인수를 선언할 수 있음
# def myFun(*args):
#     print(type(args), args)
#     print()
#     for arg in args:
#         print(arg)
#
# myFun('Hello', 'Welcome', 'to', 'GeeksforGeeks')

# 함수 호출시 넣어주는 인수 값들 중 일반 인수에 할당되는 값을 제외한 나머지 값들만을 지닌 튜플 객체가 할당된다.
# def varg(a, *args):
#     print(a, args)
#
# varg(1)
# varg(2, 3)
# varg(2, 3, 4, 5, 6)

# C언어의 printf문과 유사한 형태의 printf 정의 방법
# def printf(format, *args):
#     print(format % args)
#
# printf("I've spent %d days and %d night to do this %d", 6, 5, 10)

# The special syntax **kwargs in function definitions in python is used to pass a keyworded, variable-length argument list
# def myFun(**kwargs):
#     print(type(kwargs), kwargs)
#     print()
#     for key, value in kwargs.items():
#         print("{0}: {1}".format(key, value))
#
# myFun(first ='Geeks', mid ='for', last='Geeks')
#
# def myFun(arg1, **kwargs):
#     for key, value in kwargs.items():
#         print ("{0} - {1}: {2}".format(arg1, key, value))
#
# myFun("Hi", first ='Geeks', mid ='for', last='Geeks')

# 함수 호출에 사용될 인수값들이 튜플에 있다면 "*튜플변수"를 이용하여 함수 호출이 가능
# def h(a, b, c):
#     print(a, b, c)
#
# args = (1, 2, 3)
# h(*args)
#
# # 함수 호출에 사용될 인수값들이 사전에 있다면 "**사전변수"를 이용하여 함수 호출이 가능
# def h(a, b, c):
#     print(a, b, c)
#
# dargs = {'aa':1, 'bb':2, 'cc':3}
# h(*dargs) #사전의 키값을 인수로 넣음
#
# dargs = {'a':1, 'b':2, 'c':3}
# h(**dargs)#사전의 값을 인수로 넣음

# def function(**arg):
#     for i in arg:
#         print (i, arg[i])
#
# function(a=1, b=2, c=3, d=4)

# s = 'abcd'
# print(s[::2])   #step:2 - 각 원소들 사이의 거리가 인덱스 기준으로 2가 됨
# print(s[::-1])  #step:-1 - 왼쪽 방향으로 1칸씩

# s = 'abc'
# print(s * 4)
#
# L = [1, 2, 3]
# print(L * 2)

# 문자열은 불변이다
# my_str = '예준아 안녕, 나는 수아야. '
# my_str[0] = '원'                # 에러!

# my_str = '안녕'
# my_str = '안녕하세요'
#
# print(my_str)

# print('\\abc\\')
# print()
# print('abc\tdef\tghi')
# print()
# print('a\nb\nc')

#문자열을 2진수로 변환
# n = int('10001', 2)      # 이진수로 변환
# #n = int('10001', base=2)      # 이진수로 변환
# print(n)

# n1 = int('775', 8)
# n2 = int('1E', 16)
# print('8진수 775와 16진수 1E의 값:', n1, n2)

#casefold는 대문자를 소문자로 바꾸는 역할을 수행한다.
# str = "QWE"
# print(str.casefold())


# print(ord('A'))
# print(chr(65))

#Join을 이용해서 리스트에 특정한 문자를 넣어서 출력이 가능하다
# def print_nice(a_lst):
#     print(', '.join(a_lst))
#
#
# print_nice(['John', 'Paul', 'George', 'Ringo'])

# u = 'spam ham\tegg\ncheese'
# t = u.split()     # 문자열 내의 단어 리스트
# print(t)
# print()
#
# t2 = ':'.join(t)  # 리스트 t 내부의 각 원소들을 ':'로 연결한 문자열 반환
# print(type(t2))   # <type 'str'>
# print(t2)
# print()
#
# t3 = ",".join(t)  # 리스트 t 내부의 각 원소들을 ','으로 연결한 문자열 반환
# print(t3)
# print()
#
# t4 = '\n'.join(t) # 리스트 t 내부의 각 원소들을 '\n'으로 연결한 문자열 반환
# print(t4)
# print()

#문자열 순서 방법
# print(list(reversed('Wow,Bob,wow!')))
# print(sorted('Wow,Bob,wow!'))
#
# a_str = ''.join(reversed('Wow,Bob,wow!'))
# print(a_str)
#
# b_str = ''.join(sorted('Wow,Bob,wow!'))
# print(b_str)


#문자를 대문자로 바꾸는 방법
# my_str = "I'm Henry VIII, I am!"
# new_str = my_str.upper()
# my_str = new_str
# print(my_str)

#문자열의 각 인덱스를 대문자는 소문자로 반대는 반대의 변환을 수행하는 기능
# my_str = "I'm Henry VIII, I am!"
# my_str = my_str.swapcase()
# print(my_str)

# s = 'i like programming, i like swimming.'
# print(s.startswith('i like')) # 'i like'로 시작하는 문자열인지 판단
# print(s.startswith('I like')) # 대소문자 구별
# print()
#
# print(s.endswith('swimming.')) # 'swimming.'로 끝나는 문자열인지 판단
# print(s.startswith('progr', 7)) # 7번째 문자열이 'progr'로 시작하는지 판단
# print()

#Count
# frank_str = 'doo be doo be doo...'
#
# n = frank_str.count('doo')
# print(n)
#
# print(frank_str.count('doo', 1)) 			# 2 출력
# print(frank_str.count('doo', 1, 10)) 		# 1 출력

#find
# s = 'i like programming, i like swimming.'
# print(s.count('like'))       # 'like' 문자열이 출현한 횟수를 반환
# print()
# print(s.find('like'))        # 'like'의 첫글자의 인덱스인 위치(offset)를 반환
# print(s.find('programming')) # 'programming'의 첫글자 위치를 반환
# print(s.find('programmin'))  # 'programmin'의 첫글자 위치를 반환
# print(s.find('programmii'))  # 'programmii' 단어는 없기 때문에 -1 반환
# print()
# print(s.find('like', 3))     # offset=3 부터 'like'을 검색하여 'like'의 첫글자 위치 반환
# print(s.find('my'))          # 'my' 단어는 없기 때문에 -1 반환

#rfind : find를 뒤에서 수행해서 값을 찾는 방법
# frank_str = 'doo be doo be doo...'
# print(frank_str.rfind('doo')) 			# 14 출력

#replace 사용법
# title = '25 Hues of Grey'
# new_title = title.replace('Grey', 'Gray')
# print(new_title)
#
# title = 'Greyer Into Grey'
# new_title = title.replace('Grey', 'Gray')
# print(new_title)

#split 사용법, 리스트로 반환된다.
# stooge_list = 'Moe Larry Curly Shemp'.split()
# print(stooge_list)

#srtip은 지정된 문자를 문자열의 앞뒤에서 지움
# name_str = ' Will Shakes '
# new_str = name_str.strip()
# print(new_str)

#자리맞춤 메서드
# new_str = 'Help!'.center(10, '#')
# print(new_str)
#
# new_str = '750'.rjust(6, '0')
# print(new_str)
#
# new_str = '750'.ljust(6, '0')
# print(new_str)
#
# s = '12'
# print(s.zfill(7))
#
# '-3'.zfill(5)
# '-3'.rjust(5, '0')
#
# number = "-290"
# print(number.zfill(8))
#
# number = "+290"
# print(number.zfill(8))
#
# text = "--random+text"
# print(text.zfill(20))

#remove 메소드
# my_list = [1, 2, 3]
# my_list.remove(1) 	# 변경된 리스트 : [2, 3]
# print(my_list)

#is는 오브젝트의 참조를 비교하기 때문에 값만 같다고 true가 반환되지는 않지만,
# == 는 단지 값만 비교하는 것이다.
# x = [1,2,3]
# y = [1,2,3]
# z = y
#
# print(x == y)
# print(x == z)
# print(x is y)
# print(x is z)
# print(y is z)
#
# print(x[0] == y[0])
# print(x[0] is y[0])

#아래와 같은 방식은 얕은 복사가 일어나기 때문에 원본과 사본에 모두 영향을 끼친다.
# a_list = [2, 5, 10]
# b_list = a_list
# b_list.append(100)
# a_list.append(200)
# b_list.append(1)
# print(a_list)
#
#아래와 같이 값을 복사해서 새로운 리스트를 만드는 방식은 얕은 복사가 일어나지 않는다.(깊은 복사)
# my_list = [1, 10, 5]
# yr_list = my_list[:] 	# member-by-member 복사 수행
# yr_list.append(100)
# print(yr_list)
# print(my_list)

#copy를 import하여 깊은 복사를 하는 방법
# import copy
# 
# a_list = [1, 2, [5, 10]]
# b_list = copy.deepcopy(a_list)     # 깊은 복사로 리스트 생성
# b_list[2][0] = 0
# b_list[2][1] = 0
# print(b_list)


#enumerate를 사용해서 리스트에 인덱스 값을 부여해서 튜플로 반환할 수 있다. -> 사용방법 : enumerate(리스트, 인덱스 시작번호)
# a_list = ['Tom', 'Dick', 'Jane']
# print(list(enumerate(a_list, 1)))
# for item_num, name_str in enumerate(a_list, 1):
#     print(item_num, '. ', name_str, sep='')

#sorted() 내장함수는 L 자체에는 내용 변경 없이 정렬이 되어진 새로운 리스트를 반환한다.
#sorted() 함수의 두번째 인자로 key를 지정하는 함수 할당 가능
#지정된 key 함수가 할당되어 있으면 각 리스트 원소에 대해 기본 비교함수 호출 직전에 key 함수를 먼저 호출한다.

# a_tup = (30, 55, 15, 45)
# print(sorted(a_tup))     #리스트 반환

# L = [ ('lee', 5, 38), ('kim', 3, 28), ('jung', 10, 36)]
#
# def get_key_value(a):
#     return a[1]
#
# print(sorted(L)) #기본적으로는 [][0] 인덱스를 기준으로 정렬이 된다.
# print(L)
#
# print()
#
# print(sorted(L, key=get_key_value)) #하지만 key값으로 각 인덱스의 [1]인덱스를 반환하게 하여서 [][1]을 기준으로 정렬이 되도록 만듦
# print(L)

# L.reverse()도 반환값이 없다.
# 즉, L 자체를 역순으로 뒤집는다. ([주의] 역순 정렬이 아니다.)
# reversed() 내장함수는 sorted() 처럼 내용이 뒤집힌 리스트를 반환한다.
# sorted() 처럼 원래 리스트 내용에는 변함없다.
# a_tup = (1, 3, 5, 0)
# for i in reversed(a_tup):
#     print(i, end=' ')
# print()
# print(tuple(reversed(a_tup)))

# L = ['123', '34', '56', '2345']
# print(sorted(L))
#
# print(sorted(L, key=int)) #리스트의 인덱스를 정수값을 기준으로 정렬하도록 키 값을 부여
#
# print(sorted(L, key=int, reverse=True)) # 리스트의 인덱스를 정수순으로, 내림차 순으로 반환하도록 reverse=True로 부여

#리스트의 가장 뒤 인덱스에 값을 추가하기 위해선 append, 가장 뒤 인덱스에 리스트를 추가하기 위해서는 extend
# a_list = [1, 2, 3]
#
# a_list.append(4)
# a_list.extend([4])          # 윗줄과 똑같이 동작
#
# a_list.extend([4, 5, 6])    # 리스트에 3개 항목 추가
# print(a_list)

#리스트의 insert 함수는 (넣을 위치, 넣을 값)의 형태로 사용한다.
# a_list = [10, 20, 40]   # 30이 없음
# a_list.insert(2, 30)    # 세번째(색인 2)에 30 삽입
# print(a_list)           # [10, 20, 30, 40] 출력
# a_list.insert(100, 33)
# print(a_list)           # [10, 20, 30, 40, 33] 출력
# a_list.insert(-100, 44)
# print(a_list)           # [44, 10, 20, 30, 40, 33] 출력

#remove를 사용하기 위해서는 인덱스를 명시하는게 아니라 값을 명시하는 것이다.
# my_list = [15, 25, 15, 25]
# my_list.remove(25)
# print(my_list) 			# [15, 15, 25] 출력

#리스트의 count는 값을 명시하면 그 값의 수를 정수로 반환
# yr_list = [1, 2, 1, 1,[3, 4]]
# print(yr_list.count(1)) 		# 3 출력
# print(yr_list.count(2)) 		# 1 출력
# print(yr_list.count(3)) 		# 0 출력
# print(yr_list.count([3, 4])) 	# 1 출력

#리스트의 index 함수는 찾고자 하는 값을 입력하면 그 값의 인덱스 번호를 출력한다.
# beat_list = ['John', 'Paul', 'George', 'Ringo']
# print(beat_list.index('Ringo'))

# def ignore_case(s):
#     return s.casefold()
#
# a_list = [ 'john', 'paul', 'George', 'brian', 'Ringo' ]
# b_list = a_list[:]
# a_list.sort()
# print(a_list)
#
# b_list.sort(key=ignore_case)
# print(b_list)

#스택 프로그램 만들기
# the_stack = []
#
#
# def push(v):
#     the_stack.append(v)
#
#
# def pop():
#     return the_stack.pop()
#
#
# def main():
#     s = input('Enter RPN string: ')
#     a_list = s.split()
#
#     for item in a_list:
#
#         if item in '+-*/':
#             op2 = pop()
#             op1 = pop()
#
#             if item == '+':
#                 push(op1 + op2)
#             elif item == '-':
#                 push(op1 - op2)
#             elif item == '*':
#                 push(op1 * op2)
#             else:
#                 push(op1 / op2)
#         else:
#             push(float(item))
#
#     print(pop())
#
#
# main()

#리스트 pop사용
# s = [10, 20, 30, 40, 50]
# print(s.pop(0))   #0 번째 인덱스 값을 꺼낸다.
# 
# print(s)
# 
# print(s.pop(1))   #1 번째 인덱스 값을 꺼낸다.
# 
# print(s)
#
# q = [10, 20, 30, 40, 50]
# q.append(60)
# print(q.pop(0))
#
# print(q)

#reduce 함수 사용방법 functools.reduce(사용하고자 하는 함수, 함수 인자)
# import functools
#
# def add_func(a, b):
#     return a + b
#
# def mul_func(a, b):
#     return a * b
#
# n = 5
# a_list = list(range(1, n + 1))
#
# triangle_num = functools.reduce(add_func, a_list)
# print(triangle_num)
# fact_num = functools.reduce(mul_func, a_list)
# print(fact_num)

#람다함수
# import functools
# my_f = lambda x, y: x + y
# sum1 = my_f(3, 7)
# print(sum1)         # 10 출력
# sum2 = my_f(10, 15)
# print(sum2)         # 25 출력
# t5 = functools.reduce(lambda x, y: x + y, [1,2,3,4,5])
# print(t5)
# f5 = functools.reduce(lambda x, y: x * y, [1,2,3,4,5])
# print(f5)

#람다함수 인자 1개
# f = lambda x: x + 1
# print(f(1))

#람다함수 인자 2개
# g = lambda x, y: x + y
# print(g(1, 2))

#기본인자를 포함한 람다함수
# incr = lambda x, inc = 1: x + inc
# print(incr(10))#inc 기본 인수 값으로 1 사용
# print(incr(10, 5))

#가변인수를 지니는 람다함수
# vargs = lambda x, *args: args
# print(vargs(1, 2, 3, 4, 5))
#
# # 이전 jupyter notebook 참고; "넣어주는 인수 값들 중 일반 인수에 할당되는 값을 제외한 나머지 값들을 지닌 튜플 객체가 할당된다."
# print(type(vargs))
# print(type(vargs(1, 2, 3, 4, 5)))

#람다함수 활용 1. map내장함수
# def f(x):
#     return x * x
#
# X = [1, 2, 3, 4, 5]
# m = map(f, X)
# print(m)
#
# def f(x):
#     return x * x
#
# X = [1, 2, 3, 4, 5]
# Y = list(map(f, X)) #map 형식 같은 경우는 list를 붙여서 출력해야함
#
# print(Y)

#람다함수를 이용해서 map을 사용하는 것이 가장 이상적이다.
# X = [1, 2, 3, 4, 5]
# print(list(map(lambda x: x * x, X)))
#
# Y = list(map(lambda x: x * x + 4 * x + 5, range(10)))
# print(Y)
#
# y = list(map(lambda x: len(x), ["Hello", "Python", "Programming"]))
# print(y)

#filter 내장함수
# print(list(filter(lambda x: x > 2, [1, 2, 3, 34])))
#
# #필터와 람다를 쓰지 않을 경우 아래와 같이 코드가 길어짐
# y = []
# for x in [1, 2, 3, 34]:
#     if x > 2:
#         y.append(x)
# print(y)

# print(list(filter(lambda x: x % 2, [1, 2, 3, 4, 5, 6])))
#
# print(list(filter(lambda x: x % 2 - 1, [1, 2, 3, 4, 5, 6])))
# def F():
#     x = 1
#     print(list(filter(lambda a: a > x, range(-5, 5))))
#
# F()

# print(filter(lambda x: x > 2, [1, 2, 3, 34]))
# print(filter(lambda x: x > 2, (1, 2, 3, 34)))
# print(filter(lambda x: x < 'a', 'abcABCdefDEF'))
# print(list(filter(lambda x: x > 2, [1, 2, 3, 34])))
# print(tuple(filter(lambda x: x > 2, (1, 2, 3, 34))))
# print(list(filter(lambda x: x < 'a', 'abcABCdefDEF')))


#리스트 내포
# mult_list = [ ]
# for i in range(3):
#     for j in range(3):
#         mult_list.append(i * j)
#
# mult_list = [i * j for i in range(3) for j in range(3)]
# my_list = [10, -10, -1, 12, -500, 13, 15, -3]
#
# new_list = []
#
# for i in my_list:
#     if i > 0:
#         new_list.append(i)
#
# new_list = [i for i in my_list if i > 0 ] #리스트 내포의 뒤에 if로 조건을 추가할 수 있다.
#
# my_list = [1, 2, -10, -500, 33, 21, -1]
# neg_list = [i for i in my_list if i < 0 ]
# print(neg_list)

# L = [k * k for k in range(100) if k % 2]   # 홀수의 제곱만 리스트로 형성
# print(L)
#
# seq1 = 'abc'
# seq2 = (1, 2, 3)
# print([(x, y) for x in seq1 for y in seq2])

# L = [(i, j, i*j) for i in range(2, 20, 2) for j in range(3, 20, 3) if (i + j) % 7 == 0]
# print(L)

# words = 'The quick brown fox jumps over the lazy dog'.split()
# stuff = [[w.upper(), w.lower(), len(w)] for w in words]
# for i in stuff:
#     print(i)

# k = [(x,y,z) for x in range(1,30) for y in range(x,30) for z in range(y,30) if x**2 + y**2 == z**2]
# print(k)

#셋 내포
# a_list = [5, 5, 5, -20, 2, -1, 2]
# my_set = set( )
# for i in a_list:
#     if i > 0:
#         my_set.add(i)
# my_set = {i for i in a_list if i > 0}
# print(my_set)
# my_set = {i * i for i in a_list if i > 0}
# print(my_set)

#딕셔너리 내포
# vals_list = [ ('pi', 3.14), ('phi', 1.618) ]
# my_dict = { i[0]: i[1] for i in vals_list }
# print(my_dict)
#
# keys = ['Bob', 'Carol', 'Ted', 'Alice' ]
# vals = [4.0, 4.0, 3.75, 3.9]
# grade_dict = { keys[i]: vals[i] for i in range(len(keys)) }
# print(grade_dict)
#
# grade_dict = { key: val for key, val in zip(keys, vals)}
# print(grade_dict)
#
# phone_dict = {'철수': '000-0000-00000', '영희': '000-1111-00000'}
# idict = {v : k for k, v in phone_dict.items() }
# print(idict)

#리스트 내포로 행렬 만들기
# mat2 = [[[ [0] * 10 for _ in range(10) ]
#                     for _ in range(10) ]
#                     for _ in range(10) ]
# print(mat2)

# a = set([1, 2, 3])
# print(type(a))
# print(a)
# b = set((1, 2, 3))
# print(type(b))
# print(b)
# c = set({'a':1, 'b':2, 'c':3})
# print(type(c))
# print(c)
# d = set({'a':1, 'b':2, 'c':3}.values())
# print(type(d))
# print(d)

# f = {1, 1, 2, 2, 3, 3}
# g = set([1, 1, 2, 2, 3, 3])
# print(f)
# print(g)

# print(set())                         # 빈 set 객체 생성
# print(set([1, 2, 3, 4, 5]))         # 초기 값은 일반적으로 시퀀스 자료형인 리스트를 넣어준다.
# print(set([1, 2, 3, 2, 3, 4]))      # 중복된 원소는 한 나만 저장됨
# print(set('abc'))                  # 문자열은 각 문자를 집합 원소로 지닌다.
# print(set([(1, 2, 3), (4, 5, 6)]))  # 각 튜플은 원소로 가질 수 있음

# print(set([[1, 2, 3], [4, 5, 6]]))  # 변경 가능 자료인 리스트는 집합의 원소가 될 수 없다.
# print(set([{1:"aaa"}, {2:"bbb"}]))  # 변경 가능 자료인 사전도 집합의 원소가 될 수 없다.

# B = set([4, 5, 6, 10, 20, 30])
# C = set([10, 20, 30])
#
# print(C.issubset(B))    # C가 B의 부분집합?
# print(C <= B)
# print(B.issuperset(C))  # B가 C를 포함하는 집합?
# print(B >= C)
# print()
# A = set([1, 2, 3, 4, 5, 6, 7, 8, 9])
# B = set([4, 5, 6, 10, 20, 30])
#
# print(A.union(B)) # A와 B의 합집합
# print(A | B)
# print(A)
# print(A.intersection(B)) # A와 B의 교집합
# print(A & B)
# print(A)
# print(A.difference(B)) # A - B (차집합)
# print(A - B)
# print(A)
# print(A.symmetric_difference(B)) # 베타집합. A와 B의 합집합에서 교집합의 원소를 제외한 집합
# print(A ^ B)
# print(A)
# A = set([1, 2, 3, 4, 5, 6, 7, 8, 9])
# D = A.copy()
# print(D)
# print()
#
# print(A == D) #자료값 비교
# print(A is D) #객체 동등성 비교

# set은 시퀀스 자료형이 아니므로 인덱싱, 슬라이싱, 정렬 등을 지원하지 않는다.
# A = set([1, 2, 3, 4, 5, 6, 7, 8, 9])
# print(A[0])
# print(A[1:4])
# print(A.sort())

# 집합을 리스트나 튜플로 변경가능
# 집합에 인덱싱, 슬라이싱, 정렬 등을 적용하기 위해서는 리스트나 튜플로 변경한다.
# A = set([1, 2, 3, 4, 5, 6, 7, 8, 9])
# print(list(A))
# print(tuple(A))
# # 하지만 집합에 for ~ in 연산은 적용 가능하다.
# A = set([1, 2, 3, 4, 5, 6, 7, 8, 9])
# for ele in A:
#     print(ele,end=" ")

# A = set([1, 2, 3, 4])
# B = set([3, 4, 5, 6])
#
# A.update(B) # A에 B 집합의 원소를 추가 시킴
# print(A)
# A.intersection_update([4,5,6,7,8]) # &=
# print(A)
# A.difference_update([6,7,8]) # -=
# print(A)
# A.symmetric_difference_update([5,6,7]) # ^=
# print(A)
# A.add(8)    # 원소 추가
# print(A)
# A.remove(8) # 원소 제거
# print(A)
# A.remove(10) # 없는 원소를 제거하면 KeyError 발생
# A.discard(10) # remove와 같으나 예외가 발생하지 않음
# A.discard(6)  # 원소 6제거
# print(A)
# A.pop() # 임의의 원소 하나 꺼내기
# print(A)
# A = set([1,2,3,4])
# A.clear() # 모든 원소 없애기
# print(A)

#패킹 언패킹
# tup = 10, 20, 30    # 패킹 (Packing)
# a, b, c = tup       # 언패킹 (Unpacking)
# print(a, b, c) 		# 10, 20, 30 출력

#한 항목만을 가진 튜플 만들기
# my_tup = (3)
# print(type(my_tup))
#
# my_tup = (3,) 	# 한 항목 3을 가진 튜플 만들기
# print(type(my_tup))

# a, *b = 2, 4, 6, 8
# print(a, b)
# a, *b, c = 10, 20, 30, 40, 50
# print(a, b, c)

# big, bigger, *many = 100, 200, 300, 400, 500, 600
# print(big, bigger, many, sep='\n')
#출력
# 100
# 200
# [300, 400, 500, 600]

# my_list = [0] * 10000
# print(len(my_list))

#for문에 else를 사용하는 방법
# def find_divisor(n, max):
#     for i in range(2, max + 1):
#         if n % i == 0:
#             print(i, 'divides evenly into', n)
#             break
#     else:  # break를 만나서 일찍 빠져나오지 않는 한 루프 종료시 수행된다.
#         print('No divisor found')
#
# find_divisor(49, 6)
#
# find_divisor(49, 7)

#isalpha는 문자열이 알파벳으로 이루어졌는지 반환하는 함수
#isalnum은 문자열이 숫자로 이루어져있는지 반환하는 함수

# replace를 사용하여 문자를 제거한다
# s = '1 / 2'
# s = s.replace(' ', '')
# print(s)

# yield 키워드
# return 대신에 yield에 의해 값을 반환하는 함수는 발생자이다.
# yield는 return과 유사하게 임의의 값을 반환하지만 함수의 실행 상태를 보존하면서 함수를 호출한 쪽으로 복귀시켜준다.
# 발생자는 곧 반복자이다!!!
# 즉, 발생자에게 next() 호출이 가능하다.
# def f(a, b):
#     c = a * b
#     d = a + b
#     yield c, d
#
# g = f(1, 2)
#
# x, y = next(g)
# print(x, y)
#
# x, y = next(g)
# print(x, y)

# def f(a, b):
#     for _ in range(2):
#         c = a * b
#         d = a + b
#         yield c, d
#
# g = f(1, 2)
#
# x, y = next(g)
# print(x, y)
#
# x, y = next(g)
# print(x, y)

# 발생자 함수와 일반 함수의 차이점
#
# 일반 함수는 함수가 호출되면 그 함수 내부에 정의된 모든 일을 마치고 결과를 반환함
# 발생자 함수는 함수 내에서 수행 중에 중간 결과 값을 반환할 수 있음
# 발생자가 유용하게 사용되는 경우
#
# 함수 처리의 중간 결과를 다른 코드에서 사용해야 할 경우
# 즉, 모든 결과를 한꺼번에 반환 받는 것이 아니라 함수 처리 중에 나온 중간 결과를 받아서 사용해야 할 경우
# 시퀀스 자료형을 효율적으로 만들고자 하는 경우


def make_evens_gen():
    for n in range(2, 11, 2):
        yield n

# my_gen = make_evens_gen()
# next(my_gen)#2
# next(my_gen)
# next(my_gen)
# my_gen = make_evens_gen()  # 다시 시작
# next(my_gen)
# next(my_gen)
# next(my_gen)
# my_gen = make_evens_gen()  # 다시 시작
# next(my_gen)
# next(my_gen)
# next(my_gen)
# next(make_evens_gen())
# next(make_evens_gen())
# next(make_evens_gen())

#발생자를 사용해서 구현한 피보나치 함수
# def fibonacci(a=1, b=1):
#     while 1:
#         yield a
#         a, b = b, a + b
#
#
# for k in fibonacci():  # 발생자를 직접 for ~ in 구문에 활용
#     if k > 100:
#         break
#     print(k, end=" ")

#발생자를 통해서 홀수 집합 만들기
# def odds(limit=None):
#     k = 1
#     while not limit or limit >= k:
#         yield k
#         k += 2
#
#
# for k in odds(20):
#     print(k, end=" ")
#
#     print()
#
# print(list(odds(20)))  # list() 내장 함수가 발생자를 인수로 받으면 해당 발생자의 next()를 매번 호출하여 각 원소를 얻어온다.

