import time

temp=int(input("enter an tempature"))
if temp>=0 and temp<=30:
    print("good")
    print("go outside")
elif temp<0 or temp>30:
    print("bad")
    print("don't go to be outside")
for i in range(10):
    print(i)
for i in range(80,100+1,2):
    print(i,"saif")
for i in "saif":
    print(i)
for seconds in range(10,0,-1):
    print(seconds)
    time.sleep(1)
print("happy new year")







