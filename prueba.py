
#Proyecto de prueba, trabajando con Git

numero1=int(input("Introduce el primer número: "))
numero2=int(input("Introduce el segundo número: "))

operacion=[1,2,3,4]
print("Selecciona la operación que quiera realizar: ")
print("1. Suma, 2. Resta, 3.Multiplicación, 4.División")
if operacion==1:
	Resultado=numero1+numero2
	print(Resultado)

elif operación==2:
	Resultado=numero1-numero2
	print(Resultado)
elif operacion==3:
	Resultado=numero1*numero2
	print(Resultado)
elif operacion==4:
	Resultado=numero1/numero2
	print(Resultado)