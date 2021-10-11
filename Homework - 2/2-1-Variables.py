# -*- coding: utf-8 -*-
"""
Created on Mon Oct 11 08:32:46 2021

Student number: 180421
Full Name: KOTIBKHONOV ZOKIRKHON ZOKHIDKHON UGLI

"""


"""
English:
    
Think of a variable as a name attached to a particular object. 
In Python, variables need not be declared or defined in advance, 
as is the case in many other programming languages. 
To create a variable, you just assign it a value and then start using it. 
Assignment is done with a single equals sign (=):
    

Korean:

변수를 특정 개체에 연결된 이름으로 생각하십시오. 
Python에서는 다른 많은 프로그래밍 언어의 경우와 같이 변수를 미리 선언하거나 정의할 필요가 없습니다. 
변수를 생성하려면 값을 할당하고 사용을 시작하면 됩니다. 
할당은 단일 등호(=):로 수행됩니다.
"""


n = 300



"""
English:

This is read or interpreted as “n is assigned the value 300.” 
Once this is done, n can be used in a statement or expression, 
and its value will be substituted:


Korean:

이것은 "n에 값 300이 할당됨"으로 읽거나 해석됩니다. 
이 작업이 완료되면 n을 명령문 또는 표현식에서 
사용할 수 있으며 해당 값은 다음으로 대체됩니다.
"""


print(n) # 300



"""
English:

Later, if you change the value of n and use it again, 
the new value will be substituted instead:


Korean:

나중에 n 값을 변경하고 다시 사용하면 새 값이 대신 대체됩니다.
"""

n = 1000

print(n) # 1000



"""
English:

Python also allows chained assignment, 
which makes it possible to assign 
the same value to several variables simultaneously:


Korean:

Python은 또한 여러 변수에 동일한 값을 동시에 
할당할 수 있도록 하는 연결 할당을 허용합니다.
"""


a = b = c = 300
print(a, b, c) # 300 300 300



"""
English:

In many programming languages, variables are statically typed. 
That means a variable is initially declared to have a specific data type, 
and any value assigned to it during its lifetime must always have that type.

Variables in Python are not subject to this restriction. 
In Python, a variable may be assigned a value of one type 
and then later re-assigned a value of a different type:


Korean:

많은 프로그래밍 언어에서 변수는 정적으로 유형이 지정됩니다. 
즉, 변수는 초기에 특정 데이터 유형을 갖도록 선언되고 수명 동안 
할당된 모든 값은 항상 해당 유형을 가져야 합니다.

Python의 변수에는 이 제한이 적용되지 않습니다. 
Python에서는 변수에 한 유형의 값을 할당한 다음 
나중에 다른 유형의 값을 다시 할당할 수 있습니다.
"""



some = 23.5
print(some) # 23.5

some = "Now I'm String"
print(some) # Now I'm String



"""
English:

A Python variable is a symbolic name that is a reference or pointer to an object. 
Once an object is assigned to a variable, you can refer to the object by that name. 
But the data itself is still contained within the object.


Korean:

Python 변수는 객체에 대한 참조 또는 포인터인 기호 이름입니다. 
개체가 변수에 할당되면 해당 이름으로 개체를 참조할 수 있습니다. 
그러나 데이터 자체는 여전히 개체 내에 포함되어 있습니다.

"""


n = 300


"""
English:

This assignment creates an integer object with the value 
300 and assigns the variable n to point to that object.

The following code verifies that n points to an integer object:


Korean:

이 할당은 값이 300인 정수 개체를 만들고 해당 개체를 가리키도록 변수 n을 할당합니다.

다음 코드는 n이 정수 객체를 가리키는지 확인합니다.

"""


print(n) # 300

print(type(n)) # <class 'int'>

m = n

print(m) # 300




"""
English:

In Python, every object that is created is given a number that uniquely identifies it. 
It is guaranteed that no two objects will have the same identifier 
during any period in which their lifetimes overlap. 
Once an object’s reference count drops to zero and it is garbage collected, 
as happened to the 300 object above, then its identifying number 
becomes available and may be used again.

The built-in Python function id() returns an object’s integer identifier. 
Using the id() function, you can verify that two variables 
indeed point to the same object:


Korean:

Python에서 생성되는 모든 객체에는 고유하게 식별하는 번호가 부여됩니다. 
수명이 겹치는 기간 동안 두 개체가 동일한 식별자를 갖지 않는다는 것이 보장됩니다. 
위의 300개 개체에서와 같이 개체의 참조 횟수가 0으로 떨어지고 가비지 수집되면 해당 
식별 번호를 사용할 수 있게 되어 다시 사용할 수 있습니다.

내장 파이썬 함수 id()는 객체의 정수 식별자를 반환합니다. 
id() 함수를 사용하여 두 변수가 실제로 동일한 객체를 가리키는지 확인할 수 있습니다.

"""

n = 300
m = n 
print(id(n)) #2039542032272
print(id(m)) #2039542032272

m = 400 
print(id(m)) #2039546061072



"""
English:

The examples you have seen so far have used short, 
terse variable names like m and n. But variable names can be more verbose. 
In fact, it is usually beneficial if they are because 
it makes the purpose of the variable more evident at first glance.

Officially, variable names in Python can be any length and 
can consist of uppercase and lowercase letters (A-Z, a-z), 
digits (0-9), and the underscore character (_). An additional 
restriction is that, although a variable name can contain digits, 
the first character of a variable name cannot be a digit.

For example, all of the following are valid variable names:


Korean:

지금까지 본 예제에서는 m 및 n과 같은 짧고 간결한 변수 이름을 사용했습니다. 
그러나 변수 이름은 더 장황할 수 있습니다. 사실, 변수의 목적이 언뜻 보기에 
더 명확해지기 때문에 일반적으로 유리합니다.

공식적으로 Python의 변수 이름은 길이에 제한이 없으며 대문자와 
소문자(A-Z, a-z), 숫자(0-9) 및 밑줄 문자(_)로 구성될 수 있습니다. 
추가 제한 사항은 변수 이름에 숫자가 포함될 수 있지만 변수 
이름의 첫 번째 문자는 숫자가 될 수 없다는 것입니다.

예를 들어, 다음은 모두 유효한 변수 이름입니다.

"""

name = "Zokirkhon"
Age = 23
is_Student = True

print(name, Age, is_Student) # Zokirkhon 23 True



"""
English:

But this one is not, because a variable name can’t begin with a digit:


Korean:

그러나 이것은 변수 이름이 숫자로 시작할 수 없기 때문에 그렇지 않습니다.

"""

1999field = False

print(1999_field) # SyntaxError: invalid syntax



"""


Camel Case: Second and subsequent words are capitalized, to make word boundaries easier to see. 
(Presumably, it struck someone at some point that 
the capital letters strewn throughout the variable name vaguely resemble camel humps.)

    Example: numberOfCollegeGraduates
    
Pascal Case: Identical to Camel Case, except the first word is also capitalized.

    Example: NumberOfCollegeGraduates
    
Snake Case: Words are separated by underscores.

    Example: number_of_college_graduates


Korean:

Camel Case: 단어 경계를 더 쉽게 볼 수 있도록 두 번째 이후의 단어는 대문자로 표시됩니다. 
(변수 이름 전체에 흩어져 있는 대문자가 어렴풋이 낙타 혹을 닮았다는 사실이 누군가에게 충격을 주었을 것이다.)

    예: numberOfCollegeGraduates
    
Pascal Case: 첫 번째 단어도 대문자라는 점을 제외하고 Camel Case와 동일합니다.

    예: NumberOfCollegeGraduates
    
스네이크 케이스: 단어는 밑줄로 구분됩니다.

    예: number_of_college_graduates
    
"""






"""
English:

Reserved Words (Keywords)

There is one more restriction on identifier names. 
The Python language reserves a small set of keywords 
that designate special language functionality. 
No object can have the same name as a reserved word.


Korean:

예약어(키워드).

식별자 이름에 대한 제한 사항이 하나 더 있습니다. 
Python 언어는 특수 언어 기능을 지정하는 작은 키워드 세트를 예약합니다. 
어떤 객체도 예약어와 같은 이름을 가질 수 없습니다.

"""
"""

Python Keywords: 	 	 
False	
def	
if
raise
None
del	
import	
return
True	
elif	
in	
try
and	
else	
is	
while
as	
except	
lambda	
with
assert	
finally	
nonlocal	
yield
break	
for	
not	
class	
from	
or	
continue	
global	
pass

News from Python 3.10 version (2021,10,04):

match
case

"""



































