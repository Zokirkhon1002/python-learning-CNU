with open('bool.py') as file:
    lines = file.read()
print(lines)
code_object = compile(lines,'bool.py','exec')
# code_object = compile(lines,'','exec')
exec(code_object)