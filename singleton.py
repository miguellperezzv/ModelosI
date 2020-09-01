class Singleton:
    
    def __new__(cls):

        if not hasattr(cls, 'atributo'): # Si no existe el atributo “instance”

            cls.atributo = super(Singleton, cls).__new__(cls) # Crea el atributo instancia 
            return cls.atributo
    
x = Singleton()

y = Singleton()

z= Singleton()

print("Variables iguales: ",(x is z is y)) 
print("Dirección x ", (id(x))) 
print("Dirección y ", (id(y)))
print("Dirección z ", (id(z)))
