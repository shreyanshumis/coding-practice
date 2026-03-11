class India():
    def capital(self):
        print("The capital of India is new Delhi.")

    def language(self):
        print("India is a diverse country which hosts a lot of language, which are over 400.")
    
    def type(self):
        print("India is a parliamentary democracy.")

class USA():
    def capital(self):
        print("The capital of USA is Washington DC.")

    def language(self):
        print("Most of the native american languages have died, so English and Spanish are the only majority spoken languages left.")

    def type(self):
        print("USA is a presidential democracy.")

obj_ind = India()
obj_usa = USA()

for country in (obj_ind, obj_usa):
    country.capital()
    country.language()
    country.type()