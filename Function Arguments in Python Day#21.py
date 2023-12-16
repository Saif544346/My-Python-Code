#Default Argumrnts
#Keyword Argumrnts
#Variable Length Argumrnts
#Required Argumrnts
def name(fname,midname,lastname):
    print("Welcome "+fname,midname,lastname)
name("Golam ","Ibadullah ","Saif")
#Default Argumrnts
def avg(a,b,c=20):
    print("avareg=",(a+b+c)/2)
avg(10,20)

def avareg(*number):
    sum=0
    for i in number:

        sum=sum+i
        print(sum)

avareg(20,40,54,34,24)
