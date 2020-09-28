import csv 

lista_datos_exp_imp = [] #tabla general
exp_sl = [] #tabla de importaciones
imp_sl = [] #tabla de exportaciones

contador = 0

#abrir el archivo 
with open("Synergy_Logistics_imp_exp.csv", "r") as archivo_csv:
    lector = csv.reader(archivo_csv)
    
    for linea in lector:
        lista_datos_exp_imp.append(linea)

#Definición de funciones (contador de rutas, contador de transporte, contador de productos, y valor total de exportaciones e importaciones )
#contador de rutas
def rutas(direction):
    rutas_a_contar = []
    conteo_rutas = []
    contador_rutas = 0   
    for ruta in lista_datos_exp_imp:
        if ruta[1] == direction:
            ruta_actual = [ruta[2],ruta[3]]            
            if ruta_actual not in rutas_a_contar:
                for registro in lista_datos_exp_imp:
                    if ruta_actual == [registro[2],registro[3]]:
                        contador_rutas += 1                
                rutas_a_contar.append(ruta_actual)
                conteo_rutas.append([ruta[2],ruta[3],contador_rutas])                
                contador_rutas = 0
    return(conteo_rutas)  
#contador de transporte
def transporte(direction):
    transporte_a_contar = []
    conteo_transporte = []
    contador_transporte = 0
    for transporte in lista_datos_exp_imp:
        if transporte[1] == direction:
            trans_actual = [transporte[7]]
            if trans_actual not in transporte_a_contar:
                for registro in lista_datos_exp_imp:
                    if trans_actual == [registro[7]]:
                        contador_transporte += 1
                transporte_a_contar.append(trans_actual)
                conteo_transporte.append([transporte[7],contador_transporte])
                contador_transporte = 0
    return(conteo_transporte)    
#contador de producto
def producto(direction):
    producto_a_contar = []
    conteo_producto = []
    contador_producto = 0
    for producto in lista_datos_exp_imp:
        if producto[1] == direction:
            prod_actual = [producto[6]]
            if prod_actual not in producto_a_contar:
                for registro in lista_datos_exp_imp:
                    if prod_actual == [registro[6]]:
                        contador_producto += 1
                producto_a_contar.append(prod_actual)
                conteo_producto.append([producto[6],contador_producto])
                contador_producto = 0
    return(conteo_producto) 
# print(producto("Exports"))


#Valor total de las exportaciones/importaciones
#EXPORTACIONAES
def valor_total_exports(direction):
    pais_a_contar_exports = []
    conteo_pais_exports = []
    contador_pais_exports = 0  
    for pais in lista_datos_exp_imp:
        if pais[1] == direction:
            ruta_actual = [pais[2]]
            if ruta_actual not in pais_a_contar_exports:
                for registro in lista_datos_exp_imp:
                    if ruta_actual == [registro[2]]:
                        contador_pais_exports += int(pais[9])
                pais_a_contar_exports.append(ruta_actual)
                conteo_pais_exports.append([pais[2],contador_pais_exports])                
                contador_pais_exports = 0
    return(conteo_pais_exports)

#IMPORTACIONES
def valor_total_imports(direction):
    pais_a_contar_imports = []
    conteo_pais_imports = [] 
    contador_pais_imports = 0

    for pais in lista_datos_exp_imp:
        if pais[1] == direction:
            ruta_actual = [pais[3]]
            if ruta_actual not in pais_a_contar_imports:
                for registro in lista_datos_exp_imp:
                    if ruta_actual == [registro[3]]:
                        contador_pais_imports += int(pais[9])
                pais_a_contar_imports.append(ruta_actual)
                conteo_pais_imports.append([pais[3],contador_pais_imports])                
                contador_pais_imports = 0     
    return(conteo_pais_imports) 




#Primer menú de opciones
print("\n¡Bienvenido!")
#seleccion1 = int(input(" 1. Importaciones\n 2. Exportaciones\n 3. Rutas de exportación más demandadas\n 4. Rutas de importación más demandadas\n 5. Rutas de exportación menos demandadas\n 6. Rutas de importación menos demandadas\n 7. Medio de transporte más demandado(general)\n 8. Medio de transporte menos demandado(general)\n 9. Medio de transporte más demandado(Exportaciones)\n 10. Medio de transporte menos demandado(Exportaciones)\n 11. Medio de transporte más demandado(Importaciones)\n 12. Medio de transporte menos demandado(Importaciones)\n Selecciona una opción (1-12): "))
seleccion1 = int(input(" 1. EXPORTACIONES\n 2. IMPORTACIONES\n Selecciona una opción (1-2): "))
if seleccion1 == 1:
    print("\nEXPORTACIONES")
    seleccion2 = int(input(" 1. Rutas mas demandadas\n 2. Rutas menos demandadas\n 3. Medio de transporte mas demandado\n 4. Medio de transporte menos demandado\n 5. Productos mas demandados\n 6. Productos menos demandados\n 7. Valor total de exportaciones\n 8. Países con el 80% del valor total de exportaciones\n Seleccione una opción (1-8): "))
    #Consultas de segundo menú        
    if seleccion2 == 1: #las 10 rutas más demandadas
        datos = rutas("Exports")  
        cuenta_demanda = 0
        datos.sort(reverse = True, key = lambda x:x[2])
        for mas_demanda in datos:
            if cuenta_demanda <= 9:
                print((cuenta_demanda + 1),mas_demanda)
                cuenta_demanda += 1                
    elif seleccion2 == 2: #las 10 rutas menos demandadas
        datos = rutas("Exports")  
        datos.sort(key = lambda x:x[2]) 
        cuenta_demanda = 0
        for menos_demanda in datos:
            if cuenta_demanda <= 9:
                print((cuenta_demanda + 1),menos_demanda)
                cuenta_demanda += 1 
    elif seleccion2 == 3: #Los tres medio de transporte mas demandado
        dato_medio = transporte("Exports")
        dato_medio.sort(reverse = True, key = lambda x:x[1])
        cuenta_demanda = 0
        for menos_demanda in dato_medio:
            if cuenta_demanda <= 2:
                print((cuenta_demanda + 1),menos_demanda)
                cuenta_demanda += 1 
    elif seleccion2 == 4: #El medio de transporte menos demandado
        dato_medio = transporte("Exports")
        dato_medio.sort(key = lambda x:x[1])
        cuenta_demanda = 0
        for menos_demanda in dato_medio:
            if cuenta_demanda <= 0:
                print((cuenta_demanda + 1),menos_demanda)
                cuenta_demanda += 1 
    elif seleccion2 == 5: #Los 5 productos mas demandados
        cuenta_demanda = 0
        prod = producto("Exports")
        prod.sort(reverse = True, key = lambda x:x[1])
        for mas_demanda in prod:
            if cuenta_demanda <= 4:
                print((cuenta_demanda + 1),mas_demanda)
                cuenta_demanda += 1         
    elif seleccion2 == 6: #Los 5 productos menos demandado
        cuenta_demanda = 0
        prod = producto("Exports")
        prod.sort(key = lambda x:x[1])
        for menos_demanda in prod:
            if cuenta_demanda <= 4:
                print((cuenta_demanda + 1),menos_demanda)
                cuenta_demanda += 1 
    elif seleccion2 == 7: #Valor total de exportaciones
        suma = 0 
        valor_exportaciones = valor_total_exports("Exports")
        valor_exportaciones.sort(reverse = True, key = lambda x:x[1])
        for registro in valor_exportaciones:
            suma += registro[1]    
        print("El valor total de las exportaciones es de: $",suma)
    elif seleccion2 == 8: #Países con el 80% de exportaciones
        suma = 0 
        suma_porc = 0
        paises_80_porciento = []
        valor_exportaciones = valor_total_exports("Exports")
        valor_exportaciones.sort(reverse = True, key = lambda x:x[1])
        for registro in valor_exportaciones:
            suma += registro[1]        
        porcentaje80 = suma*.8 #el 80% de las exportaciones 
        #para obtener los países que han exportado el 80% del valor total de las exportaciones
        for registro in valor_exportaciones: 
            pais = [registro[0]]
            if pais not in paises_80_porciento:
                for dato in valor_exportaciones:
                    if pais == [dato[0]]:
                        suma_porc += dato[1]
                        pais_nombre = dato[0]
                        if suma_porc <= porcentaje80:
                            paises_80_porciento.append(pais_nombre)
        print("Los países que generan el 80% de las exportaciones son:",paises_80_porciento)
    else: 
        print("Selección inválida")
elif seleccion1 ==2:
    print("\nIMPORTACIONES")
    seleccion2 = int(input(" 1. Rutas mas demandadas\n 2. Rutas menos demandadas\n 3. Medio de transporte mas demandado\n 4. Medio de transporte menos demandado\n 5. Productos mas demandados\n 6. Productos menos demandados\n 7. Valor total de importaciones\n 8. Países con el 80% del valor total de importaciones\n Seleccione una opción (1-8): "))
    #Consultas de segundo menú        
    if seleccion2 == 1: #las 10 rutas más demandadas
        datos = rutas("Imports")  
        cuenta_demanda = 0
        datos.sort(reverse = True, key = lambda x:x[2])
        for mas_demanda in datos:
            if cuenta_demanda <= 9:
                print((cuenta_demanda + 1),mas_demanda)
                cuenta_demanda += 1                
    elif seleccion2 == 2: #las 10 rutas menos demandadas
        datos = rutas("Imports")  
        datos.sort(key = lambda x:x[2]) 
        cuenta_demanda = 0
        for menos_demanda in datos:
            if cuenta_demanda <= 9:
                print((cuenta_demanda + 1),menos_demanda)
                cuenta_demanda += 1 
    elif seleccion2 == 3: #Los tres medio de transporte mas demandado
        dato_medio = transporte("Imports")
        dato_medio.sort(reverse = True, key = lambda x:x[1])
        cuenta_demanda = 0
        for menos_demanda in dato_medio:
            if cuenta_demanda <= 2:
                print((cuenta_demanda + 1),menos_demanda)
                cuenta_demanda += 1 
    elif seleccion2 == 4: #El medio de transporte menos demandado
        dato_medio = transporte("Imports")
        dato_medio.sort(key = lambda x:x[1])
        cuenta_demanda = 0
        for menos_demanda in dato_medio:
            if cuenta_demanda <= 0:
                print((cuenta_demanda + 1),menos_demanda)
                cuenta_demanda += 1 
    elif seleccion2 == 5: #Los 5 productos mas demandados
        cuenta_demanda = 0
        prod = producto("Imports")
        prod.sort(reverse = True, key = lambda x:x[1])
        for mas_demanda in prod:
            if cuenta_demanda <= 4:
                print((cuenta_demanda + 1),mas_demanda)
                cuenta_demanda += 1         
    elif seleccion2 == 6: #Los 5 productos menos demandado
        cuenta_demanda = 0
        prod = producto("Imports")
        prod.sort(key = lambda x:x[1])
        for menos_demanda in prod:
            if cuenta_demanda <= 4:
                print((cuenta_demanda + 1),menos_demanda)
                cuenta_demanda += 1 
    elif seleccion2 == 7: #Valor total de importaciones
        suma = 0 
        valor_exportaciones = valor_total_exports("Imports")
        valor_exportaciones.sort(reverse = True, key = lambda x:x[1])
        for registro in valor_exportaciones:
            suma += registro[1]    
        print("El valor total de las importaciones es de: $",suma)
    elif seleccion2 == 8: #Países con el 80% de importaciones
        #para obtener los países que han importado el 80% del valor total de las exportaciones
        suma = 0 
        suma_porc = 0
        paises_80_porciento = []
        valor_importaciones = valor_total_imports("Imports")
        valor_importaciones.sort(reverse = True, key = lambda x:x[1])
        for registro in valor_importaciones:
            suma += registro[1]        
        porcentaje80 = suma*.8 #el 80% de las exportaciones 
        #para obtener los países que han exportado el 80% del valor total de las exportaciones
        for registro in valor_importaciones: 
            pais = [registro[0]]
            if pais not in paises_80_porciento:
                for dato in valor_importaciones:
                    if pais == [dato[0]]:
                        suma_porc += dato[1]
                        pais_nombre = dato[0]
                        if suma_porc <= porcentaje80:
                            paises_80_porciento.append(pais_nombre)
        print("Los países que generan el 80% de las importaciones son:",paises_80_porciento)
    else: 
        print("Selección inválida")
else:
    print("Selección inválida")
    