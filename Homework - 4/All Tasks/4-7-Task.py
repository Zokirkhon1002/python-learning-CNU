# -*- coding: utf-8 -*-
"""
Created on Mon Nov 22 11:45:24 2021

@author: Zokirkhon
Homework - 4.7
"""


"""
Task: Describe instance variables and class variables.

직무: 인스턴스 변수와 클래스 변수를 설명하시오
"""


"""
English:

Python class variables are declared within a class and their 
values are the same across all instances of a class. 
Python instance variables can have different values 
across multiple instances of a class.
Class variables share the same value among all instances of the class. 
The value of instance variables can differ across each instance of a class.
Class variables can only be assigned when a class has been defined. 
Instance variables, on the other hand, can be assigned or changed at any time.
Both class variables and instance variables store a value in a program, 
just like any other Python variable.




Korean:
Python 클래스 변수는 클래스 내에서 선언되며
값은 클래스의 모든 인스턴스에서 동일합니다.
Python 인스턴스 변수는 다른 값을 가질 수 있습니다.
클래스의 여러 인스턴스에 걸쳐.
클래스 변수는 클래스의 모든 인스턴스에서 동일한 값을 공유합니다.
인스턴스 변수의 값은 클래스의 각 인스턴스에 따라 다를 수 있습니다.
클래스 변수는 클래스가 정의된 경우에만 할당할 수 있습니다.
반면 인스턴스 변수는 언제든지 할당하거나 변경할 수 있습니다.
클래스 변수와 인스턴스 변수 모두 프로그램에 값을 저장합니다.
다른 Python 변수와 마찬가지로.


"""



"""
English:

Python Class Variables
A Python class variable is shared by all object instances of a class. 
Class variables are declared when a class is being constructed. 
They are not defined inside any methods of a class.

Because a class variable is shared by instances of a class, 
the Python class owns the variable. As a result, 
all instances of the class will be able to access that variable. 
Class variables are shared by all instances that access the class.

Here is an example of a class variable in Python:
    
class Espresso:
	menu_type = "Drink"

Accessing a Class Variable in Python
Now that we’ve declared a class variable, 
we can access it when we create an object of our class. 
So, if we want to create a new class instance and see 
the value of the menu_type variable, we could use this code:

class Espresso:
	menu_type = "Drink"

espresso_order = Espresso()
print(espresso_order.menu_type)




Korean:

파이썬 클래스 변수
Python 클래스 변수는 클래스의 모든 개체 인스턴스에서 공유됩니다.
클래스 변수는 클래스가 생성될 때 선언됩니다.
클래스의 어떤 메서드에도 정의되어 있지 않습니다.

클래스 변수는 클래스의 인스턴스에 의해 공유되기 때문에,
Python 클래스는 변수를 소유합니다. 결과적으로,
클래스의 모든 인스턴스는 해당 변수에 액세스할 수 있습니다.
클래스 변수는 클래스에 액세스하는 모든 인스턴스에서 공유됩니다.

다음은 Python의 클래스 변수 예입니다.

class Espresso:
	menu_type = "Drink"


파이썬에서 클래스 변수 접근하기
이제 클래스 변수를 선언했으므로,
클래스의 개체를 만들 때 액세스할 수 있습니다.
따라서 새 클래스 인스턴스를 만들고 보려면
menu_type 변수의 값에 대해 다음 코드를 사용할 수 있습니다.

class Espresso:
	menu_type = "Drink"

espresso_order = Espresso()
print(espresso_order.menu_type)

"""


"""
English:

Python Instance Variables
Python instance variables are owned by an instance of a class. 
The value of an instance variable can be different depending on 
the instance with which the variable is associated.
This means that the value of each instance variable can be. 
This is unlike a class variable where the variable can only have one value that you assign. 
Instance variables are declared inside a class method.
Here is an example of two instance variables in Python:


class CoffeeOrder:
	def __init__(self, coffee_name, price):
		self.coffee_name = coffee_name
		self.price = price

In this example, coffee_name and price are instance variables that exist within our class.

Assinging Values to an Instance Variable in Python
We can assign values to an instance variable when we declare a class. 
We do this by specifying the values we want to assign as arguments 
when we declare the class. Suppose we want to create an instance of 
our class with the following values:

coffee_name = “Espresso”
price = 2.10

We could create this instance using the following code:

class CoffeeOrder:
	def __init__(self, coffee_name, price):
		self.coffee_name = coffee_name
		self.price = price

customer_order = CoffeeOrder("Espresso", 2.10)
print(customer_order.coffee_name)
print(customer_order.price)

# output:
Espresso
2.10






Korean:

파이썬 인스턴스 변수
Python 인스턴스 변수는 클래스의 인스턴스가 소유합니다.
인스턴스 변수의 값은 다음에 따라 다를 수 있습니다.
변수가 연결된 인스턴스입니다.
이것은 각 인스턴스 변수의 값이 될 수 있음을 의미합니다.
이것은 변수가 사용자가 할당한 값을 하나만 가질 수 있는 클래스 변수와 다릅니다.
인스턴스 변수는 클래스 메서드 내에서 선언됩니다.
다음은 Python의 두 인스턴스 변수의 예입니다.


class CoffeeOrder:
	def __init__(self, coffee_name, price):
		self.coffee_name = coffee_name
		self.price = price

이 예에서 coffee_name과 price는 우리 클래스 내에 존재하는 인스턴스 변수입니다.


Python에서 인스턴스 변수에 값 할당
클래스를 선언할 때 인스턴스 변수에 값을 할당할 수 있습니다.
인수로 할당하려는 값을 지정하여 이 작업을 수행합니다.
클래스를 선언할 때. 의 인스턴스를 생성한다고 가정해 보겠습니다.
다음 값을 가진 클래스:

coffee_name = “Espresso”
price = 2.10


다음 코드를 사용하여 이 인스턴스를 만들 수 있습니다.

class CoffeeOrder:
	def __init__(self, coffee_name, price):
		self.coffee_name = coffee_name
		self.price = price

customer_order = CoffeeOrder("Espresso", 2.10)
print(customer_order.coffee_name)
print(customer_order.price)

# output:
Espresso
2.10

"""




