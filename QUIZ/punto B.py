import numpy as np

class Matrix:
    def __init__(self, Tamanho,):
        self.Tamanho= Tamanho
        self.matriz = [None] * (Tamanho-3)
        self.A= [None]* (Tamanho-3)
        self.pivote = 0
        self.x = 0
        self.y = 0
        self.z = 0
        self.vectora= [None] * 3
        self.vectorb= [None] * 3
        self.vectorc= [None] * 3

    def inicial(self):
        for i in range(self.Tamanho-3):
            self.matriz[i] = [None] * self.Tamanho
            self.A[i] = [None] * 4

    def ingresar(self):
        for i in range(self.Tamanho-3):
            for j in range(self.Tamanho):
                self.matriz[i][j]=float(input("ingrese un numero para la posicion ",i, j))


    def Pivote(self, i, j):
        self.pivote=self.matriz[i][j]

    def calc1(self, reglon):
        for j in range(self.Tamanho):
            self.matriz[reglon][j] = self.matriz[reglon][j] / self.pivote

    def elimincacion(self, posicion, l):

        for i in range(1+l,3):
            num = float(self.matriz[i][posicion])
            for j in range(self.Tamanho):

                self.matriz[i][j] = float(self.matriz[i][j]) - float(self.matriz[posicion][j]*num/self.pivote)

    def despejez(self,matr):
        a=matr[2][3]/matr[2][2]
        self.z=a
        print(a)
        return self.z

    def despejey(self,matr):
        b=matr[1][3]-(matr[1][2]*self.z)
        b=b/matr[1][1]
        self.y = b
        print(b)
        return self.y

    def despejex(self,matr):
        c=matr[0][3]-(matr[0][2]*self.z)-(matr[0][1]*self.y)
        c=c/matr[0][0]
        self.x = c
        print(c)
        return self.x

    def convector(self):
        for i in range(self.Tamanho-3):
            for j in range(3,self.Tamanho):
                if(i==0):
                    self.vectora[j-3]=float(self.matriz[j-3][i+3])
                elif(i==1):
                    self.vectorb[j-3]=float(self.matriz[j-3][i+3])
                else:
                    self.vectorc[j-3]=float(self.matriz[j-3][i+3])
        print (self.vectora)
        print (self.vectorb)
        print (self.vectorc)

    def conmatriz(self, aumen):
        for i in range(self.Tamanho-3):
            for j in range(self.Tamanho-2):
                if(j<3):
                    self.A[i][j]= float(self.matriz[i][j])
                else:
                    self.A[i][j] = float(aumen[i])
        print (self.A)







    def full(self):
        arr = np.array(self.matriz)
        arr1 = a = arr[:, :3]
        n = np.linalg.det(arr1)

        if (n != 0):
            print (self.matriz)

            for i in range(vector1.Tamanho):
                if (i < 3):
                    self.Pivote(i, i)

                self.elimincacion(i, i)

        else:
            print("la matriz ingresada no tiene solucion")
        print (self.matriz)
        self.convector()
        self.conmatriz(self.vectora)
        self.despejez(self.A)
        self.despejey(self.A)
        self.despejex(self.A)
        isd=[self.x,self.y,self.z]
        self.conmatriz(self.vectorb)
        self.despejez(self.A)
        self.despejey(self.A)
        self.despejex(self.A)
        esd=[self.x,self.y,self.z]
        self.conmatriz(self.vectorc)
        self.despejez(self.A)
        self.despejey(self.A)
        self.despejex(self.A)
        asd=[self.x,self.y,self.z]

        Inversa=[isd,esd,asd]
        print (Inversa)
        vectorb=[220,176,264]
        vectorX=[0,0,0]
        print ("*****************SOLUCION SEL***************")
        for i in range(3):
         resultado = 0
         for j in range(3):
            resultado += ( Inversa[j][i] * vectorb[j] )
            vectorX[i] = float(resultado)
        print (vectorX)







print ("*****************VECTOR INDEPENDIENTE 1***************")
vector1 = Matrix(6)
vector1.inicial()
vector1.matriz=[[12,20,32,1,0,0],[16,12,28,0,1,0],[8,28,38,0,0,1]]
vector1.full()
#print ("*****************VECTOR INDEPENDIENTE 2***************")
#vector2 = Matrix(4)
#vector2.inicial()
#vector2.matriz=[[12,20,32,0],[16,12,28,1],[8,28,38,0]]
#esd=vector2.full()
#print ("*****************VECTOR INDEPENDIENTE 3***************")
#vector3 = Matrix(4)
#vector3.inicial()
#vector3.matriz=[[12,20,32,0],[16,12,28,0],[8,28,38,1]]
#asd=vector3.full()
#print ("*****************MATRIZ INVERSA***************")
#Inversa=[isd,esd,asd]
#print (Inversa)
#vectorb=[220,176,264]
#vectorX=[0,0,0]
#resultado = 0
#print ("*****************SOLUCION SEL***************")
#for i in range(3):
#    resultado = 0
#    for j in range(3):
#        resultado += ( Inversa[j][i] * vectorb[j] )
#    vectorX[i] = float(resultado)


