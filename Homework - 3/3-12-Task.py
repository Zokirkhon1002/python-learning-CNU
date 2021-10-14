"""
Created on Thu Oct 14 23:31:38 2021

Student number: 180421
Full Name: KOTIBKHONOV ZOKIRKHON ZOKHIDKHON UGLI

"""

# Task:
# Describe the following program.

from sys import argv

if __name__ == '__main__':
    print(f"Number of argv: {len(argv)}")
    for item in argv:
        print(item)

# output
# Number of argv: 1
# 3-12-Task.py


"""
English:

It means “from the module sys, import the function or parameter argv”.

The sys module contains all kinds of system-related functions and constants.
The list of command line arguments passed to a Python script. 
argv[0] is the script name (it is operating system dependent whether 
this is a full pathname or not). If the command was executed using the -c 
command line option to the interpreter, argv[0] is set to the string '-c'. 
If no script name was passed to the Python interpreter, argv[0] is the empty string.
To loop over the standard input, or the list of files given on the command line, 
see the fileinput module. And with FOR LOOP we printed each item in argv.


Korean:

"모듈 sys에서 함수 또는 매개변수 argv를 가져옵니다"를 의미합니다.

sys 모듈에는 모든 종류의 시스템 관련 함수와 상수가 포함되어 있습니다.
Python 스크립트에 전달된 명령줄 인수 목록입니다.
argv[0]은 스크립트 이름입니다(운영 체제에 따라 다름
이것은 전체 경로명인지 아닌지). -c를 사용하여 명령을 실행한 경우
인터프리터에 대한 명령줄 옵션, argv[0]은 문자열 '-c'로 설정됩니다.
스크립트 이름이 Python 인터프리터에 전달되지 않은 경우 argv[0]은 빈 문자열입니다.
표준 입력 또는 명령줄에 제공된 파일 목록을 반복하려면,
fileinput 모듈을 참조하십시오.
그리고 FOR LOOP를 사용하여 argv의 각 항목을 인쇄했습니다.
"""