class casa:
    def __init__(self,ventanas,puertas,techo,color):
        self.ventanas = ventanas
        self.puertas = puertas
        self.techo = techo
        self.color = color

    def get_ventanas(self):
        return self.ventanas

    def set_ventanas(self, value):
        self.ventanas = value

    def get_puertas(self):
        return self.puertas

    def set_puertas(self, value):
        self.puertas = value

    def get_techo(self):
        return self.techo

    def set_techo(self, value):
        self.techo = value

    def get_color(self):
        return self.color

    def set_color(self, value):
        self.color = value
    
    def describir(self):
        print(f"casa con {self.ventanas} ventanas, {self.puertas} puertas, techo de {self.techo} y color {self.color}")

class vivienda_familiar(casa):
    def __init__(self, ventanas, puertas, techo, color, num_habitaciones):
        super().__init__(ventanas, puertas, techo, color)
        self.num_habitaciones = num_habitaciones
    
    def describir(self):
        super().describir()
        print(f"tiene {self.num_habitaciones} habitaciones ideal para familia")


class apartamento(casa):
    def __init__(self, ventanas, puertas, techo, color, piso):
        super().__init__(ventanas, puertas, techo, color)
        self.piso = piso

    def describir(self):
        super().describir()
        print(f"el piso esta ubicado en {self.piso}")

class bungalo(casa):
    def __init__(self, ventanas, puertas, techo, color, porche):
        super().__init__(ventanas, puertas, techo, color)
        self.porche = porche

    def describir(self):
        super().describir()
        if self.porche:
            print(f"incluye porce")
        else:
            print("No tiene porce")


if __name__ == "__main__":
    casa1 = vivienda_familiar(6,2,"teja","blanco",4)
    casa2 = apartamento(4,1,"concreto","gris",5)
    casa3 = bungalo(5,1,"metal","verde",True)

    casa1.describir()
    print()
    casa2.describir()
    print()
    casa3.describir()
# MiPrimerClonada2
