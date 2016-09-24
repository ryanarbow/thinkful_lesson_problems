def print_function():
   """I'm also a function, but I don't take any parameters"""
   print("I'm {}, and I'm printing now".format(print_function.__name__))

if __name__ == '__main__':
   print_function()
