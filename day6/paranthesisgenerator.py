braces={'{':'}','[':']','(':')'}
ob=['{','[','(']
for i in range(len(ob)):
    print(ob[i],braces.get(ob[i]),end="")
