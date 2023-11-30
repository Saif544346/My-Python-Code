class student:
    id=""
    name=""
    def set_value(self,id,name):
        self.id=id
        self.name=name
    def dispaly(self):
        print(f"id= {self.id}name{self.name}")
        saif=student()
        saif.set_value(221002108,"golam ibadullah saif")
        saif.dispaly()