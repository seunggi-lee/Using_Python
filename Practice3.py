result = 0

# def add(num):
#     global result #전역 변수인 result를 사용하기 위해서 global이라고 명시해준 후 사용
#     result += num
#
# add(3)
# add(4)
# print(result)
#
# def add_a(num):
#     result += num #글로벌 명시 x이기 때문에 에러
#
# add_a(5)

#클래스 사용
# class Calculator:
#     def __init__(self):
#         self.result = 0
#
#     def add(self, num):
#         self.result += num
#
# cal1 = Calculator()
# cal2 = Calculator()
#
# cal1.add(3)
# cal1.add(4)
# cal2.add(3)
# cal2.add(7)

# class Car:
#     accel = 3.0
#     mpg = 25
# car1 = Car()
# car2 = Car()
#
# print('car1.accel = ', car1.accel)
# print('car2.accel = ', car2.accel)
# print('car1.mpg = ', car1.mpg)
# print('car2.mpg = ', car2.mpg)
#
# car1.accel = 3.0
# car2.accel = 3.0
# car1.mpg = 25
# car2.mpg = 25
# my_car = Car()
# yr_car = Car()
# my_car.accel = 5.0
# print(my_car.accel)
# print(yr_car.accel)

#클래스 외부에서 이름 공간에 새로운 이름을 생성 가능하다.
# class S1:
#     a = 1
#
# print(S1.a)
# print()
#
# S1.b = 2 # 클래스 이름 공간에 새로운 이름의 생성
# print(S1.b)
# print()
#
# # print(dir(S1)) # S1에 포함된 이름들을 리스트로 반환
# # del S1.b # 이름 공간 S1에서 b삭제
# # print(dir(S1))
#
# x = S1() # x는 S1의 인스턴스
# print(x.a)
#
# x.a = 10 # 인스턴스 x의 이름 공간에 이름 생성
# print(x.a)
#
# print(S1.a) # 클래스 이름 공간과 인스턴스 이름 공간은 다르다
#
# y = S1() # S1 클래스의 또 다른 인스턴스 생성
#
# y.a = 300 # 인스턴스 y의 이름 공간에 이름 생성
#
# print(y.a)
# print(x.a) # x 인스턴스 공간의 이름 a 확인
# print(S1.a) # 클래스 이름 공간의 a 확인

# class Simple:
#     pass
#
# s1 = Simple()
# s2 = Simple()
# s1.stack = [] # 동적으로 인스턴스 이름 공간 안에 새로운 변수(이름) stack 생성
# s1.stack.append(1) # 값 추가
# s1.stack.append(2)
# s1.stack.append(3)
#
# print(s1.stack)
# print(s1.stack.pop())
# print(s1.stack.pop())
# print()
# print(s1.stack) # 최종 s1.stack값
# print(s2.stack) # s2에는 stack을 정의한 적이 없다.

# class Var:
#     c_mem = 100 # 클래스 멤버 정의
#
#     def f(self):
#         self.i_mem = 200 # 인스턴스 멤버 정의
#
#     def g(self):
#         print(self.i_mem)
#         print(self.c_mem)
#
# print(Var.c_mem)  # 클래스를 통하여 클래스 멤버 접근
# v1 = Var()        # 인스턴스 v1 생성
# print(v1.c_mem)   # 인스턴스를 통하여 클래스 멤버 접근
# v1.f()            # 인스턴스 멤버 i_mem이 생성됨
# print(v1.i_mem)   # 인스턴스 v1을 통하여 인스턴스 멤버 접근
# v2 = Var()       # 인스턴스 v2 생성
# print(v2.c_mem)
# # print(v2.i_mem)   # 인스턴스 v2에는 아직 f() 호출이 안되어서 i_mem 멤버 없음 ==> 생성자의 필요성
#
# print(v1.c_mem)   # 인스턴스 v1을 통해 클래스 멤버 참조
# print(v2.c_mem)   # 인스턴스 v2를 통해 클래스 멤버 참조
#
# print()
# v1.c_mem = 50    # 인스턴스 이름 공간에 c_mem생성
# print(v1.c_mem)   # 인스턴스 v1을 통해 인스턴스 멤버 참조
# print(v2.c_mem)   # 인스턴스 v2을 통해 클래스 멤버참조 (인스턴스 멤버가 없으므로, 클래스 멤버 참조)
# print(Var.c_mem)  # 클래스 멤버참조

# __init__ 메서드와 __new__ 메서드
# class Dog:
#     def __init__(self, name, breed, age):
#         self.name = name
#         self.breed = breed
#         self.age = age
# top_dog = Dog('Handsome Dan', 'Bulldog', 10)
#
# #아래 3줄은 위 코드와 동일함
# top_dog.name = 'Handsome Dan'
# top_dog.breed = 'Bulldog'
# top_dog.age = 10
# good_dog = Dog('WonderBoy', 'Collie', 11)

# __new__()
# 객체에 메모리를 할당(Allocate)하는 것은 __new__() 메소드
# 파이썬에서 객체를 생성할 때 __init__()이 실행되기 직전에 항상 __new__()가 먼저 실행되며 이 때 객체에 메모리가 할당돰

# __init__: 생성자 메소드
#
# 객체가 생성될 때 자동으로 불리어지는 메소드
# 일반적으로 객체가 보유해야 할 변수나 자원들의 초기화하는 코드를 작성함
# self 인자가 정의되어야 함
# __del__: 소멸자 메소드
#
# 객체가 소멸 (메모리에서 해제)될 때 자동으로 불리어지는 메소드
# 일반적으로 객체가 점유하고 있는 메모리나 기타 자원들의 해제하는 코드를 작성함
# self 인자가 정의되어야 함
# 개발자가 특별히 작성하지 않아도 될 메소드
# 이유: 파이썬에서는 객체가 점유하고 있는 메모리나 기타 자원들의 해제가 자동으로 되기 때문에

# from time import ctime, sleep
#
# class Life:
#     def __init__(self):               # 생성자
#         self.birth = ctime()          # 현재시간에 대한 문자열을 얻는다.
#         print('Birthday', self.birth) # 현재 시간 출력
#
#     def __del__(self):                # 소멸자
#         print('Deathday', ctime())    # 소멸 시간 출력
#
# def test():
#     mylife = Life()
#     print('Sleeping for 3 sec')
#     sleep(3) #3초간 sleep(block)상태에 있음 (즉, 3초간 CPU 점유 못함)
#
# test()

# 인자를 받는 생성자 호출 가능
# [참고] __str__: print 예약어나 str() 내장함수 호출에 대응되는 메소드 ->print(인스턴스)를 하면 str에 명시된 방식대로 출력이 된다.
# class Integer:
#     def __init__(self, i):
#         self.i = i
#
#     def __str__(self):
#         return "self.i:" + str(self.i)
#
#
# i = Integer(10)
# print(i)
# print(str(i))

# 문제가 발생하는 코드
# class Marriage:
#     def __init__(self):
#         self.wife = Person('f')
#         self.husband = Person('m')
#
# a_marriage = Marriage()           # Person 클래스 초기화 누락
#
# class Person:
#     def __init__(self, gender):
#         self.gender = gender

# 문제가 발생하는 코드 수정
# class Marriage:
#     def __init__(self):
#         self.wife = Person('f')
#         self.husband = Person('m')
#
#
# class Person:
#     def __init__(self, gender):
#         self.gender = gender
#         self.marriage = Marriage()
#
#
# a_marriage = Marriage()  # 해당 라인을 끝으로 옮김
# 선행 참조에 관한 주요 명심 사항
# 모든 클래스들은 인스턴스화 하기 전에 미리 정의되어 있어야 함
# 클래스 상호 간에 인스턴스화를 하는 것(Mutual dependency)은 금지

# class Pretty:
#     def __init__(self, prefix):
#         self.prefix = prefix
#
#     def print_me(self, a, b, c):
#         print(self.prefix, a, sep='')
#         print(self.prefix, b, sep='')
#         print(self.prefix, c, sep='')
#
#     def print_class():  # 클래스 범위 메소드 (객체로 부터 호출 불가)
#         print("Preedy class")
# printer = Pretty('-->')
# printer.print_me(10, 20, 30)  # 바운드 메소드 호출 (Bound Method Call)
# Pretty.print_me(printer, 10, 20, 30)  # 언바운드 메소드 호출 ( Unbound Method Call)
# # Pretty.print_class()  # 클래스 범위 메소드 (객체로 부터 호출 불가)
# # printer.print_class()

# 파이썬에서 객체 지향 설계는 매우 단순!
# Capsulization (캡슐화)와 대치
# 파이썬에는 public, package, private 등의 키워드 없음
# 클래스 내 존재하는 모든 것이 public
# 한가지 예외: Mangled Member <-- 클래스 내부에서만 접근 가능한 지역 변수/메소드
#
# class Odd:
#     def __init__(self):
#         self.x = 10
#         self.y = 20
#         self._u = 30  # 클래스 정의 내부에서만 사용하는 특수 변수라는 약속. 외부에서 직접 접근하는 것을 하지 말자는 약속. 접근은 허용됨
#         self.__z = 40  # Mangled Member --> 외부에서 접근 불가 ([주의] 메직 메소드 아님!!!)
#
#     def pr(self):
#         print('__z = ', self.__z)
#
#     def __pr(self):
#         print("!!!!!!!!!!!!!")
#
# o = Odd()
# print(o.x)  # 10
# print(o.y)  # 20
# print(o._u)
# print(o.__z)  # 에러!

# 상속의 이유
#
# 코드의 재사용
# 상속받은 자식 클래스는 상속을 해준 부모 클래스의 모든 기능을 그대로 사용
# 자식 클래스는 필요한 기능만을 정의하거나 기존의 기능을 변경(재정의, Override)할 수 있음
# 부모 클래스 메소드 호출 방법
#
# Unbound 메소드 호출
# 부모 클래스.메소드(self, ...)
# Bound 메소드 호출 (더 자주 이용됨)
# super(Subclass, self)
# super()에 대한 자세한 설명

# class Person:
#     def __init__(self, name, phone=None):
#         self.name = name
#         self.phone = phone
#
#     def __str__(self):
#         return '<Person {0} {1}>'.format(self.name, self.phone)
# class Employee(Person):                    # 괄호 안에 쓰여진 클래스는 슈퍼클래스를 의미한다.
#     def __init__(self, name, phone, position, salary):
#         #Person.__init__(self, name, phone) # Person클래스의 생성자 호출 --> Unbound Method Call
#         super(Employee, self).__init__(name, phone)   # --> Bound Method Call
#
#         self.position = position
#         self.salary = salary
#
# p1 = Person('홍길동', 1498)
# print(p1.name)
# print(p1)
#
# print()
#
# m1 = Employee('손창희', 5564, '대리', 200)
# m2 = Employee('김기동', 8546, '과장', 300)
# print(m1.name, m1.position)  # 슈퍼클래스와 서브클래스의 멤버를 하나씩 출력한다.
# print(m1)
# print(m2.name, m2.position)
# print(m2)
#
# l1 = [x for x in dir(p1) if not x.startswith("__")]
# print(l1)
#
# l2 = [x for x in dir(m1) if not x.startswith("__")]
# print(l2)

# 서브 클래스의 생성자는 슈퍼 클래스의 생성자를 자동으로 호출하지 않는다.
# class Super:
#     def __init__(self):
#         print('Super init called')
#
# class Sub(Super):
#     def __init__(self):
#         print('Sub init called')
#
# s = Sub()

# 서브 클래스의 생성자에서 슈퍼 클래스의 생성자를 명시적으로 호출해야 한다.
# class Super:
#     def __init__(self):
#         print('Super init called')
#
# class Sub(Super):
#     def __init__(self):
#         #Super.__init__(self)          # Unbound 방식으로 슈퍼클래스의 생성자를 호출한다.
#         super(Sub, self).__init__()    # 또는 왼쪽처럼 Bound 메소드 호출
#         print('Sub init called')
#
# s = Sub()

# 서브 클래스에 생성자가 정의되어 있지 않은 경우에는 슈퍼 클래스의 생성자가 호출된다.
# class Super:
#     def __init__(self):
#         print('Super init called')
#
# class Sub(Super):
#     pass
#
# s = Sub()

# 메쏘드의 대치 (메소드 오버라이드 - Override)
# 서브 클래스에서 슈퍼 클래스에 정의된 메소드를 재정의하여 대치하는 기능
# class Person:
#     def __init__(self, name, phone=None):
#         self.name = name
#         self.phone = phone
#
#     def __str__(self):
#         return '<Person %s %s>' % (self.name, self.phone)
#
# class Employee(Person):
#     def __init__(self, name, phone, position, salary):
#         #Person.__init__(self, name, phone)
#         super(Employee, self).__init__(name, phone)
#         self.position = position
#         self.salary = salary
#
# p1 = Person('gslee', 5284)
# m1 = Employee('kslee', 5224, 'President', 500)
#
# print(p1)
# print(m1)

# class Employee(Person):
#     def __init__(self, name, phone, position, salary):
#         #Person.__init__(self, name, phone)
#         super(Employee, self).__init__(name, phone)
#         self.position = position
#         self.salary = salary
#
#     def __str__(self):
#         return '<Employee %s %s %s %s>' % (self.name, self.phone, self.position, self.salary)
#
# p1 = Person('gslee', 5284)
# m1 = Employee('kslee', 5224, 'President', 500)
#
# print(p1)
# print(m1)

# 다형성(Polymorphism)
# 상속 관계 내의 다른 클래스들의 인스턴스들이 같은 멤버 함수 호출에 대해 각각 다르게 반응하도록 하는 기능
# 연산자 오버로딩(Operator Overloading)도 다형성과 관련된 중요한 기술
# 연산자 오버로딩: a와 b의 객체 형에 따라 a + b의 + 연산자 행동 방식이 변경되는 것
# 다형성의 장점
# 적은 코딩으로 다양한 객체들에게 유사한 작업을 수행시킬 수 있음
# 일관된 코딩 방식이 유지됨
# 프로그램 작성 코드 량이 줄어든다.
# 코드의 가독성을 높혀준다
# 파이썬에서 다형성의 장점
# 형 선언이 없다는 점에서 파이썬에서는 다형성을 적용하기가 더욱 용이하다.
# 실시간으로 객체의 형이 결정 => 하나의 메소드에 연관시킬 수 있는 객체의 종류에 제한이 없다.
# 즉, 상속 관계등의 클래스 간의 관계 설정 필요 없이 다형성 적용 가능
# class Animal:
#     def cry(self):
#         print('...')
#
# class Dog(Animal):
#     def cry(self):
#         print('멍멍')
#
# class Duck(Animal):
#     def cry(self):
#         print('꽥꽥')
#
# class Fish(Animal):
#     pass
#
# for each in (Dog(), Duck(), Fish()):
#     each.cry()

# 내장 자료형(list, dict, tuple, string)을 상속하여 사용자 클래스를 정의하는 것
# 내장 자료형과 사용자 자료형의 차이를 없에고 통일된 관점으로 모든 객체를 다룰 수 있는 방안
# 클래스 정의는 새로운 자료형의 정의임
# class MyList(list):
#     def __sub__(self, other):   # '-' 연산자에 대응되는 함수 정의
#         for x in other:
#             if x in self:
#                 self.remove(x)     # 각 항목을 하나씩 삭제한다.
#         return self
#
# L = MyList([1, 2, 3, 'spam', 4, 5])
# print(L)
# print()
#
# L = L - ['spam', 4]
# print(L)

# class Stack(list):  # 클래스 정의
#     def push(self, other):
#         self.append(other)
#
# s = Stack()         # 인스턴스 생성
#
# s.push(4)
# s.push(5)
# print(s)
# print()
#
# s = Stack([1,2,3])
# s.push(4)
# s.push(5)
# print(s)
# print()
#
# print(s.pop())       # 슈퍼 클래스인 리스트 클래스의 pop() 메소드 호출
# print(s.pop())
# print(s)

# class Stack(list):  # 클래스 정의
#     push = list.append
#
# s = Stack()         # 인스턴스 생성
#
# s.push(4)
# s.push(5)
# print(s)
# print()
#
# s = Stack([1,2,3])
# s.push(4)
# s.push(5)
# print(s)
# print()
#
# print(s.pop())       # 슈퍼 클래스인 리스트 클래스의 pop() 메소드 호출
# print(s.pop())
# print(s)

# class Queue(list):
#     def enqueue(self, obj):
#         self.append(obj)
#
#     def dequeue(self):
#         return self.pop(0)
#
#
# q = Queue()
# q.enqueue(1)  # 데이터 추가
# q.enqueue(2)
# print(q)
#
# print(q.dequeue())  # 데이터 꺼내기
# print(q.dequeue())
#
#
# class Queue(list):
#     enqueue = list.append
#
#     def dequeue(self):
#         return self.pop(0)
#
#
# q = Queue()
# q.enqueue(1)  # 데이터 추가
# q.enqueue(2)
# print(q)
#
# print(q.dequeue())  # 데이터 꺼내기
# print(q.dequeue())

# class MyDict(dict):
#     def keys(self):
#         K = list(dict.keys(self)) # 언바운드 메소드 호출 --> K = list(self.keys()) 라고 호출하면 무한 재귀 호출
#         K.sort()
#         return K
#
# d = {'b':1, 'c':2, 'a':3}
# print(d.keys())
# print(list(d.keys()))
# print()
#
# d2 = MyDict({'b':1, 'c':2, 'a':3})
# print(d2.keys())
#
# class MyDict(dict):
#     def keys(self):
#         K = list(super().keys()) # 바운드 메소드 호출
#         K.sort()
#         return K
#
# d = {'b':1, 'c':2, 'a':3}
# print(d.keys())
# print(list(d.keys()))
# print()
#
# d2 = MyDict({'b':1, 'c':2, 'a':3})
# print(d2.keys())

# 객체가 어떤 클래스에 속해 있는지 확인하기
# print(int)
#
# # 객체의 자료형 비교 방법 I (전통적 방법)
# print(type(123) == int)
# print(type(123) == type(0))
# a = 12345678
# print(type(a) == type(0))
#
# # 객체의 자료형 비교 방법 II (새로운 방법)
# # isinstance() 내장 함수와 기본 객체 클래스 사용
# print(isinstance(123, int))

# 서브 클래스의 인스턴스는 슈퍼 클래스의 인스턴스이기도 하다.
# class A:
#     pass
#
# class B:
#     def f(self):
#         pass
#
# class C(B):
#     pass
#
# def check(obj):
#     print(obj, '=>', end=" ")
#     if isinstance(obj, A):
#         print('A', end="")
#     if isinstance(obj, B):
#         print('B', end="")
#     if isinstance(obj, C):
#         print('C', end="")
#     print()
#
# a = A()
# b = B()
# c = C()
#
# check(a)
# check(b)
# check(c)

# 클래스 간의 상속 관계 알아내기
# issubclass() 내장 함수 활용
# class A:
#     pass
#
# class B:
#     def f(self):
#         pass
#
# class C(B):
#     pass
#
# def check(class_obj):
#     print(class_obj, '=>', end=" ")
#     if issubclass(class_obj, A):
#         print('A', end="")
#     if issubclass(class_obj, B):
#         print('B', end="")
#     if issubclass(class_obj, C):
#         print('C', end="")
#     print()
#
# check(A)
# check(B)
# check(C)

# 다중상속(Multiple Inheritance)
# class Mammal:
#     def __init__(self, name, size):
#         self.name = name
#         self.size = size
#
#     def speak(self):
#         print("My name is", self.name)
#
#     def call_out(self):
#         self.speak()
#         self.speak()
#         self.speak()
#
#
# class Pet:
#     pass
#
#
# class Carnivore:
#     pass
#
#
# class Dog(Mammal, Pet, Carnivore):
#     def __init__(self, name, size, breed):
#         Mammal.__init__(self, name, size)  # 원하는 상위 클래스 생성자만 선택하여 호출
#         self.breed = breed
#
#     def speak(self):
#         print('ARF!')
#
#
# dog = Dog("jack", 10, True)
# dog.speak()
# print(dog.size)
# print("#" * 10)
# dog.call_out()

# class Pet:
#     def __init__(self, nickname):
#         self.nickname = nickname
#
# class Dog(Mammal, Pet, Carnivore):
#     def __init__(self, name, size, nickname, breed):
#         Mammal.__init__(self, name, size) # 원하는 상위 클래스 생성자만 선택하여 호출
#         Pet.__init__(self, nickname)      # 원하는 상위 클래스 생성자만 선택하여 호출
#         self.breed = breed
#
#     def speak(self):
#         print('ARF!')
# dog = Dog("jack", 10, "jackjack", True)
# dog.speak()
# print(dog.nickname)
# print("#" * 10)
# dog.call_out()

# class A:
#     def __init__(self):
#         print("Class A __init__()")
#
# class B(A):
#     def __init__(self):
#         print("Class B __init__()")
#         A.__init__(self)
#
# class C(A):
#     def __init__(self):
#         print("Class C __init__()")
#         A.__init__(self)
#
# class D(B, C):
#     def __init__(self):
#         print("Class D __init__()")
#         B.__init__(self)
#         C.__init__(self)
#
# d = D()
#
# class A:
#     def __init__(self):
#         print("Class A __init__()")
#
# class B(A):
#     def __init__(self):
#         print("Class B __init__()")
#         super().__init__()
#
# class C(A):
#     def __init__(self):
#         print("Class C __init__()")
#         super().__init__()
#
# class D(B, C):
#     def __init__(self):
#         print("Class D __init__()")
#         super().__init__()
#
# d = D()
# print(D.mro())
#
# class A:
#     def __init__(self):
#         print("Class A __init__()")
#
# class B(A):
#     def __init__(self):
#         print("Class B __init__()")
#         super(B, self).__init__()
#
# class C(A):
#     def __init__(self):
#         print("Class C __init__()")
#         super(C, self).__init__()
#
# class D(B, C):
#     def __init__(self):
#         print("Class D __init__()")
#         super(D, self).__init__()
#
# d = D()
# print(D.mro())

# 비교 메서드
# class Dog:
#     def __init__(self, n):
#         self.n = n
#
#     def __eq__(self, other):
#         ''' == 를 구현하면 != 를 무료로 얻는다.'''
#         return self.n == other.n
#
#     def __lt__(self, other):
#         '' '< 를 구현하면 > 를 무료로 얻는다.'''
#         return self.n < other.n
#
#     def __le__(self, other):
#         ''' <= 를 구현하면, >= 를 무료로 얻는다.'''
#         return self.n <= other.n

# a = Dog(10)
# b = Dog(100)
# print(a == b, a != b)
# print(a < b, a > b)
# print(a <= b, a >= b)

# class Dog:
#     def __init__(self, d):
#         self.d = d
#
#     def __gt__(self, other):
#         '''
#         Greater than (>).
#         '''
#         print("__gt__() is called !!!!!!!!!!!")
#         if type(other) == Dog:
#             return self.d > other.d
#         else:
#             return self.d > other
#
#     def __lt__(self, other):
#         '''
#         Less than (<).
#         '''
#         print("__lt__() is called !!!!!!!!!!!")
#         if type(other) == Dog:
#             return self.d < other.d
#         else:
#             return self.d < other
#
#     #  _ _repr_ _ 정의하는 것은  _ _str_ _도 갖게 되는 것이다.
#     def __repr__(self):
#         return "Dog(" + str(self.d) + ")"
# d1 = Dog(1)
# d2 = Dog(10)
# d3 = 2
# print(d1 < d2)
# print(d1 < d3)
# print(d2 < d1)
# print(d3 < d1)
# print(d1)
# d1, d5, d10 = Dog(1), Dog(5), Dog(10)
# a_list = [50, d5, 100, d1, -20, d10, 3]
# a_list.sort()
# print(a_list)

# 산술(Arithmetic) 연산자 메서드
# import fractions
#
# f = fractions.Fraction(1, 2)
# print(f + 1)  # Fraction._ _add_ _ 호출
# print(2 + f)  # Fraction._ _radd_ _ 호출
#
#
# class Point:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#
#     def __add__(self, other):
#         ''' self+other를 포함한 포인트 반환.'''
#         newx = self.x + other.x
#         newy = self.y + other.y
#         return Point(newx, newy)
#
#     def __sub__(self, other):
#         ''' 두 포인트의 거리 반환.'''
#         dx = self.x - other.x
#         dy = self.y - other.y
#         return (dx * dx + dy * dy) ** 0.5
#
#     def __mul__(self, n):
#         ''' point 곱하기 스칼라 숫자 n.'''
#         newx = self.x * n
#         newy = self.y * n
#         return Point(newx, newy)
#
#     def __str__(self):
#         return "Point({0}, {1})".format(self.x, self.y)
#
#
# pt1 = Point(10, 15)
# pt2 = Point(0, 5)
# x = pt1 + pt2
# print(x)

# 단항(Unary) 산술 연산자
# class Point:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#
#     def __add__(self, other):
#         ''' self+other를 포함한 포인트 반환.'''
#         newx = self.x + other.x
#         newy = self.y + other.y
#         return Point(newx, newy)
#
#     def __sub__(self, other):
#         ''' 두 포인트의 거리 반환.'''
#         dx = self.x - other.x
#         dy = self.y - other.y
#         return (dx * dx + dy * dy) ** 0.5
#
#     def __mul__(self, n):
#         ''' point 곱하기 스칼라 숫자 n.'''
#         newx = self.x * n
#         newy = self.y * n
#         return Point(newx, newy)
#
#     def __neg__(self):
#         newx = -self.x
#         newy = -self.y
#         return Point(newx, newy)
#
#     __invert__ = __neg__
#
#     def __trunc__(self):
#         newx = self.x.__trunc__()
#         newy = self.y.__trunc__()
#         return Point(newx, newy)
#
#     def __str__(self):
#         return "Point({0}, {1})".format(self.x, self.y)
#
#
# pt1 = Point(3, 4)
# pt2 = -pt1
# pt3 = ~pt1
# print(pt2.x, ', ', pt2.y, ', ', pt3.y, sep='')
#
# import math
#
# pt1 = Point(5.5, -6.6)
# pt2 = math.trunc(pt1)
# print(pt2.x, ', ', pt2.y, sep='')

# __iter__와 __next__ 구현하기
# class Stack:
#     def __init__(self):
#         self.mylist = []  # Containment는 여기서 사용된다!
#
#     def append(self, v):
#         self.mylist.append(v)
#
#     def push(self, v):
#         self.mylist.append(v)
#
#     def pop(self):
#         return self.mylist.pop()
#
#     def peek(self):
#         return self.mylist[-1]
#
#     def __len__(self):
#         return len(self.mylist)
#
#     def __contains__(self, v):
#         return self.mylist.__contains__(v)
#
#     def __getitem__(self, k):
#         return self.mylist[k]
#
#     def __iter__(self):
#         self.current = 0
#         return self
#
#     def __next__(self):
#         if self.current < len(self):
#             self.current += 1
#             return self.mylist[self.current - 1]
#         else:
#             raise StopIteration

# class Seq:
#     def __init__(self, file):
#         self.file = open(file)
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         line = self.file.readline()  # 한 라인을 읽는다.
#         if not line:
#             raise StopIteration  # 읽을 수 없으면 예외 발생
#         return line  # 읽은 라인을 리턴한다.
#
#
# s = Seq('readme.txt')  # s 인스턴스가 next() 메소드를 지니고 있으므로 s 인스턴스 자체가 반복자임
#
# for line in s:  # 우선 __iter__() 메소드를 호출하여 반복자를 얻고, 반복자에 대해서 for ~ in 구문에 의하여 __next__() 메소드가 호출됨
#     print(line)
#
# print()
#
# print(Seq('readme.txt'))
#
# # list() 내장 함수가 객체를 인수로 받으면 해당 객체의 반복자를 얻어와 next()를 매번 호출하여 각 원소를 얻어온다.
# print(list(Seq('readme.txt')))
#
# # tuple() 내장 함수가 객체를 인수로 받으면 해당 객체의 반복자를 얻어와 next()를 매번 호출하여 각 원소를 얻어온다.
# print(tuple(Seq('readme.txt')))

# 클래스 내 연산자 중복 (Operator Overloading) 정의
# class MyInteger: #올바르지 못한 코드
#     def __init__(self, i):
#         self.i = i
#
#     def __str__(self):
#         return str(self.i)
#
#     def __add__(self, other):
#         return self.i + other
#
#     def __sub__(self, other):
#         return self.i - other
#
#     def __mul__(self, other):
#         return self.i * other
#
#
# i = MyInteger(10)
# print(i)
# print(str(i))
#
# print()
# i = i + 10
# print(i)
#
# print()
# i += 10
# print(i)
#
# print()
# i += 15
# print(i)
#
# print()
# i *= 10
# print(i)

# class MyInteger2: #이와 같이 써줘야함
#     def __init__(self, i):
#         self.i = i
#
#     def __str__(self):
#         return str(self.i)
#
#     def __add__(self, other):
#         return MyInteger2(self.i + other)
#
#     def __sub__(self, other):
#         return MyInteger2(self.i - other)
#
#     def __mul__(self, other):
#         return MyInteger2(self.i * other)
#
#
# i = MyInteger2(10)
# print(i)
# print(str(i))
#
# print()
# i = i + 10
# print(i)
#
# print()
# i += 10
# print(i)
#
# print()
# i += 15
# print(i)
#
# print()
# i *= 10
# print(i)

# class MyInteger:
#     def __init__(self, i):
#         self.i = i
#
#     def __gt__(self, y):
#         return self.i > y
#
#     def __ge__(self, y):
#         return self.i >= y
#
#     def __lt__(self, y):
#         return self.i < y
#
#     def __le__(self, y):
#         return self.i <= y
#
#     def __eq__(self, y):
#         return self.i == y
#
#     def __ne__(self, y):
#         return self.i != y
#
# c = MyInteger(10)
# print(c > 1)
# print(c >= 1)
# print(c < 1)
# print(c <= 1)
# print()
# print(c == 1)
# print(c != 1)

# class MyInteger:
#     def __init__(self, i):
#         self.i = i
#
#     def __gt__(self, y):
#         if isinstance(y, MyInteger):
#             return self.i > y.i
#         elif isinstance(y, int):
#             return self.i > y
#         else:
#             return False
#
#     def __ge__(self, y):
#         if isinstance(y, MyInteger):
#             return self.i >= y.i
#         elif isinstance(y, int):
#             return self.i >= y
#         else:
#             return False
#
#     def __lt__(self, y):
#         if isinstance(y, MyInteger):
#             return self.i < y.i
#         elif isinstance(y, int):
#             return self.i < y
#         else:
#             return False
#
#     def __le__(self, y):
#         if isinstance(y, MyInteger):
#             return self.i <= y.i
#         elif isinstance(y, int):
#             return self.i <= y
#         else:
#             return False
#
#     def __eq__(self, y):
#         if isinstance(y, MyInteger):
#             return self.i == y.i
#         elif isinstance(y, int):
#             return self.i == y
#         else:
#             return False
#
#     def __ne__(self, y):
#         if isinstance(y, MyInteger):
#             return self.i != y.i
#         elif isinstance(y, int):
#             return self.i != y
#         else:
#             return False
#
# c = MyInteger(10)
# d = MyInteger(100)
# e = 50
#
# print(c > d)
# print(c >= d)
# print()
#
# print(c > e)
# print(c >= e)
# print()
#
# print(c < d)
# print(c <= d)
# print()
#
# print(c < e)
# print(c <= e)
# print()
#
# print(c == d)
# print(c != d)
# print()
#
# print(c == e)
# print(c != e)

# 문자열로 변환하기
# 1) __repr__
#
# 객체를 대표하여 유일하게 표현할 수 있는 공식적인 문자열
# eval() 함수에 의하여 같은 객체로 재생성 될 수 있는 문자열 표현
#
# 2) __str__
#
# 객체의 비공식적인 문자열 표현
# 사용자가 보기 편한 형태로 자유롭게 표현될 수 있음

# class StringRepr:
#     def __repr__(self):
#         return 'repr called'
#
#     def __str__(self):
#         return 'str called'
#
# s = StringRepr()
# print(s)
# print(str(s))
# print(repr(s))
#
# __str__() 호출시
# __str__()가 정의되어 있지 않으면 __repr__()이 대신 호출됨
# class StringRepr:
#     def __repr__(self):
#         return 'repr called'
#
# s = StringRepr()
# print(s)
# print(str(s))
# print(repr(s))

# __repr__() 호출시
# __repr__()이 정의되어 있지 않으면 객체 식별자가 출력됨
# 대신하여 __str__()이 호출되지 않음
#
# class StringRepr:
#     def __str__(self):
#         return 'str called'
#
# s = StringRepr()
# print(s)
# print(str(s))
# print(repr(s))

