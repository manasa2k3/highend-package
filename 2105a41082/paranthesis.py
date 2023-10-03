def are_parentheses_balanced(expression):
    stack = []
    opening_brackets = "({["
    closing_brackets = ")}]"

    for char in expression:
        if char in opening_brackets:
            stack.append(char)
        elif char in closing_brackets:
            if not stack:
                return False  # Unmatched closing bracket
            top_of_stack = stack.pop()
            if opening_brackets.index(top_of_stack) != closing_brackets.index(char):
                return False  # Mismatched opening and closing brackets

    return not stack  # True if the stack is empty (all parentheses matched)

# Example usage:
expression = "([{})]"
if are_parentheses_balanced(expression):
    print("Parentheses are balanced.")
else:
    print("Parentheses are not balanced.")