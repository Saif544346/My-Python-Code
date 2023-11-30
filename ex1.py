class student:
    id=""
    name=""
    def __init__(self,id,name):
        self.id=id
        self.name=name
    def display(self):
        print(f"id={self.id}\nname={self.name}")
saif=student(221002108,"ibadullah saif")
saif.display()
yasir=student(221002109,"yasir ali khan")
yasir.display()



