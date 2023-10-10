def paranthesis_check(l):
    braces={'{':'}','[':']','(':')'}
    bstack=[]
    if len(l)%2!=0:
        return False
    for i in l:
        if i in braces.keys():
            bstack.append(i)
        if i in braces.values():
            if len(bstack)==0:
                return False
            ele=bstack.pop()
            if braces.get(ele)!=i:
                return False
    if len(bstack)!=0:
        return False
    return True
def generate_parentheses(n):
    def backtrack(s, left, right):
        if len(s) == 2 * n:
            combinations.append(s)
            return
        if left < n:
            
            backtrack(s +'(', left + 1, right)
        if right < left:
            
            backtrack(s +')', left, right + 1)
        if left < n:
        
            backtrack(s +'[', left + 1, right)
        if right < left:
            
            backtrack(s +']', left, right + 1)
        if left < n:
        
            backtrack(s +'{', left + 1, right)
        if right < left:
            backtrack(s +'}', left, right + 1)

    combinations = []
    backtrack('', 0, 0)
    return combinations

# Example usage
n = int(input())

a='['
b='{'
c='('
valid_parentheses = generate_parentheses(n)
for i in valid_parentheses:
    if paranthesis_check(i) and a in i and b in i and c in i:
        print(i)
