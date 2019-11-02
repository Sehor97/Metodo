

class Matriz:

    def __init__(self):
        self.matriz=[]
        self.matrizId=[]
        self.vectorb=[]
        self.vectorX=[]
        self.fila = int(input("ingrese numero de filas"))
        self.columna=self.fila

    def poblar(self):
        for i in range(int(self.fila)):
           self.matriz.append([])
           self.vectorb.append([])
           self.vectorX.append([])
           for j in range(int(self.columna)):
               self.matriz[i].append(float(input("ingrese valor para la posicion:")))
           self.vectorb[i]=(float(input("ingresar valor para vector b:")))

    def poblarMatrizId(self):
        for i in range(int(self.fila)):
           self.matrizId.append([])
           for j in range(int(self.columna)):
               if(i==j):
                  self.matrizId[i].append(float(1))
               if(i!=j):
                  self.matrizId[i].append(float(0))

    def imprimir(self):
        imprimir = ""
        for i in range(self.fila):
            for j in range(self.fila):
                imprimir += str("[")
                imprimir += str(self.matriz[i][j])
                imprimir += str("]")
            imprimir +="|"
            for k in range(self.fila):
                imprimir += str("[")
                imprimir += str(self.matrizId[i][k])
                imprimir += str("]")
            imprimir += "\n"
        print(imprimir)

    def operaciones_entre_reglones(self, R_inicio,R_fin):
        valor =(self.matriz[R_fin][R_inicio]*-1)
        for i in range(self.columna):
            self.matriz[R_fin][i] = self.matriz[R_fin][i]+(self.matriz[R_inicio][i]*valor)
            self.matrizId[R_fin][i] = self.matrizId[R_fin][i]+(self.matrizId[R_inicio][i]*valor)


    def pibote(self, i):
        numero = float(self.matriz[i][i])
        for k in range(self.columna):
            self.matriz[i][k] = (self.matriz[i][k]/numero)
            self.matrizId[i][k] = (self.matrizId[i][k]/numero)


    def gauus_jordan(self):
        for i in range(self.columna):
            self.pibote(i)
            for j in range(self.columna):
                if(i!=j):
                 self.operaciones_entre_reglones(i,j)

    def productoAxX(self):
        resultado=0
        for i in range(self.columna):
            resultado=0
            for j in range(self.columna):
                resultado+= (self.matrizId[i][j]*self.vectorb[j])
            self.vectorX[i]=float(resultado)

    def imprimirVectorX(self):
        imprimirX=""
        for i in range(self.columna):
            imprimirX += str("[")
            imprimirX += str(self.vectorX[i])
            imprimirX += str("]")
            imprimirX += str("\n")
        print(imprimirX)

    def imprimirVectorb(self):
        imprimirb=""
        for i in range(self.columna):
            imprimirb += str("[")
            imprimirb += str(self.vectorb[i])
            imprimirb += str("]")
            imprimirb += str("\n")
        print(imprimirb)

    def imprimir_resultado(self):
        imprimirResult=""
        imprimirResult += "A="+str(self.vectorX[0])+"\n"
        imprimirResult += "B=" +str(self.vectorX[1])+ "\n"
        imprimirResult += "C=" + str(self.vectorX[2])+ "\n"
        print(imprimirResult)


print("*********GAUSS-JORDAN**********")
print("*********INICIO**********")
prueba = Matriz()
prueba.poblar()
print("***********************")
prueba.poblarMatrizId()
prueba.imprimir()
print("*******Vector b********")
prueba.imprimirVectorb()
print("***********************")
prueba.gauus_jordan()
prueba.imprimir()
print("******vectorX**********")
prueba.productoAxX()
prueba.imprimirVectorX()
print("******Resultados*******")
prueba.imprimir_resultado()
print("*********FIN*********")