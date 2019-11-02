import numpy as np

class Matriz:

    def __init__(self):
        self.matriz=[]
        self.matrizAd=[]
        self.matrizAdT=[]
        self.vectorb=[]
        self.vectorR=[]
        self.fila = 3
        self.columna=self.fila
        self.determinante=0

    def poblar(self):

        for i in range(int(self.fila)):
           self.matriz.append([])
           self.matrizAd.append([])
           self.matrizAdT.append([])
           self.vectorb.append([])
           self.vectorR.append([])
           self.matriz = [[12, 20, 32], [16, 12, 28], [8, 28, 38]]
           self.vectorb = [220, 176, 264]
           for j in range(int(self.columna)):
               self.matrizAd[i].append(float(1))
               self.matrizAdT[i].append(float(1))
           self.vectorR[i]=(float(1))
        Am=np.array(self.matriz)
        self.determinante=np.linalg.det(Am)

    def matrizcofactore(self):
        for i in range(self.columna):
            for j in range(self.columna):
                if(i==0):
                    if(j==0):
                        self.matrizAd[i][j]=((self.matriz[1][1]*self.matriz[2][2])-(self.matriz[1][2]*self.matriz[2][1]))
                    if(j==1):
                        self.matrizAd[i][j]=((self.matriz[1][0] * self.matriz[2][2]) - (self.matriz[2][0] * self.matriz[1][2]))*-1
                    if(j==2):
                        self.matrizAd[i][j]=((self.matriz[1][0] * self.matriz[2][1]) - (self.matriz[2][0] * self.matriz[1][1]))
                if (i == 1):
                    if (j == 0):
                        self.matrizAd[i][j]=((self.matriz[0][1] * self.matriz[2][2]) - (self.matriz[2][1] * self.matriz[0][2]))*-1
                    if (j == 1):
                        self.matrizAd[i][j]=((self.matriz[0][0] * self.matriz[2][2]) - (self.matriz[2][0] * self.matriz[0][2]))
                    if (j == 2):
                        self.matrizAd[i][j]=((self.matriz[0][0] * self.matriz[2][1]) - (self.matriz[2][0] * self.matriz[0][1]))*-1
                if (i == 2):
                    if (j == 0):
                        self.matrizAd[i][j]=((self.matriz[0][1] * self.matriz[1][2]) - (self.matriz[1][1] * self.matriz[0][2]))
                    if (j == 1):
                        self.matrizAd[i][j]=((self.matriz[0][0] * self.matriz[1][2]) - (self.matriz[1][0] * self.matriz[0][2]))*-1
                    if (j == 2):
                        self.matrizAd[i][j]=((self.matriz[0][0] * self.matriz[1][1]) - (self.matriz[1][0] * self.matriz[0][1]))

    def matrizTraspuesta(self):
        for i in range(self.columna):
            for j in range(self.columna):
                self.matrizAdT[j][i]=self.matrizAd[i][j]

    def matrizTrasXdet(self):
        for i in range(self.columna):
            for j in range(self.columna):
                self.matrizAdT[i][j]=(self.matrizAdT[i][j]/self.determinante)

    def matrizTrasXdetXvecB(self):
        for i in range(self.columna):
            resultado = 0
            for j in range(self.columna):
                resultado += (self.matrizAdT[i][j] * self.vectorb[j])
            self.vectorR[i] = float(resultado)

    def imprimir(self):
        imprimir = ""
        for i in range(self.fila):
            for j in range(self.fila):
                imprimir += str("[")
                imprimir += str(self.matriz[i][j])
                imprimir += str("]")
            imprimir +="\n"
        print(imprimir)

    def imprimiraj(self):
        imprimir = ""
        for i in range(self.fila):
            for j in range(self.fila):
                imprimir += str("[")
                imprimir += str(self.matrizAd[i][j])
                imprimir += str("]")
            imprimir +="\n"
        print(imprimir)

    def imprimirVectorX(self):
        imprimirX = ""
        for i in range(self.columna):
            imprimirX += str("[")
            imprimirX += str(self.vectorR[i])
            imprimirX += str("]")
            imprimirX += str("\n")
        print(imprimirX)

    def imprimirMatrizAdjuntaTranspuesta(self):
        imprimir = ""
        for i in range(self.fila):
            for j in range(self.fila):
                imprimir += str("[")
                imprimir += str(self.matrizAdT[i][j])
                imprimir += str("]")
            imprimir +="\n"
        print(imprimir)



print("************ADJUNTA**************")
print("*************INICIO**************")

prueba = Matriz()
prueba.poblar()

print("**********MATRIZ******************")
prueba.imprimir()
if(prueba.determinante!=0):
    print("****+*****MATRIZ ADJUNTA**********")
    prueba.matrizcofactore()
    prueba.imprimiraj()
    print("*****MATRIZ ADJUNTA TRASPUESTA****")
    prueba.matrizTraspuesta()
    prueba.imprimirMatrizAdjuntaTranspuesta()
    print("MATRIZ ADJUNTA TRASPUESTA SOBRE DET")
    prueba.matrizTrasXdet()
    prueba.imprimirMatrizAdjuntaTranspuesta()
    print("***********resultados*************")
    prueba.matrizTrasXdetXvecB()
    prueba.imprimirVectorX()
    print("**************FIN******************")
else:
    print ("El SEL NO TIENE SOLUCION O TIENE INFINITAS SOLUCIONES")