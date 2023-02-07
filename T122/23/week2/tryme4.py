
""" When a functions three_lines, nine_lines and clear_screen are invoked, it runs as per its definition and 
    displays the expected output. At the end of the program, 25 lines are printed in the order 3, for the three_lines function, 
    9  or the nine_lines function and finally 13 for the clear_screen function rendering a total of 25 lines. 
    function and this applies the nested function principle nesting new_line function into three_lines function, three_lines 
    function into nine_lines function and finally nine_lines function into clear_screen function symbolizing a nest structure.
"""
# Aspect: 1
# This prints a single line.

def new_line():
    print(".")
    

# Aspect: 2
# This prints 3 lines nesting new line_function into three_line function
def three_lines():
    new_line()
    new_line()
    new_line()


# Aspect: 3
# This function nests three_lines functoin into nine_lines function
def nine_lines():
    three_lines()
    three_lines()
    three_lines()


def clear_screen():
    new_line()
    three_lines()
    nine_lines()
print("Printing Three lines")#This function helps in distinguising the start of three_lines funcion's output and the start of nine_lines function's output
three_lines()
print("Printing Nine lines")#This function helps in distinguising the start of nine_lines funcion and the end of three_lines' funcion 
nine_lines()
print("Calling clear_lines printing 13 lines")#This function helps in denoting the start of clear_screen funcion's output and the end of nine_lines' funcion's output
clear_screen()

# Expected Output:
# Three lines
# .
# .
# .
# Nine lines
# .
# .
# .
# .
# .
# .
# .
# .
# .
# Print clear screen
# .
# .
# .
# .
# .
# .
# .
# .
# .
# .
# .
# .
# .