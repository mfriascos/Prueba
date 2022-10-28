from calcular_bandejas import calcular_bandejas

def clasificacion_huevos(list_eggs):
    
    categorie_a = [i for i in list_eggs if i>=53 and i<60]
    total_a = len(categorie_a)
    print(f'Tipo_huevos: A, numero_huevos: {total_a}, numero_bandejas: {calcular_bandejas(total_a,30)}')
    
    categorie_aa = [i for i in list_eggs if i>=60 and i<67]
    total_aa = len(categorie_aa)
    print(f'Tipo_huevos: AA, numero_huevos: {total_aa}, numero_bandejas: {calcular_bandejas(total_aa,24)}')

    categorie_aaa = [i for i in list_eggs if i>=67]
    total_aaa = len(categorie_aaa)
    print(f'Tipo_huevos: AAA, numero_huevos: {total_aaa}, numero_bandejas: {calcular_bandejas(total_aaa,12)}')

    categorie_bc = [i for i in list_eggs if i<53]
    total_bc = len(categorie_bc)
    print(f'Tipo_huevos: BC, numero_huevos: {total_bc}, numero_bandejas: {calcular_bandejas(total_bc,30)}')

    