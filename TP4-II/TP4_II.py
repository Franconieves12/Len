# -*- coding: utf-8 -*-

from clases.perfil import Perfil
from clases.post import Post
from clases.comentario import Comentario
import datetime

lista_de_perfiles = [Perfil('0','heavy'), Perfil('1','agus'), \
                    Perfil('2','james'), Perfil('3','troilo'), \
                    Perfil('4','steve'), Perfil('5','asus'), \
                    Perfil('6','di sarli'), Perfil('7','azul'), \
                    Perfil('8','esteban'), Perfil('9','marti'), \
                    Perfil('10','cayetano'), Perfil('11','laurenz'), \
                    Perfil('12','maria'), Perfil('13','jeizet'), \
                    Perfil('14','frank'), Perfil('15','fornite_fan'), \
                    Perfil('16','minecraft_fan'),  \
                    ]

lista_de_posteos = [Post('17', lista_de_perfiles[0], 'A buenas horas, mangas verdes (ayuda a destiempo)'), \
    Post('18', lista_de_perfiles[10], 'Buscarle tres pies al gato (buscar una explicación imposible)'), \
    Post('19', lista_de_perfiles[11], 'Andar con pies de plomo (ser cauto)'), \
    Post('20', lista_de_perfiles[1] , 'Aflojar la mosca (pagar, entregar el dinero que se debe)'), \
    Post('21', lista_de_perfiles[9], 'Abrir la caja de Pandora (decisión que traerá consecuencias graves)'), \
    Post('22', lista_de_perfiles[1], 'Aquí me pongo a cantar Al compás de la vigüela, que el hombre que lo desvela una pena estrordinaria, como la ave solitaria con el cantar se consuela.'), \
    Post('23', lista_de_perfiles[2], 'Cuartito azul de mi primera pasion, vos guardaras todo mi corazón; si alguna vez, volviera la que ame vos le diras que nunca la olvide;'), \
    Post('24', lista_de_perfiles[2], 'Niebla del Riachuelo Amarrado al recuerdo Yo sigo esperando Niebla del Riachuelo De ese amor, para siempre Me vas alejando'), \
    Post('25', lista_de_perfiles[6], 'Uno busca lleno de esperanzas El camino que los sueños Prometieron a sus ansias Sabe que la lucha es cruel y es mucha Pero lucha y se desangra Por la fe que lo empecina'), \
    Post('26', lista_de_perfiles[3], 'No quiero ser alarmista pero mi padre tiene una empresa de alarmas y seguridad y la voy a heredar.'), \
    Post('27', lista_de_perfiles[10], '—Cariño, después de tantos años, ¿Todavía te gusto? —No, todavía no.'), \
    Post('28', lista_de_perfiles[7], 'Estoy conociendo a un chico muy guapo. Bueno, a lo mejor guapo guapo tampoco es. Ni es un chico. A lo mejor es un donut. De chocolate.'), \
    Post('29', lista_de_perfiles[4], 'Acabo de ver a esa mosca frotarse las manos durante veinte minutos. Es increíble con qué tonterías se entretienen las moscas.'), \
    Post('30', lista_de_perfiles[11], 'Les tengo que poner una foto que les va a fascinar... Salgo yo en Pisa y parece que sujeto la torre!'), \
    Post('31', lista_de_perfiles[8], 'Hoy hace exactamente doce años que me dijeron que era un rencoroso.'), \
    Post('32', lista_de_perfiles[5], 'En un segundo pueden pasar muchas cosas. Lo sé porque vivo en un tercero y se oye todo.'), \
    Post('33', lista_de_perfiles[1], 'A los que ponéis "haber" en lugar de "a ver". Deberíais hirviendo si solucionáis ese problema.'), \
    Post('34', lista_de_perfiles[7], '"Basado en hechos reales" quiere decir "pasó más o menos así pero todos eran mucho más feos".'), \
    Post('35', lista_de_perfiles[12], 'Solo mi cama save lo q paso anóche'), \
    Post('36', lista_de_perfiles[16], 'miren mi nueva skin!! ya komieron prros? jsjsjs'), \
    Post('37', lista_de_perfiles[13], 'Hey There! I´m Using Whatsapp! UWU.'), \
    Post('38', lista_de_perfiles[14], 'uwu.'), \
    Post('39', lista_de_perfiles[15], 'Fornite vest game butos.'), \
    Post('40', lista_de_perfiles[16], 'maldito kreepeer.')]

lista_de_comentarios=[Comentario('41', lista_de_perfiles[16]),Comentario('42', lista_de_perfiles[13]),Comentario('43', lista_de_perfiles[16]),\
                                    Comentario('44', lista_de_perfiles[13]),Comentario('45', lista_de_perfiles[13]),Comentario('46', lista_de_perfiles[13]),\
                                    Comentario('47', lista_de_perfiles[16]),Comentario('48', lista_de_perfiles[13]),Comentario('49', lista_de_perfiles[16]),\
                                    Comentario('50', lista_de_perfiles[14]),Comentario('51', lista_de_perfiles[13]),Comentario('52', lista_de_perfiles[16]),\
                                    Comentario('53', lista_de_perfiles[16]),Comentario('54', lista_de_perfiles[13]),Comentario('55', lista_de_perfiles[16]),\
                                    Comentario('56', lista_de_perfiles[13]),Comentario('57', lista_de_perfiles[16]),Comentario('58', lista_de_perfiles[13]),\
                                    Comentario('59', lista_de_perfiles[15]),Comentario('60', lista_de_perfiles[13]),Comentario('61', lista_de_perfiles[13]),\
                                    Comentario('62', lista_de_perfiles[14]),Comentario('63', lista_de_perfiles[11]),Comentario('64', lista_de_perfiles[13]),\
                                    Comentario('65', lista_de_perfiles[14]),Comentario('66', lista_de_perfiles[7]),Comentario('67', lista_de_perfiles[12]),\
                                    Comentario('68', lista_de_perfiles[9]),Comentario('69', lista_de_perfiles[8]),Comentario('70', lista_de_perfiles[14]),\
                                    Comentario('71', lista_de_perfiles[15])]
lista_de_comentarios[0].setContenido('creeper')
lista_de_comentarios[1].setContenido('aww man')
lista_de_comentarios[2].setContenido('so we back in the main')
lista_de_comentarios[3].setContenido('corregilo boludo')
lista_de_comentarios[4].setContenido('uu bueno no importa')
lista_de_comentarios[5].setContenido('creeper')
lista_de_comentarios[6].setContenido('creeper')
lista_de_comentarios[7].setContenido('lpm')
lista_de_comentarios[8].setContenido('creeper')
lista_de_comentarios[9].setContenido('draculeo')
lista_de_comentarios[10].setContenido('lpm!!!')
lista_de_comentarios[11].setContenido('crreper')
lista_de_comentarios[12].setContenido('creeper*')
lista_de_comentarios[13].setContenido('aww man')
lista_de_comentarios[14].setContenido('so we back in the mine')
lista_de_comentarios[15].setContenido('got our pickaxe swinging')
lista_de_comentarios[16].setContenido('from side to side')
lista_de_comentarios[17].setContenido('side side to side')
lista_de_comentarios[18].setContenido('creeper')
lista_de_comentarios[19].setContenido('HIJO DE PUTA')
lista_de_comentarios[20].setContenido('YA FUE ME VOY A LA MIERDA')
lista_de_comentarios[21].setContenido('SOMEbody')
lista_de_comentarios[22].setContenido('ones told me')
lista_de_comentarios[23].setContenido('no me c la canciòn we')
lista_de_comentarios[24].setContenido('matate')
lista_de_comentarios[25].setContenido('si, te measte en tu cama y tulong_perfilese que lavar las sabanas')
lista_de_comentarios[26].setContenido('mamaaaaa')
lista_de_comentarios[27].setContenido('nwn')

lista_de_posteos[23].addComentario(lista_de_comentarios[0])
lista_de_posteos[23].addComentario(lista_de_comentarios[1])
lista_de_posteos[23].addComentario(lista_de_comentarios[2])
lista_de_posteos[23].addComentario(lista_de_comentarios[3])
lista_de_posteos[23].addComentario(lista_de_comentarios[4])
lista_de_posteos[23].addComentario(lista_de_comentarios[5])
lista_de_posteos[23].addComentario(lista_de_comentarios[6])
lista_de_posteos[23].addComentario(lista_de_comentarios[7])
lista_de_posteos[23].addComentario(lista_de_comentarios[8])
lista_de_posteos[23].addComentario(lista_de_comentarios[9])
lista_de_posteos[23].addComentario(lista_de_comentarios[10])
lista_de_posteos[23].addComentario(lista_de_comentarios[11])
lista_de_posteos[23].addComentario(lista_de_comentarios[12])
lista_de_posteos[23].addComentario(lista_de_comentarios[13])
lista_de_posteos[23].addComentario(lista_de_comentarios[14])
lista_de_posteos[23].addComentario(lista_de_comentarios[15])
lista_de_posteos[23].addComentario(lista_de_comentarios[16])
lista_de_posteos[23].addComentario(lista_de_comentarios[17])
lista_de_posteos[23].addComentario(lista_de_comentarios[18])
lista_de_posteos[23].addComentario(lista_de_comentarios[19])
lista_de_posteos[23].addComentario(lista_de_comentarios[20])
lista_de_posteos[23].addComentario(lista_de_comentarios[21])
lista_de_posteos[23].addComentario(lista_de_comentarios[22])
lista_de_posteos[23].addComentario(lista_de_comentarios[23])
lista_de_posteos[23].addComentario(lista_de_comentarios[24])
lista_de_posteos[18].addComentario(lista_de_comentarios[25])
lista_de_posteos[18].addComentario(lista_de_comentarios[26])
lista_de_posteos[21].addComentario(lista_de_comentarios[27])

# comience a editar el programa desde aca hacia abajo
print("Punto 1A \n")
print("Lista de Perfiles")
x=len(lista_de_perfiles)
cont=0
while cont<x:
    a=lista_de_perfiles[cont].getalias()
    print (a + ',')
    cont+=1

#Fin del punto 1A 
print('\n')

print("Punto 2B \n")
print("Lista de posteos")
x=len(lista_de_posteos)
cont=0
while cont<x:
    a=lista_de_posteos[cont].getId()
    b=lista_de_posteos[cont].getOwner()
    c=lista_de_posteos[cont].getContenido()
    print ("Id: "+a+ " Perfil: "+b.getalias()+" Text: "+c+',')
    print('\n')
    cont+=1

#Fin del punto 2B 
print('\n')

print('Punto 3C \n')
print("Lista de Posteos por Perfil")
x=len(lista_de_perfiles)
l=len(lista_de_posteos)
cont=0
while cont<x:
    us=lista_de_perfiles[cont].getalias()
    print(us)
    f=0
    while f<l:
        idprros=lista_de_posteos[f].getOwner()
        if (idprros.getalias()==us):
            print("     "+lista_de_posteos[f].texto)      
        f=f+1
    cont+=1

#Fin del punto 3C
print('\n')

print("Punto 7G \n")

l=len(lista_de_posteos)
cont=0
print("Lista de Posts Hechos por un Perfil Ingresado por Teclado")
pro=(input("Ingrese el Nombre del Perfil "))
find= False
while cont<l:
    us=lista_de_posteos[cont].getOwner()
    if (pro==us.alias):
        propietario_post=lista_de_posteos[cont].texto
        print(propietario_post+"\n")     
        find=True
    cont+=1
if (find==False):
    print("No existe tal perfil")

#Fin del punto 7G
print('\n')

print("Punto 8H \n")

c=len(lista_de_comentarios)
cont=0
print("Lista de Comentarios Hechos en un Post por un Perfil Ingresado por Teclado")
dueño=(input("Ingrese el Nombre del Perfil "))
find= False
while cont<c:
    uscom=lista_de_comentarios[cont].getOwner()
    ala=uscom.getalias()
    if (dueño==ala):
        com=lista_de_comentarios[cont].getContenido()
        print(com)
        print("\n")     
        find=True
    cont+=1
if (find==False):
    print("No existe tal perfil o no posee comentarios")

#Fin del punto 8H
print('\n')

print("Punto 9I \n")

long_post=len(lista_de_posteos)
long_comentario=len(lista_de_comentarios)
long_perfiles=len(lista_de_perfiles)
cont_post=0
cont_coment=0
cont_perfiles=0
print("Lista de Comentarios Hechos en un Post por un Perfil Ingresado por Teclado")
dueño=(input("Ingrese el Nombre del Perfil "))
find= False


while cont_post < long_post:
    
    comentariado[cont_post] = lista_de_posteos[cont_post].getComentarios()
    duenio[cont_post]=comentariado[cont_post].getOwner()
    if duenio.alias == dueño:
        find=True
        while cont_coment<long_comentario:
            contenidoPost=lista_de_posteos[cont_post].getContenido()
            print(contenidoPost)
            print(comentariado.texto)

if (find==False):
    print("No existe tal perfil o no posee comentarios")
