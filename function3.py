def function3(a=1, b=1): 
  """I'm a function that calls other functions """
  print("I'm {} and I'm about to call subtractor function".format(function3.__name__))
  total = subtractor(a,b)
  print("I'm {} and I'm about to call print_function".format(function3.__name__))
  print_function()
  print("I'm {} and I'm about return total".format(function3.__name__))
  return total

if __name__ == '__main__':
  total = function3()
  print("total is {}".format(total))
    