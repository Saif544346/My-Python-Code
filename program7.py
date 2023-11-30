marks=int(input("Enter a marks"))
if marks>=80:
    print("A+")
elif marks>=70:
    print("A")
elif marks>=60:
    print("A-")
elif marks>=50:
    print("B")
elif marks>=33:
    print("pass")
elif marks<33:
    print("fail")
else:
    print("invalid marks !! please enter valid marks")