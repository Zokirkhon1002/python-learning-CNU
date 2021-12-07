# -*- coding: utf-8 -*-
"""
Created on Mon Dec  6 11:30:42 2021

@author: Zokirkhon
task: 12. Describe the __name__ variable.
"""



"""
English:
__name__ (A Special variable) in Python.
Since there is no main() function in Python, 
when the command to run a python program is given to the interpreter, 
the code that is at level 0 indentation is to be executed. 
However, before doing that, it will define a few special variables. 
__name__ is one such special variable. If the source file is executed as the main program, 
the interpreter sets the __name__ variable to have a value “__main__”. 
If this file is being imported from another module, __name__ will be set to the module’s name.
__name__ is a built-in variable which evaluates to the name of the current module. 
Thus it can be used to check whether the current script is being run on its own or being imported 
somewhere else by combining it with if statement, as shown below.


Korean: 

Python의 __name__(특수 변수).
파이썬에는 main() 함수가 없기 때문에,
파이썬 프로그램을 실행하라는 명령이 인터프리터에게 주어졌을 때,
레벨 0 들여쓰기에 있는 코드가 실행됩니다.
그러나 그렇게 하기 전에 몇 가지 특수 변수를 정의합니다.
__name__은 그러한 특수 변수 중 하나입니다. 소스 파일을 메인 프로그램으로 실행하면,
인터프리터는 __name__ 변수가 "__main__" 값을 갖도록 설정합니다.
이 파일을 다른 모듈에서 가져오는 경우 __name__이 모듈 이름으로 설정됩니다.
__name__은 현재 모듈의 이름으로 평가되는 내장 변수입니다.
따라서 현재 스크립트가 자체적으로 실행되고 있는지 또는 가져오는지 확인하는 데 사용할 수 있습니다.
아래와 같이 if 문과 결합하여 다른 곳으로 이동합니다.
"""


