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

#casefole는 대문자를 소문자로 바꾸는 역할을 수행한다.
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
new_str = 'Help!'.center(10, '#')
print(new_str)

new_str = '750'.rjust(6, '0')
print(new_str)

new_str = '750'.ljust(6, '0')
print(new_str)

s = '12'
print(s.zfill(7))

'-3'.zfill(5)
'-3'.rjust(5, '0')

number = "-290"
print(number.zfill(8))

number = "+290"
print(number.zfill(8))

text = "--random+text"
print(text.zfill(20))