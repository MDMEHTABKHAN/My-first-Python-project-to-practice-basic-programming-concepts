x = int(input("Enter the value of x: "))
y = int(input("Enter the value of y: "))
temp = x
x = y
y = temp

print("the value of x: ", x)
print("The value of y: ", y)
print("the value of temp variable is: ", temp)

# without using third variable

m = 19
s = 13

m, s = s, m

print("the value of a: ", m)
print("The value of b: ", s)
