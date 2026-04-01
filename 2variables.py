#datos se reutilizan = vaiables
a = 5
b = 3
c = a + b
print(c)# print(8)

#valor    #definicion
nombre = "marcos"
#.        #redefinicion
nombre =  "dani"
nombre = "rigoberto" # va al ultimo ya que se pueden modificar (let)
print(nombre) # print rigoberto 


#Concatenar con + y F strings
#redefinicion con sumas y resta 
numero = 10
numero += 5
numero -= 3
print(numero)#print = 12

name = "abraham"
bienvenida = "hola " + name + "?como estas"
print(bienvenida)#hola abraham como estas

# f strings convierte todo a texto como toString
tia = 4 #no es string 
saludo = f"Hola {tia} como estas"
print(saludo)#hola 4 como estas

#del = a borrar ejemplo
num = 4 
del num 
#print(num)# undefine el num

#false o true en texto estilo busqueda
negro = "joe"
molestar = "Hola" + negro + "hueles mal"
print("juan" in molestar)# false
print("juan" not in molestar)# true

#operadores de pertenencia ( in / not in )con mayuscula y minuscula
print("Joe" in molestar)#false porque es mayuscula
print("joe" in molestar)#true por que es minuscula

#Snake_case es como camel pero en vez de mayuscula para separar usa _
snake_case_de_hoy = "snake_case_guion_bajo"

#input() permite que el usuario declare la variable en string!!
nombre = input("?como te llamas")
print("un gusto " + nombre)


