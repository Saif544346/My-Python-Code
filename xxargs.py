'''def student(*details):
    print(details)
student(101,"saif",3.50)'''
def add(*number):
    sum=0
    for num in number:
        sum=sum+num
    print(sum)
add(2,40)
add(20,30,40)