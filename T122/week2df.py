#Aspect 1
def function(x): #x is param
    print(x)
    print(x)
    print(x)

#Aspect 2
v1 = 1
function(9 - 1)
function('Pythoneering')
function(1)

#Aspect 3:
def fun_2():
    loc = 228

#Aspect 3:
# fun_2() if you run this code,
#print(loc)  there will be an error, since the variable is local
def func_3(param):
    print('really a parameter')

#Aspect 4:
func_3(1000)
#print(unical_param) if you run this code,there will be NameError
v1 = 7
def fun_4(v1):
    print(v1)
    
    #Aspect 5:
#variable inside a function and a variable with the same name outside
# of it are two different variables
# and their values do not overlap or replace fun_4(v1)



