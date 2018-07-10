# Name:
# Date:

# proj02_02: Fibonaci Sequence

"""
Asks a user how many Fibonacci numbers to generate and generates them. The Fibonacci 
sequence is a sequence of numbers where the next number in the sequence is the sum of the 
previous two numbers in the sequence. The sequence looks like this: 
1, 1, 2, 3, 5, 8, 13...
"""
"""
counter = 1
input1 = raw_input("How many Fibonacci numbers would you like to generate? ")
num_low = 0
num_high = 1
num_spare = 0
print 1
for counter in range (int(input1)):
    print num_high + num_low
    num_spare = num_high
    num_high = num_high + num_low
    num_low = num_spare
"""

# While loop version

"""
counter = 1
input2 = raw_input("How many Fibonacci numbers would you like to generate? ")
num_low = 0
num_high = 1
num_spare = 0
print 1
while counter < int(input1):
    print num_high + num_low
    num_spare = num_high
    num_high = num_high + num_low
    num_low = num_spare
    counter = counter + 1
"""

# Powers of 2 version

"""
counter = 1
input3 = raw_input("How many powers of 2 would you like to generate? ")
for counter in range (1, int(input3) + 1):
    print 2 ** counter
"""

# Divisors Version


