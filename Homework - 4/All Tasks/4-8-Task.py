# -*- coding: utf-8 -*-
"""
Created on Mon Nov 22 15:32:04 2021

@author: Zokirkhon
Homework - 4.8
"""


"""
Task: Describe an abstract method.

직무: 추상메소드를 설명하시오.
"""


"""
English:

Abstract Classes in Python
An abstract class can be considered as a blueprint for other classes. 
It allows you to create a set of methods that must be created within 
any child classes built from the abstract class. A class which contains 
one or more abstract methods is called an abstract class. 
An abstract method is a method that has a declaration but 
does not have an implementation. 
While we are designing large functional units we use an abstract class. 
When we want to provide a common interface for different 
implementations of a component, we use an abstract class.

Why use Abstract Base Classes : 
By defining an abstract base class, 
you can define a common Application Program Interface(API) 
for a set of subclasses. This capability is especially useful 
in situations where a third-party is going to provide implementations, 
such as with plugins, but can also help you when working in a large 
team or with a large code-base where keeping all classes in your mind 
is difficult or not possible. 

How Abstract Base classes work : 
By default, Python does not provide abstract classes. 
Python comes with a module that provides the base for defining 
Abstract Base classes(ABC) and that module name is ABC. 
ABC works by decorating methods of the base class as abstract 
and then registering concrete classes as implementations of the 
abstract base. A method becomes abstract when decorated with 
the keyword @abstractmethod. For Example:




Korean:
파이썬의 추상 클래스
추상 클래스는 다른 클래스의 청사진으로 간주될 수 있습니다.
내에서 생성되어야 하는 메소드 세트를 생성할 수 있습니다.
추상 클래스에서 빌드된 모든 자식 클래스. 포함하는 클래스
하나 이상의 추상 메서드를 추상 클래스라고 합니다.
추상 메서드는 선언이 있지만
구현이 없습니다.
우리는 큰 기능 단위를 설계하는 동안 추상 클래스를 사용합니다.
서로 다른 인터페이스를 위한 공통 인터페이스를 제공하고자 할 때
컴포넌트의 구현에서는 추상 클래스를 사용합니다.

추상 기본 클래스를 사용하는 이유:
추상 베이스 클래스를 정의함으로써,
공통 API(응용 프로그램 인터페이스)를 정의할 수 있습니다.
하위 클래스 집합의 경우. 이 기능은 특히 유용합니다.
제3자가 구현을 제공하려는 상황에서
플러그인과 같은 것이지만 대규모 작업을 할 때도
팀 또는 모든 클래스를 염두에 두는 대규모 코드 기반
어렵거나 불가능합니다.

추상 기본 클래스의 작동 방식:
기본적으로 Python은 추상 클래스를 제공하지 않습니다.
Python은 정의를 위한 기반을 제공하는 모듈과 함께 제공됩니다.
추상 기본 클래스(ABC)이며 해당 모듈 이름은 ABC입니다.
ABC는 기본 클래스의 메소드를 추상화하여 작동합니다.
그런 다음 구체적인 클래스를 구현으로 등록합니다.
추상 베이스. 메소드는 다음으로 장식될 때 추상적이 됩니다.
키워드 @abstractmethod. 예를 들어:


"""

# Python program showing abstract base class work
# 추상 기본 클래스 작업을 보여주는 Python 프로그램.

from abc import ABC, abstractmethod;

class MyName(ABC):
    
    @abstractmethod
    def showMyName(self):
        pass
class ShowingName1(MyName):
    # overriding abstract method
    # 추상 메서드를 재정의합니다.
    def showMyName(self):
        print("1-my full name is: Zokirkhon Kotibkhonov")
class ShowingName2(MyName):
    # overriding abstract method
    # 추상 메서드를 재정의합니다.
    def showMyName(self):
        print("2-my full name is: Zokirkhon Kotibkhonov")
class ShowingName3(MyName):
    # overriding abstract method
    # 추상 메서드를 재정의합니다.
    def showMyName(self):
        print("3-my full name is: Zokirkhon Kotibkhonov")
class ShowingName4(MyName):
    # overriding abstract method
    # 추상 메서드를 재정의합니다.
    def showMyName(self):
        print("4-my full name is: Zokirkhon Kotibkhonov")

# Driver code
# 드라이버 코드
name_1 = ShowingName1()
name_1.showMyName();


name_2 = ShowingName2()
name_2.showMyName();


name_3 = ShowingName3()
name_3.showMyName();


name_4 = ShowingName4()
name_4.showMyName();