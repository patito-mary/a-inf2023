class Persona():
    """Almacenamiento de personas"""
    def __init__(self):
        self.items = 0
        self.tlocal = 0 
# Agregar tiempo de espera a cliente?
class Validador(Persona):
    """Las personas que se encargan de validar dentro del super"""
    def __init__(self, timescale=10):
        """Este timescale corresponde a la cantidad de segundo que se demora
        en validarse cada item. Esto es, hacer 'pip', mover y embolsar"""
        self.validscale = timescale
        self.validtime = 0

    def get_items(self, nitems):
        self.items = nitems
        self.validtime = nitems*self.validscale

    def validar(self, dt):
        while (dt > 0 and self.validtime > 0):
            self.validtime -= 1 
            dt -= 1
        return dt


    
