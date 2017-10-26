"""
********************************************************************* 

Instituto Tecnológico de Costa Rica 

    Ingeniería en Computadores

 Lenguaje: Python 3.5.1

 Autor: Esteban Agüero Pérez

 Versión: 1.0

 Fecha Última Modificación: Octubre 24/2016

 Adivina quien, pokemones

***********************************************************************
"""
listaPokemons=[]
sizeLista=0
def cargarArchivo():
    global listaPokemons, sizeLista
    listaPokemons=[]
    caracteristicas=["nombre","numero","especie","tipo1","tipo2","habilidad","habilidad oculta","peso","altura","prob macho","prob hembra","habitat","color","lvl evolucion","piedra evolutiva","mega evolucion","crecimiento","ratio captura","ciclos eclosion","salud","ataque","defensa","ataque especial","def especial","velocidad"]
    try:
        ubicacion=input(">Ingrese la ubicación del archivo -")
        archivo=open(ubicacion,'r+')
        lista=[]
        for linea in archivo:
            pokemon=[]
            palabra=""
            for letra in linea:
                if letra=="," or letra=="\n":
                    pokemon.append(palabra)
                    palabra=""    
                elif letra!=",":
                    palabra+=letra 
            lista.append(pokemon)
        pokemon={}
        for poke in lista:
            i=0
            while i<len(caracteristicas):
                pokemon[caracteristicas[i]]=poke[i]
                i+=1
            listaPokemons.append(pokemon)
            pokemon={}
        archivo.close()
        sizeLista=len(listaPokemons)
        return 0
    except:
        print ("Archivo no encontrado")
        return 1

#QUITAR PRINTS
def buscarPokemon(caracteristica,valor):
    global listaPokemons
    i=0
    while i<len(listaPokemons):
        if listaPokemons[i][caracteristica]==valor:
            break
    return i

def juego():
    global listaPokemons,sizeLista
    listaPivote=[]
    print(""">>>Piensa en un Pokemon<<<
""")
    p1=input("¿De qué color es el pokemon? -")
    for pokemon in listaPokemons:
        if p1=="":
            listaPivote.append(pokemon)
        elif pokemon["color"].upper()!=p1.upper():
            pass
        else:
            listaPivote.append(pokemon)
    listaPokemons=listaPivote
    listaPivote=[]
    if len(listaPokemons)==1:
        print("El pokemon en que pensó es "+listaPokemons[0]["nombre"])
        return True
    
    p2=input("¿Qué especie es tu pokemon? -")
    for pokemon in listaPokemons:
        if p2=="":
            listaPivote.append(pokemon)
        elif pokemon["especie"].upper()!=p2.upper():
            pass
        else:
            listaPivote.append(pokemon)
    listaPokemons=listaPivote
    listaPivote=[]
    if len(listaPokemons)==1:
        print("El pokemon en que pensó es "+listaPokemons[0]["nombre"])
        return True
        
    p3=input("¿El pokemon tiene más de un tipo? (Si/No) -")
    if p3=="Si" or p3=="si" or p3=="SI" or p3=="sí" or p3=="Sí":
        for pokemon in listaPokemons:
            if p2=="":
                listaPivote.append(pokemon)
            elif pokemon["tipo2"]!="N/A":
                listaPivote.append(pokemon)
            else:
                pass
    elif p3=="No" or p3=="no" or p3=="NO":
        for pokemon in listaPokemons:
            if p3=="":
                listaPivote.append(pokemon)
            elif pokemon["tipo2"]=="N/A":
                listaPivote.append(pokemon)
            else:
                pass
    else:
        listaPivote=listaPokemons
    listaPokemons=listaPivote
    listaPivote=[]
    if len(listaPokemons)==1:
        print("El pokemon en que pensó es "+listaPokemons[0]["nombre"])
        return True
        
    p4=input("¿El pokemon tiene nivel de evolución? (Si/No) -")
    if p4=="":
        listaPivote=listaPokemons
    elif p4=="Si" or p4=="si" or p4=="SI" or p4=="sí" or p4=="Sí":
        for pokemon in listaPokemons:
            if pokemon["lvl evolucion"]=="N/A":
                pass
            else:
                listaPivote.append(pokemon)
        listaPokemons=listaPivote
        listaPivote=[]
        p41=input("¿El nivel de evolución del pokemon estan entre a)0-9 b)10-19 c)20-29 d)30-39? -")
        if p41=="a":
            for pokemon in listaPokemons:
                if float(pokemon["lvl evolucion"])<=9:
                    listaPivote.append(pokemon)
                else:
                    pass        
        elif p41=="b":
            for pokemon in listaPokemons:
                if 10<=float(pokemon["lvl evolucion"])<=19:
                    listaPivote.append(pokemon)
                else:
                    pass
        elif p41=="c":
            for pokemon in listaPokemons:
                if 20<=float(pokemon["lvl evolucion"])<=29:
                    listaPivote.append(pokemon)
                else:
                    pass
        elif p41=="d":
            for pokemon in listaPokemons:
                if 30<=float(pokemon["lvl evolucion"])<=39:
                    listaPivote.append(pokemon)
                else:
                    pass 
        else:
            listaPivote=listaPokemons
        
    elif p4=="No" or p4=="no" or p4=="NO":
        for pokemon in listaPokemons:
            if pokemon["lvl evolucion"]!="N/A":
                pass
            else:
                listaPivote.append(pokemon)
    else:
        listaPivote=listaPokemons
    listaPokemons=listaPivote
    listaPivote=[]
    if len(listaPokemons)==1:
        print("El pokemon en que pensó es "+listaPokemons[0]["nombre"])
        return True
        
    p5=input("¿Su pokemon evoluciona con piedra evolutiva? (Si/No) -")
    if p5=="Si" or p5=="si" or p5=="SI" or p5=="sí" or p5=="Sí":
        for pokemon in listaPokemons:
            if pokemon["piedra evolutiva"]=="Si":
                listaPivote.append(pokemon)
            else:
                pass
    elif p5=="NO" or p5=="No" or p5=="no":
        for pokemon in listaPokemons:
            if pokemon["piedra evolutiva"]=="No":
                listaPivote.append(pokemon)
            else:
                pass
    else:
        listaPivote=listaPokemons
    listaPokemons=listaPivote
    listaPivote=[]
    if len(listaPokemons)==1:
        print("El pokemon en que pensó es "+listaPokemons[0]["nombre"])
        return True
        
    p6=input("¿Su pokemon tiene mega evolución? (Si/No) -")
    if p6=="Si" or p6=="si" or p6=="SI" or p6=="sí" or p6=="Sí":
        for pokemon in listaPokemons:
            if pokemon["mega evolucion"]=="Si":
                listaPivote.append(pokemon)
            else:
                pass
    elif p6=="NO" or p6=="No" or p6=="no":
        for pokemon in listaPokemons:
            if pokemon["mega evolucion"]=="No":
                listaPivote.append(pokemon)
            else:
                pass
    else:
        listaPivote=listaPokemons
    listaPokemons=listaPivote
    listaPivote=[]
    if len(listaPokemons)==1:
        print("El pokemon en que pensó es "+listaPokemons[0]["nombre"])
        return True
        
    p7=input("¿Qué crecimiento tiene su pokemon? -")
    for pokemon in listaPokemons:
        if p7=="":
            listaPivote.append(pokemon)    
        elif pokemon["crecimiento"].upper()!=p7.upper():
            pass
        else:
            listaPivote.append(pokemon)    
    listaPokemons=listaPivote
    listaPivote=[]
    if len(listaPokemons)==1:
        print("El pokemon en que pensó es "+listaPokemons[0]["nombre"])
        return True
        
    p8=input("¿Qué habilidad tiene su pokemon? -")
    for pokemon in listaPokemons:
        if p8=="":
            listaPivote.append(pokemon)
        elif pokemon["habilidad"].upper()!=p8.upper():
            pass
        else:
            listaPivote.append(pokemon)    
    listaPokemons=listaPivote
    listaPivote=[]
    if len(listaPokemons)==1:
        print("El pokemon en que pensó es "+listaPokemons[0]["nombre"])
        return True
        
    p9=input("¿Que habitat tiene su pokemon? -")
    for pokemon in listaPokemons:
        if p9=="":
            listaPivote.append(pokemon)    
        elif pokemon["habitat"].upper()!=p9.upper():
            pass
        else:
            listaPivote.append(pokemon)    
    listaPokemons=listaPivote
    listaPivote=[]
    if len(listaPokemons)==1:
        print("El pokemon en que pensó es "+listaPokemons[0]["nombre"])
        return True
        
    p10=input("El rango de puntos de salud del pokemon esta en: a)0-19 b)20-39 c)40-59 d)60-79 e)Mayor a 80 -")
    if p10=="a":
        for pokemon in listaPokemons:
            if float(pokemon["salud"])<=19:
                listaPivote.append(pokemon)
            else:
                pass        
    elif p10=="b":
        for pokemon in listaPokemons:
            if 20<=float(pokemon["salud"])<=39:
                listaPivote.append(pokemon)
            else:
                pass
    elif p10=="c":
        for pokemon in listaPokemons:
            if 40<=float(pokemon["salud"])<=59:
                listaPivote.append(pokemon)
            else:
                pass
    elif p10=="d":
        for pokemon in listaPokemons:
            if 60<=float(pokemon["salud"])<=79:
                listaPivote.append(pokemon)
            else:
                pass
    elif p10=="e":
        for pokemon in listaPokemons:
            if 80<=float(pokemon["salud"]):
                listaPivote.append(pokemon)
            else:
                pass
    else:
        listaPivote=listaPokemons
    listaPokemons=listaPivote
    listaPivote=[]
    if len(listaPokemons)==1:
        print("El pokemon en que pensó es "+listaPokemons[0]["nombre"])
        return True
        
    p11=input("El rango de puntos de ataque del pokemon esta en: a)0-19 b)20-39 c)40-59 d)60-79 e)Mayor a 80 -")
    if p11=="a":
        for pokemon in listaPokemons:
            if float(pokemon["ataque"])<=19:
                listaPivote.append(pokemon)
            else:
                pass        
    elif p11=="b":
        for pokemon in listaPokemons:
            if 20<=float(pokemon["ataque"])<=39:
                listaPivote.append(pokemon)
            else:
                pass
    elif p11=="c":
        for pokemon in listaPokemons:
            if 40<=float(pokemon["ataque"])<=59:
                listaPivote.append(pokemon)
            else:
                pass
    elif p11=="d":
        for pokemon in listaPokemons:
            if 60<=float(pokemon["ataque"])<=79:
                listaPivote.append(pokemon)
            else:
                pass
    elif p11=="e":
        for pokemon in listaPokemons:
            if 80<=float(pokemon["ataque"]):
                listaPivote.append(pokemon)
            else:
                pass
    else:
        listaPivote=listaPokemons
    listaPokemons=listaPivote
    listaPivote=[]
    if len(listaPokemons)==1:
        print("El pokemon en que pensó es "+listaPokemons[0]["nombre"])
        return True

    p12=input("El rango de puntos de defensa del pokemon esta en: a)0-19 b)20-39 c)40-59 d)60-79 e)Mayor a 80 -")
    if p12=="a":
        for pokemon in listaPokemons:
            if float(pokemon["defensa"])<=19:
                listaPivote.append(pokemon)
            else:
                pass        
    elif p12=="b":
        for pokemon in listaPokemons:
            if 20<=float(pokemon["defensa"])<=39:
                listaPivote.append(pokemon)
            else:
                pass
    elif p12=="c":
        for pokemon in listaPokemons:
            if 40<=float(pokemon["defensa"])<=59:
                listaPivote.append(pokemon)
            else:
                pass
    elif p12=="d":
        for pokemon in listaPokemons:
            if 60<=float(pokemon["defensa"])<=79:
                listaPivote.append(pokemon)
            else:
                pass
    elif p12=="e":
        for pokemon in listaPokemons:
            if 80<=float(pokemon["defensa"]):
                listaPivote.append(pokemon)
            else:
                pass
    else:
        listaPivote=listaPokemons
    listaPokemons=listaPivote
    listaPivote=[]
    if len(listaPokemons)==1:
        print("El pokemon en que pensó es "+listaPokemons[0]["nombre"])
        return True

    p13=input("El rango de puntos de ataque especial del pokemon esta en: a)0-19 b)20-39 c)40-59 d)60-79 e)Mayor a 80 -")
    if p13=="a":
        for pokemon in listaPokemons:
            if float(pokemon["ataque especial"])<=19:
                listaPivote.append(pokemon)
            else:
                pass        
    elif p13=="b":
        for pokemon in listaPokemons:
            if 20<=float(pokemon["ataque especial"])<=39:
                listaPivote.append(pokemon)
            else:
                pass
    elif p13=="c":
        for pokemon in listaPokemons:
            if 40<=float(pokemon["ataque especial"])<=59:
                listaPivote.append(pokemon)
            else:
                pass
    elif p13=="d":
        for pokemon in listaPokemons:
            if 60<=float(pokemon["ataque especial"])<=79:
                listaPivote.append(pokemon)
            else:
                pass
    elif p13=="e":
        for pokemon in listaPokemons:
            if 80<=float(pokemon["ataque especial"]):
                listaPivote.append(pokemon)
            else:
                pass
    else:
        listaPivote=listaPokemons
    listaPokemons=listaPivote
    listaPivote=[]
    if len(listaPokemons)==1:
        print("El pokemon en que pensó es "+listaPokemons[0]["nombre"])
        return True

    p14=input("El rango de puntos de defensa especial del pokemon esta en: a)0-19 b)20-39 c)40-59 d)60-79 e)Mayor a 80 -")
    if p14=="a":
        for pokemon in listaPokemons:
            if float(pokemon["def especial"])<=19:
                listaPivote.append(pokemon)
            else:
                pass        
    elif p14=="b":
        for pokemon in listaPokemons:
            if 20<=float(pokemon["def especial"])<=39:
                listaPivote.append(pokemon)
            else:
                pass
    elif p14=="c":
        for pokemon in listaPokemons:
            if 40<=float(pokemon["def especial"])<=59:
                listaPivote.append(pokemon)
            else:
                pass
    elif p14=="d":
        for pokemon in listaPokemons:
            if 60<=float(pokemon["def especial"])<=79:
                listaPivote.append(pokemon)
            else:
                pass
    elif p14=="e":
        for pokemon in listaPokemons:
            if 80<=float(pokemon["def especial"]):
                listaPivote.append(pokemon)
            else:
                pass
    else:
        listaPivote=listaPokemons
    listaPokemons=listaPivote
    listaPivote=[]
    if len(listaPokemons)==1:
        print("El pokemon en que pensó es "+listaPokemons[0]["nombre"])
        return True

    p15=input("El rango de puntos de velocidad del pokemon esta en: a)0-19 b)20-39 c)40-59 d)60-79 e)Mayor a 80 -")
    if p15=="a":
        for pokemon in listaPokemons:
            if float(pokemon["velocidad"])<=19:
                listaPivote.append(pokemon)
            else:
                pass        
    elif p15=="b":
        for pokemon in listaPokemons:
            if 20<=float(pokemon["velocidad"])<=39:
                listaPivote.append(pokemon)
            else:
                pass
    elif p15=="c":
        for pokemon in listaPokemons:
            if 40<=float(pokemon["velocidad"])<=59:
                listaPivote.append(pokemon)
            else:
                pass
    elif p15=="d":
        for pokemon in listaPokemons:
            if 60<=float(pokemon["velocidad"])<=79:
                listaPivote.append(pokemon)
            else:
                pass
    elif p15=="e":
        for pokemon in listaPokemons:
            if 80<=float(pokemon["velocidad"]):
                listaPivote.append(pokemon)
            else:
                pass
    else:
        listaPivote=listaPokemons
    listaPokemons=listaPivote
    listaPivote=[]
    if sizeLista==len(listaPokemons):
        print("Pokemon no encontrado, no brindó información suficiente")
    elif listaPokemons==[]:
        print("Pokemon no encontrado, el pokemon descrito no existe")
    elif len(listaPokemons)==1:
        print("El pokemon en que pensó es "+listaPokemons[0]["nombre"])
        
while True:
    if cargarArchivo()!=1:        
        juego()
        continuar=input(">¿Desea volver a jugar? (Si/No)-")
        if continuar=="si" or continuar=="Si" or continuar=="SI":
            pass
        elif continuar =="no" or continuar=="No" or continuar=="NO":
            break
    else:
        pass
