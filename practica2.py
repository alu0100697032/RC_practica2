#! /usr/bin/python
# -*- coding: utf-8 -*-
#Articulacion, tipo(ROTACION O PRISMATICA), x,y,z, desplazamiento, minimo, maximo, movilidad(movil)
def leerParametros():
    
    listaParesArticulacionLink = []
    numeroPares = int(raw_input("¿Cuantos pares articulacion-link quieres?"))
    for i in range(numeroPares):
        
        infoLink = []
        parArticulacionLink = []
        
        infoArticulacion = []
        tipo = raw_input("Introduzca tipo de articulacion: Prismatica o Roacion")
        x = raw_input("Componnte eje otacion x")
        y = raw_input("Componnte eje otacion y")
        z = raw_input("Componnte eje otacion z")
        desplazamiento = raw_input("Grados en Rotacion, distancia en Prismatica")
        minimo = raw_input("Rango minimo desplazamiento")
        maximo = raw_input("Rango maximo desplazamiento")
        movilidad = raw_input("Movilidad: movil o estatica")
        
        link = raw_input("Longitud link")
        
        infoArticulacion.append("Articulacion")
        infoArticulacion.append(tipo)
        infoArticulacion.append(x)
        infoArticulacion.append(y)
        infoArticulacion.append(z)
        infoArticulacion.append(desplazamiento)
        infoArticulacion.append(minimo)
        infoArticulacion.append(maximo)
        infoArticulacion.append(movilidad)
        
        infoLink.append("Link")
        infoLink.append(link)
        
        parArticulacionLink.append(infoArticulacion)
        parArticulacionLink.append(infoLink)
        
    string = ', '.join(listaParesArticulacionLink)
    print string
    return listaParesArticulacionLink