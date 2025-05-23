# if staement
x = 10
if x > 5:
    print("x is greater than 5")

# function 
def my_function1(fname):
    print(fname + " Refsnes")

my_function1("Emil")
def my_function2(fname, lname):
    print(fname + " " + lname )

my_function2("Emil", "Refsnes" )

def my_function3(*kids):
    print("The youngest child is " + kids[2])

my_function3("Emil", "Tobias", "Linus")

def my_function4(child3, child2, child1):
    print("The youngest child is " + child2)
    print("The big child is " + child1)

my_function4(child1="Emil", child2="Tobias", child3="Linus")

def my_function5(**kid):
    print("His last name is " + kid["fname"])

my_function5(fname="Tobias", lname="Refsnes")

def my_function6(country="Norway"):
    print("I am from " + country)

my_function6("India")
my_function6()  # uses default "Norway"

def my_function7(x):
    return 5 * x

print(my_function7(3))

def tri_recursion(k):
    if k > 0:
        result = k + tri_recursion(k - 1)
        print(result)
    else:
        result = 0
    return result

tri_recursion(5)

# txt = "The best things in life are free!"
# print("t" in txt)  # Output: True
# # print(f.read())
# print(f.readline())
# f.close()
# f = open("demofile2.txt", "a")
f = open("demofile2.txt", "a")
f.write("sjsakjaskjfNow the file has more content!")
f.close()
f = open("demofile2.txt")
print(f.read())
t = ([1, 2], 'text')
t[0][0] = 100  # This works because the list inside the tuple is mutable
print(t)

coords = {}
coords[(0, 0)] = "origin"
coords[(1, 2)] = "point A"
coords[(2, 3)] = "point b"
print(coords[( 1 , 3)])  # Output: point A