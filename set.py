num1={1,2,4,5,7,1}
num2=set([2,4,6,8,1,7])
num1.add(9)
num1.remove(4)
print(num1|num2)
print(num1&num2)
print(num1-num2)
print(num1)
