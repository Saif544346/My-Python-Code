n=input("Enter a text of numbers")
text=n.split()
sum=0
for num in text:
    sum=sum+int(num)
print(sum)
