class Coche:
    def __init__(self, gasolina):
        self.gasolina = gasolina
        self.arrancado = False
        print ("Tenemos", gasolina, "litros")
        print ("El coche esta apagado. Pulse 5 para arrancar!")

    def arrancar(self):
        if self.gasolina > 0:
            self.arrancado = True
            print("-*- EL COCHE SE HA ARRANCADO")
        else:
            self.arrancado = False
            print("-*- EL COCHE NO SE PUEDE ARRANCAR")

    def actualizar_gasolina(self):
        self.gasolina = self.gasolina - 0.5
        print("    Cantidad gasolina: " + str(self.gasolina))
        if self.gasolina == 0:
            self.arrancado = False

    def avanza(self):
        print("-*- EL COCHE AVANZA")
        coche.actualizar_gasolina()

    def gira_izquierda(self):
        print("-*- EL COCHE GIRA A LA IZQUIERDA")

    def gira_derecha(self):
        print("-*- EL COCHE GIRA A LA DERECHA")

    def repostar_gasolina(self):
        self.gasolina = self.gasolina + 10
        print("-*- EL COCHE SE HA REPOSTADO")
        print("    Cantidad gasolina: " + str(self.gasolina))

#RQ4.- Cuando se pulse una tecla especifica el coche avanzará (SOLO CONSUME GASOLINA)?????
#RQ5.- Cuando el coche acelere consumirá gasolina.
#RQ12.- Cuando se pulse una tecla definida en el juego se mostrará un mensaje comunicando la acción realizada.

#HAY QUE HACER ALGO CUANDO GIRA APARTE DE COMUNICARLO POR PANTALLA????????????????????????

coche = Coche(1)
while True:
    accion = input("<== ")
    print()
    if accion == "5":
        coche.arrancar()
    else:
        if coche.arrancado:
            if accion == "8":
                coche.avanza()
            elif accion == "4":
                coche.gira_izquierda()
            elif accion == "6":
                coche.gira_derecha()
            elif accion == "0":
                coche.repostar_gasolina()
        else:
            print("-*- EL COCHE ESTA APAGADO")
    if coche.gasolina < 0.5:
        print()
        print("-*- -*- -*- -*- -*- -*- -*- -*- -*- -*- -*- -*-")
        print("-*-      FIN DEL JUEGO: NO HAY GASOLINA     -*-")
        print("-*- -*- -*- -*- -*- -*- -*- -*- -*- -*- -*- -*-")
        break
    print()