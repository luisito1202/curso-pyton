from datetime import datetime


print('rutina de asistencia del colegio')
tiempo_inicio = datetime.now()
print(tiempo_inicio)

nombre_materia = input('nombre de la materia:')
nombre_profesor = input('nombre del profesor:')
nombre_estudiante = input('nombre del estudiante:')

nota_1 = float(input('examen 1:'))
nota_2 = float(input('examen 2:'))
nota_3 = float(input('examen 3:'))
nota_4 = float(input('examen 4:'))

#aca se calcula la nota definitiva
nota_definitiva = (nota_1+nota_2+nota_3+nota_4)/4
nota_redondeada = round(nota_definitiva)
print('nota final:' ,nota_redondeada)

#aqui muestra lo que pasa si sacas cierta nota
if nota_redondeada>=10  :
    print('felicitaciones')
    print('pasaste :)')

else:
    print('debes seguir practicando')
    print('lo siento :(')

if nota_redondeada>=17  :
    print('wow me sorprendiste')
    print('enserio eres sobresaliente')

if nota_redondeada<=5   :
    print('wow enserio no estudiaste nada')
    print('nos vemos en reparacion ;)')

tiempo_final = datetime.now()
print(tiempo_final)
tiempo_rutina = (tiempo_final-tiempo_inicio)
print('pasaron:')
print(tiempo_rutina)
print(tiempo_rutina.seconds,'segundos')
