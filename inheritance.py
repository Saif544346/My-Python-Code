class iphone:
    def call(self):
        print("call i phone")
    def message(self):
        print("message i phone")
    def photo(self):
        print("take a photo")
class redmi(iphone):
    def call(self):
        print("call redmi")
    def message(self):
        print("massege redmi")



i=iphone()
i.call()
i.message()
r=redmi()
r.photo()
