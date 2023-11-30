class student:
    id=""
    name=""

    def setvalue(self, id, name):
        self.id = id
        self.name = name
    def display(self):
        print(f"id={self.id}  name={self.name}")


saif=student()
saif.setvalue(221002108," Golam ibadullah saif")

saif.display()