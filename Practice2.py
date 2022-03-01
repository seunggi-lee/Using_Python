#백분율 기호 연산자(%)를 사용한 포매팅
# a, b, c = 25, 75, 100
# print('%d plus %d equals %d.' % (a, b, c))
#
# n = 25 + 75
# fmt_str = 'The sum is %d.'
# print(fmt_str % n)
#
# n, m = 100, 200
#
# print('n is %d' % n)
# print('n is %d and m is %d' % (n, m))
#
# tup = 10, 20, 30
# print('Answers are %d, %d, and %d.' % tup)

# print('%.4f' % 3.141592)
# print('%.2f' % 3.141592)

#format 함수
# 쉼표(,)
# 숫자 데이터에만 사용
# 문자 데이터에 사용하면 예외 발생
# n = 150000000
# print(format(n, ','))
#
# print(format("대한민국", ',')) # 오류

# 너비
# 기본 자리 맞춤(justification)
# 숫자 데이터: 오른쪽 자리 맞춤
# 문자 데이터: 왼쪽 자리 맞춤
# 너비에 지정된 수치보다 데이터가 더 길면 너비는 자동으로 증가됨
# print(format('Bob', '10'))
# print(format('Suzie', '7'))
# print(format(150, '8'))
# print(format(99, '5'))
# print(format("대한민국", '2'))

# 너비.정밀도
# 정밀도
# 데이터가 일반 숫자인 경우
# 전체 숫자 개수
# 타입_문자 f와 함께 사용
# 소수점 오른쪽에 출력할 숫자의 고정된 자리수 의미
# 데이터가 문자열인 경우
# 전체 문자열의 개수

# print(format('Bobby K.', '6.3'))
# print(format(3.141592, '6.3'))
# print(format(3.141592, '6.3f'))
# print(format(3.141592, '9.3f'))
# print(format(100.7, '9.3f'))
#

# print('{} plus {} equals {}.'.format(25, 75, 100))
# fss = '{} said, I want {} slices of {}.'
#
# name = 'Pythagoras'
# pi = 3.141592
# print(fss.format(name, 2, pi))
# print('Set = {{{}, {}}}'.format(1, 2))
# Set = {1, 2}
# fss = 'Set = {{ {}, {}, {} }}'
# print(fss.format(15, 35, 25))
# print('Set = {{ {}, {}, {} }}'.format(15, 35, 25))

# print('{}; {}; {}!'.format(10, 20, 30))
# print('{0}; {1}; {2}!'.format(10, 20, 30))
# print('The items are {2}, {1}, {0}.'.format(10, 20, 30))
# fss = 'The items are {3}, {1}, {0}.'
# print(fss.format(10, 20, 30, 40))
# fss = 'a equals {a}, b equals {b}, c equals {c}.'
# print(fss.format(a=10, c=100, b=50))
# print('{0}, {0}, {1}, {1}'.format(100, 200))
#
# current_lang = input('한국어를 원하면 KRW를 입력하세요:')
#
# if current_lang == 'KRW':
#     fss = '{0}가 {2}에서 {1}을 만나는 게 언제지?'
# else:
#     fss = "When will {0} meet {1} at {2}'s?"
# print(fss.format('Fred', 'Sam', 'Joe'))

# a_list = [100, 200, 300]
# print('{0[1]:}, {0[2]:}'.format(a_list))
# print('{a[1]:}, {a[2]:}'.format(a=a_list))

# print('{:->24}'.format('Hey Bill G, pick me!'))
# print('{:>7}'.format('Tom')) 		# '    Tom' 출력
# print('{:@>7}'.format('Lady')) 		# '@@@Lady' 출력
# print('{:*>7}'.format('Bill')) 		# '***Bill' 출력
# print('{:<7}'.format('Tom')) 		# 'Tom    ' 출력
# print('{:@<7}'.format('Lady')) 		# 'Lady@@@' 출력
# print('{:*<7}'.format('Bill')) 		# 'Bill***' 출력
# fss = '{:^10}Jones'
# print(fss.format('Tom')) 		# ' Tom Jones' 출력
# fss = '{:@^10}'
# print(fss.format('Lady')) 		# '@@@Lady@@@' 출력
# fss = '{:*^10}'
# print(fss.format('Bill')) 		# '***Bill***' 출력
# print('{:=8}'.format(-1250)) 		# '-   1250' 출력
# print('{:0=8}'.format(-1250)) 		# '-0001250' 출력
# print(format('Lady', '@<7')) 		# 'Lady@@@' 출력
# print('{:@<7}'.format('Lady'))

# pi = 3.14159265
# phi = 1.618
#
# fss = '{:.3f} + {:.3f} = {:.3f}'
# print(fss.format(pi, phi, pi + phi))

# print('{:.5}'.format('Superannuated.'))     # 'Super' 출력
# print('{:.5}'.format('Excellent!'))         # 'Excel' 출력
# print('{:.5}'.format('Sam'))                # 'Sam' 출력
#
# for i in range(2, 10):
#     for j in range(1, 10):
#         print("{0} x {1} = {2:2d}".format(i, j, i*j))
#     print()


#원하는 파일을 읽고자 할 때 예외처리
# try:
#     fname = input('Enter file to read:')
#     f = open(fname, 'r')
#     print(f.read())
# except FileNotFoundError:
#     print('File', fname, 'not found. Terminating.')


#파일을 Open한 이후 올바로 닫지 않고, 자원을 해제하지 않은 상태로 갑자기 종료가 되는 상황 발샐 가능
#파일 I/O를 잘 수행하다가 발생하는 예외 상황, 이때 with구문을 사용한다.
# with open('stock_load.py', 'r') as f:
#     lst = f.readlines()
#     for thing in lst:
#         print(thing, end='')


