# To change the value of a global variable inside a function,
#  refer to the variable by using the global keyword
x="Ibrahim"
def myFun():
    global x
    x="Ibrahim"
myFun()
print("hello "+x)