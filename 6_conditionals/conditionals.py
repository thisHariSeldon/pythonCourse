# -------------- CONDITIONALS -----------
'''
Conditionals in Python are statements that allow your program to make decisions and execute specific code based on certain conditions.
'''
# if | if-else | if-elif-else 
# Comparison Operators: ==,!=, <, >, <=, >=
# Logical Operators: and | or | not
# Membership Operators: in | not in 
# Ternary (One-Line) Conditional: 
# message = "Adult" if age >= 18 else "Minor"
# Nested Conditionals
age = 20
if age >= 18:
    if age >= 21:
        print("You can drink alcohol.")
    else:
        print("You are an adult, but cannot drink alcohol.")  # Output: This
else:
    print("You are a minor.")




# ----  Key Points
# 1) Indentation Matters: 
if True:
    print("Indented correctly")
print("Not indented")

# 2) Conditionals must Evaluate to Boolean
# 3) Chaining Conditions:
#       -  Use elif for multiple conditions.
#       -  Use and, or, and not to combine conditions.

# -------------------- Nested conditionals

