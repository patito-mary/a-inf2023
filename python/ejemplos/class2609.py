class complex:
    def __init__(self, real, img):
        self.r = real
        self.i = img
    def __str__(self):
        return str(self.r)+'i'(self.i)

x = complex(6,8)
#print(f'la parte real es {x.r}, y la imaginaria {x.i}')
#print(x.r, x.i)