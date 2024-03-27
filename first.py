"""
def mult_sum(x,y) :
    product = x*y
if product <= 1000:
   return product
else:
  return x+y 
  res = mult_sum(10,20)
 print("result is: ",res)
 """



def mult_sum(x, y):
    product = x * y
    if product <= 1000:
        return product
    else:
        return x + y

res = mult_sum(10, 20)
print("result is: ", res)
res = mult_sum(30, 40)
print("result is: ", res)
