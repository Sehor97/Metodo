import math
class ejercicio1:

    def __init__(self):
        self.euler=math.e
        self.funcion = 0
        self.derivada = 0
        self.x = 0
        self.xk = 0
        self.a = 0
        self.b = 0

    def infuncion(self,x):
        self.funcion = self.euler**x + x

        return self.funcion

    def inderivada(self,x):
        self.derivada = self.euler**x +1

        return self.derivada

    def NewtonRaphson(self):
        nwrps = ejercicio1()
        print ('y = e^x + x')
        print ('metodo de Newton Raphson')
        print ('ingrese el valor para x0:  ')
        nwrps.x = input()
        nwrps.xk = nwrps.x - nwrps.infuncion(nwrps.x) / nwrps.inderivada(nwrps.x)
        n = 0
        while n < 1:
            temp = nwrps.xk
            nwrps.xk = nwrps.xk - nwrps.infuncion(nwrps.xk) / nwrps.inderivada(nwrps.xk)
            print (nwrps.xk)
            if round(temp, 12) == round(nwrps.xk, 12):
                print ('STOP!!')
                break

        print (round(nwrps.infuncion(nwrps.xk), 9))

    def RegulaFalsi(self):
        rgfs = ejercicio1()
        print ('y = e^x + x')
        print ('metodo de Regula Falsi')
        n = 0
        while n < 1:
            print ('ingrese el valor para a: ')
            rgfs.a = input()
            print ('ingrese el valor para b: ')
            rgfs.b = input()
            if rgfs.infuncion(rgfs.a) * rgfs.infuncion(rgfs.b) < 0:
                n = 1
            else:
                print ('Los puntos ingresados no sirven para hallar la solucion \n')

        while n < 2:
            temp = rgfs.a
            rgfs.a = ((rgfs.a * rgfs.infuncion(rgfs.b) - (rgfs.b * rgfs.infuncion(rgfs.a))) / (
                        rgfs.infuncion(rgfs.b) - rgfs.infuncion(rgfs.a)))
            print (rgfs.a)

            if round(temp, 12) == round(rgfs.a, 12):
                print ('STOP!!')
                break

        print (round(rgfs.infuncion(rgfs.a), 9))



Run = ejercicio1()
Run.NewtonRaphson()
print ('\n --------------------------------------- \n')
Run.RegulaFalsi()
