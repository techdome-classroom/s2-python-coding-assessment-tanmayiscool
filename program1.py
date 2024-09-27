class Solution(object):
   def is_valid_parentheses(s: str) -> bool:
    stack = [s]
    bracket_map = {')': '(', '}': '{', ']': '['}
    
    for char in s:
        if char in bracket_map.values():
            stack.append(char) 
        elif char in bracket_map.keys():
            if not stack or stack[-1] != bracket_map[char]:
                return False  
            stack.pop() 
            
    return not stack  


user_input = input("Enter a string of parentheses: ")
x=Solution.is_valid_parentheses(user_input)
if x:
    print("true")
else:
    print("false")