                           #Hello World

#Use the "print" command to print the line "Hello, World!".
print("Hello, World")
#output : Hello, World



                        #Variables and types

#Python supports two types of numbers - integers and floating point numbers. 

#Int number
myint = 8
print(myint) # prints 8
#Float number
myfloat = 7.0
print(myfloat) # prints 7.0
#Strings
#Strings are defined either with a single quote or a double quotes.
mystring = 'hello'
print(mystring) #print "hello"

hello = "hello"
world = "world"
helloworld = hello + " " + world
print(helloworld)

                            #Lists
#Lists are very similar to arrays. They can contain any type of variable, and they can contain as many variables as you wish. 

mylist = []
mylist.append(1)
mylist.append(2)
mylist.append(3)
print(mylist[0]) # prints 1
print(mylist[1]) # prints 2
print(mylist[2]) # prints 3

#Get and element of a list
mylist = [1,2,3]
print(mylist[0]) # prints first element 1

numbers = []
strings = []
names = ["John", "Eric", "Jessica"]

# write your code here
second_name = None


# this code should write out the filled arrays and the second name in the names list (Eric).
numbers = []
strings = []
names = ["John", "Eric", "Jessica"]

# add number to number list
numbers.append(1)
numbers.append(2)
numbers.append(3)

#add strings to names list
strings.append("hello")
strings.append("world")

second_name = names[1]

# this code should write out the filled arrays and the second name in the names list (Eric).
print(numbers)
print(strings)
print("The second name on the names list is %s" % second_name)

                        #Arithmetic Operators

# the addition, subtraction, multiplication, and division operators can be used with numbers.
number = 1 + 2 * 3 / 4.0
print(number) #prints 2.5 


# (%) operator, returns the integer remainder of the division. dividend % divisor = remainder.
remainder = 11 % 3
print(remainder) # prints 2

#Using two multiplication symbols makes a power relationship.
squared = 7 ** 2 # prints 49
cubed = 2 ** 3  # prints 8
print(squared)
print(cubed)

#Operators with Strings
#Python supports concatenating strings using the addition operator:

helloworld = "hello" + " " + "world"
print(helloworld) #prints "hello world"
