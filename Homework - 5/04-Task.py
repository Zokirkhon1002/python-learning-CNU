# -*- coding: utf-8 -*-
"""
Created on Mon Dec  6 10:09:24 2021

@author: Zokirkhon
task: 4. Explain the 4 ways to import a module.
"""


"""
English:

Import in python is similar to #include header_file in C/C++. 
Python modules can get access to code from another module by importing the file/function using import. 
The import statement is the most common way of invoking the import machinery, but it is not the only way.
import module_name 
When the import is used, it searches for the module initially in the local scope by calling __import__() function. 
The value returned by the function is then reflected in the output of the initial code.



Korean:

파이썬에서 가져오기는 C/C++에서 #include header_file과 비슷합니다.
Python 모듈은 import를 사용하여 파일/함수를 가져와서 다른 모듈의 코드에 액세스할 수 있습니다.
import 문은 수입 기계를 호출하는 가장 일반적인 방법이지만 유일한 방법은 아닙니다.
import module_name
가져오기를 사용하면 __import__() 함수를 호출하여 초기에 로컬 범위에서 모듈을 검색합니다.
함수에서 반환된 값은 초기 코드의 출력에 반영됩니다.


"""


import math
print(math.pi)
# output: 3.141592653589793



"""
English:

import module_name.member_name 
In the above code module, math is imported, and its variables can be accessed by considering it to be a class and pi as its object. 
The value of pi is returned by __import__(). 
pi as a whole can be imported into our initial code, rather than importing the whole module. 


Korean:

import module_name.member_name
위의 코드 모듈에서 수학을 임포트하고, 그 변수는 클래스로 간주하고 파이를 객체로 간주하여 접근할 수 있습니다.
pi의 값은 __import__()에 의해 반환됩니다.
전체 모듈을 가져오는 대신 파이 전체를 초기 코드로 가져올 수 있습니다.

"""

from math import pi
print(pi)
# output: 3.141592653589793



"""
English:


from module_name import * 
In the above code module, math is not imported, rather just pi has been imported as a variable. 
All the functions and constants can be imported using *.

Korean:

module_name에서 가져오기 *
위의 코드 모듈에서 수학은 가져오지 않고 pi만 변수로 가져왔습니다.
모든 함수와 상수는 *를 사용하여 가져올 수 있습니다.

"""

from math import *

print(pi)
# output: 3.141592653589793

print(factorial(5))
# output: 120


"""
English:

Importing a module under a different name
We can also use the as syntax when importing a whole module.

Korean:

다른 이름으로 모듈 가져오기
전체 모듈을 가져올 때 as 구문을 사용할 수도 있습니다.

"""

from math import factorial as f;

print(f(5))
# output: 120