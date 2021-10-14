"""
Created on Thu Oct 14 23:07:50 2021

Student number: 180421
Full Name: KOTIBKHONOV ZOKIRKHON ZOKHIDKHON UGLI

"""

# Task:
# Explain __name__ variable


"""
English:

When the Python interpreter reads a source file, it executes all of the code found in it.
Before executing the code, it will define a few special variables. 
For example, if the python interpreter is running that module (the source file) as the main program, 
it sets the special __name__ variable to have a value "__main__". 
If this file is being imported from another module, __name__ will be set to the module's name.
One reason for doing this is that sometimes you write a module (a .py file) 
where it can be executed directly. Alternatively, it can also be imported 
and used in another module. By doing the main check, you can have that code 
only execute when you want to run the module as a program and not have it execute 
when someone just wants to import your module and call your functions themselves.

For example, if you have 2 files one.py and 3-11-Task.py with the following code:


Korean:

파이썬 인터프리터는 소스 파일을 읽을 때 그 안에 있는 모든 코드를 실행합니다.
코드를 실행하기 전에 몇 가지 특수 변수를 정의합니다. 
예를 들어, 파이썬 인터프리터가 그 모듈(소스 파일)을 메인 프로그램으로 실행한다면, 
특별한 __name__ 변수가 "__main__" 값을 갖도록 설정합니다. 
이 파일을 다른 모듈에서 가져오는 경우 __name__이 모듈 이름으로 설정됩니다.

이렇게 하는 한 가지 이유는 때때로 직접 실행할 수 있는 모듈(.py 파일)을 작성하기 때문입니다. 
또는 다른 모듈에서 가져와서 사용할 수도 있습니다. 
주요 검사를 수행하면 해당 코드가 모듈을 프로그램으로 실행하려는 경우에만 실행되고 
누군가가 모듈을 가져와서 함수 자체를 호출하려고 할 때 실행하지 않도록 할 수 있습니다.

예를 들어 다음 코드가 포함된 one.py 및 3-11-Task.py 파일이 2개 있는 경우.

"""

# one.py
"""
def func():
    print("func() in one.py")
print("Root of one.py")
if __name__ == "__main__":
    print("one.py is being run directly")
else:
    print("one.py is being imported")

"""
# 3-11-Task.py

import one
print("Root of two.py")
one.func()
if __name__ == "__main__":
    print("two.py is being run directly")
else:
    print("two.py is being imported")

"""
English:

Now If we run,
$ python one.py 


# output
Root of one.py
one.py is being run directly


Korean:

이제 실행하면
$ python one.py


# 출력
Root of one.py
one.py is being run directly
"""

"""
English:

But if we run,
$ python 3-11-Task.py

# output
Root of one.py
one.py is being imported
Root of two.py
func() in one.py
two.py is being run directly


Korean:
하지만 우리가 실행한다면:
$ python 3-11-Task.py

# 출력
Root of one.py
one.py is being imported
Root of two.py
func() in one.py
two.py is being run directly

"""

