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
        self.funcion = 13*x**2 - 60*x + 68

        return self.funcion

    def inderivada(self,x):
        self.derivada = 26*x - 60

        return self.derivada

    def uso(self,x):
        a = float(13 * x ** 2 - 60 * x + 68) / (26 * x - 60)



    def NewtonRaphson(self):
        nwrps = ejercicio1()
        print ('1). x^2+3y=7    2). 2x+sqrt(y)=5')
        print ('metodo de Newton Raphson')
        for i in range(2):
            print ('ingrese el valor para x'+str(i)+':')
            nwrps.x = input()
            nwrps.xk = (nwrps.x - float(nwrps.infuncion(nwrps.x)) / nwrps.inderivada(nwrps.x))
            print (nwrps.xk)
            n = 0
            while n < 1:
                temp = nwrps.xk
                nwrps.xk = float(nwrps.xk - float(nwrps.infuncion(nwrps.xk)) / nwrps.inderivada(nwrps.xk))
                print (nwrps.xk)
                if (temp) == (nwrps.xk):
                    print ('STOP!!')
                    break


            print (round(nwrps.infuncion(nwrps.xk), 9))

    def RegulaFalsi(self):
        for i in range(2):
            print ('Raiz para x'+str(i)+':')
            rgfs = ejercicio1()
            print ('1). x^2+3y=7    2). 2x+sqrt(y)=5')
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
                rgfs.a = ((rgfs.a * float(rgfs.infuncion(rgfs.b)) - (rgfs.b * float(rgfs.infuncion(rgfs.a)))) / (
                            float(rgfs.infuncion(rgfs.b)) - float(rgfs.infuncion(rgfs.a))))
                print (rgfs.a)

                if round(temp, 12) == round(rgfs.a, 12):
                    print ('STOP!!')
                    break

            print (round(rgfs.infuncion(rgfs.a), 9))



Run = ejercicio1()

print ('\n --------------------------------------- \n')
Run.RegulaFalsi()
