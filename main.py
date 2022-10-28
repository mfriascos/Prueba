from clasificacion_huevos import clasificacion_huevos
import random


def run():
    list_eggs = []
    for i in range(500):
        egg = (random.randint(430,700))/10
        list_eggs.append(egg)
    
    print(list_eggs)
    print()
    
    clasificacion_huevos(list_eggs)

if __name__ == '__main__':
    run()