def countdown(n):
    if n <= 0:
        print('Blastoff!')
    else:
        print(n)
        countdown(n-1)
        
def countup(n):
    if n >= 0:
        print('Blastoff!')
    else:
        print(n)
        countup(n+1)
        
num = int(input("Enter a number: "))

if num > 0:
    countdown(num)
elif num < 0:
    countup(num)
else:
    print('Blastoff!')
    
# Output for input 3:

# Enter a number: 3
# 3
# 2
# 1
# Blastoff!
# Output for input -3:


# Enter a number: -3
# -3
# -2
# -1
# Blastoff!
# Output for input 0:

# Enter a number: 0
# Blastoff!
# For input of zero, I have called the print statement to output "Blastoff!" 
# because zero is neither positive nor negative, and it's the starting point 
# from which we count either up or down.