import time
t=time.strftime('%H:%M:%S')
hour=int (time.strftime('%H'))
#hour=int(input("enter time:"))
print(hour)
if(hour>=0 and hour<12):
    print("Good Morning Sir")
elif(hour>=12 and hour<17):
    print("Good Afternoon Sir")
else:
    print("Good Night Sir")