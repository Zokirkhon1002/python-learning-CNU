# -*- coding: utf-8 -*-
"""
Created on Mon Nov 15 05:06:32 2021

@author: Zokirkhon
topic: Functions
"""


# 1
# def func(x):
#     x+=10;
#     print(x)
# outerdate = 50;
# func(outerdate)


# 2
# print(locals())
# # {'__name__': '__main__', '__doc__': '\Created on Mon Nov 15 05:06:32 2021\n
# # \n@author: Zokirkhon\ntopic: Functions\n
# # ', '__package__': None, '__loader__':
# # <_frozen_importlib_external.SourceFileLoader object at 0x00000259596AA100>,
# # '__spec__': None, '__annotations__': {},
# # '__builtins__': <module 'builtins' (built-in)>,
# # '__file__':
# # 'D:\\Coding Class\\Self study from Videos\\Python programming\\Chonnam National University\\11-lesson\\11-2-lesson.py',
# # '__cached__': None}


# 3
# def func():
#     print(locals());

# func()
# # ouput:
# # {};


# def func2():
#     x=10;
#     y=10;
#     print(locals());
# func2()
# # output:
# # {'x': 10, 'y': 10}


# 4
# print(dir(__builtins__))
# # output: ['ArithmeticError', 'AssertionError', 'AttributeError', 'BaseException',
# # 'BlockingIOError', 'BrokenPipeError', 'BufferError', 'BytesWarning',
# # 'ChildProcessError', 'ConnectionAbortedError', 'ConnectionError',
# # 'ConnectionRefusedError', 'ConnectionResetError', 'DeprecationWarning',
# # 'EOFError', 'Ellipsis', 'EnvironmentError', 'Exception', 'False',
# # 'FileExistsError', 'FileNotFoundError', 'FloatingPointError',
# # 'FutureWarning', 'GeneratorExit', 'IOError', 'ImportError',
# # 'ImportWarning', 'IndentationError', 'IndexError', 'InterruptedError',
# # 'IsADirectoryError', 'KeyError', 'KeyboardInterrupt', 'LookupError',
# # 'MemoryError', 'ModuleNotFoundError', 'NameError', 'None',
# # 'NotADirectoryError', 'NotImplemented', 'NotImplementedError',
# # 'OSError', 'OverflowError', 'PendingDeprecationWarning', 'PermissionError',
# # 'ProcessLookupError', 'RecursionError', 'ReferenceError',
# # 'ResourceWarning', 'RuntimeError', 'RuntimeWarning', 'StopAsyncIteration',
# # 'StopIteration', 'SyntaxError', 'SyntaxWarning', 'SystemError',
# # 'SystemExit', 'TabError', 'TimeoutError', 'True', 'TypeError',
# # 'UnboundLocalError', 'UnicodeDecodeError', 'UnicodeEncodeError',
# # 'UnicodeError', 'UnicodeTranslateError', 'UnicodeWarning', 'UserWarning',
# # 'ValueError', 'Warning', 'WindowsError', 'ZeroDivisionError', '__build_class__',
# # '__debug__', '__doc__', '__import__', '__loader__', '__name__', '__package__',
# # '__spec__', 'abs', 'all', 'any', 'ascii', 'bin', 'bool', 'breakpoint',
# # 'bytearray', 'bytes', 'callable', 'chr', 'classmethod', 'compile',
# # 'complex', 'copyright', 'credits', 'delattr', 'dict', 'dir', 'divmod',
# # 'enumerate', 'eval', 'exec', 'exit', 'filter', 'float', 'format',
# # 'frozenset', 'getattr', 'globals', 'hasattr', 'hash', 'help', 'hex',
# # 'id', 'input', 'int', 'isinstance', 'issubclass', 'iter', 'len', 'license',
# # 'list', 'locals', 'map', 'max', 'memoryview', 'min', 'next', 'object', 'oct',
# # 'open', 'ord', 'pow', 'print', 'property', 'quit', 'range', 'repr',
# # 'reversed', 'round', 'set', 'setattr', 'slice', 'sorted', 'staticmethod',
# # 'str', 'sum', 'super', 'tuple', 'type', 'vars', 'zip']


# 5
# #now 1;
# global_variable = 77;
# def function():
#     print(global_variable)
# function();


# 6
# global_variable = 77;
# def function():
#     global_variable = 88;
#     print(global_variable)
# function();
# # output: 88;


# 7
# print = 'hi';
# print(print)
# print("Hello")


# 8
# glob = 200;
# def function():
#     glob +=1;
#     print(glob)
# function();
# # output: error;


# 9
# glob = 200;
# def function():
#     global glob
#     glob +=1
#     print(glob)
# function();
# # output: 201


# 10
# var=10;
# def func():
#     global var
#     var = 20
#     print(locals())

# func() # output: {}
# print(var) # output: 20


# 11
# def outer():
#     a=1;
#     def inner1():
#         b=2;
#         def inner2():
#             c=3;
#             print(a,b,c)
#         inner2();
#     inner1();
# outer();


# 12
# def outer():
#     a=1;
#     def inner1():
#         b=2;
#         def inner2():
#             c=3;
#             print('inner2')
#             print(a,b,c)
#         print('inner1');
#         inner2();
#     print('outer');
#     inner1();
# outer();


# 13
# global_variable = 77;
# def outer():
#     global_variable = 100;
#     def inner():
#         global global_variable;     # global_variable = 77;
#         global_variable += 1;
#         print(global_variable);
#     inner();
# outer();
# # output: 78;

# global_variable = 77;
# def outer2():
#     global_variable = 100;
#     def inner():
#         nonlocal global_variable;   # nonlocal global_variable = 100;
#         global_variable += 1;
#         print(global_variable);
#     inner();
# outer2();
# # output: 101;


# 14
# outData = 77
# def func(param):
#     param += 23;
#     print(param)

# func(outData)   # output: 100
# print(outData)  # output: 77


# 15
# outData = 77
# def func():
#     global outData
#     outData += 23;
#     print(outData)

# func()   # output: 100
# print(outData)  # output: 100


# 16
# myList = [9, 1, 7, 3, 4, 2, 5, 6, 8]

# myList.sort(key=lambda x:x)
# print(myList)

# myList.sort(key=lambda x:-x)
# print(myList)

# myList.sort(key=lambda x:x%3)
# print(myList)

# myList.sort(key=lambda x:x%2)
# print(myList)






###17
# L=['123','45','6','780']
# print(L)    # ['123', '45', '6', '780']

# L.sort()
# print(L)    # ['123', '45', '6', '780']

# L.sort(key=int);
# print(L)    # ['6', '45', '123', '780']

# L.sort(reverse=True);
# print(L)    # ['780', '6', '45', '123']









###18
def func(string, option=0):
    if option:
        print(string.upper())
    else:
        print(string.lower())


def func2(string, option=0):
    print(string.upper() if option else string.lower())


def func3(string, option=0):
    print(option and string.upper() or string.lower())


def func_lambda(string, option=0):
    print(option and (lambda s:s.upper())(string) or (lambda s:s.lower())(string))

x="chonnam national university"
func(x) # output: chonnam national university
func(x,1)   # output: CHONNAM NATIONAL UNIVERSITY
func(x)  # output: chonnam national university
func_lambda(x,1)    # output: CHONNAM NATIONAL UNIVERSITY







