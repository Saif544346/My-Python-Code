class student:
    roll=""
    gpa=""
    def display(self):
        print("roll : ", self.roll, "\ngpa : ", self.gpa)

saif=student()
saif.roll=101
saif.gpa=4.80
saif.display()

print("\n")
ali=student()
ali.roll=102
ali.gpa=4.30
ali.display()


