# Aspect: 1
def new_line():
    print(".")
    
    
new_line()
print("New line")
# This prints a single line.

# Aspect: 2
def three_lines():
    new_line()
    new_line()
    new_line()
    
three_lines()
print("Three lines")

# Aspect: 3
def nine_lines():
    three_lines()
    three_lines()
    three_lines()
    three_lines()
    three_lines()
    three_lines()
    three_lines()
    three_lines
    three_lines()
    
nine_lines()
print("Nine lines")
# When a function is invoked, a it runs as per its definition and 
# displays the expected output. At the end of the program, 34 lines are printed in the order 1, for the new line function, 
# 3 for the three line function and finally 25 for the nine lines 
# function and this applies the nested function principle.
