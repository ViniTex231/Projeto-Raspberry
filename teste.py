import datetime

edv = [1234, 2345, 3564]
edvadmin = [9999, 8888, 7777]
pontos_registrados = []
hora = 13



def tempo():
    if edvuser in pontos_registrados:
        horaponto = 17
        diferenca = horaponto - hora
        return diferenca, horaponto
    else:
        horaponto = 13
        diferenca = hora - horaponto
        return diferenca, horaponto



print("-=" * 30)
print("Bem vindo ao Ponto Bosch!")
print("1 - Registro de ponto")
print("2 - Verificar pontos")
print("-=" * 30)
menu = input("Digite sua opção: ")
while True:
    if menu == "1":
            edvuser = int(input("Digite seu EDV: "))
            if edvuser in edv:
                print("EDV correto")
                diferenca = tempo()
                diftempo = diferenca
                if diftempo >1:
                    print("Ponto validado, porém você esta atrasado.")
                    pontos_registrados.append(edvuser)
                else:
                    print("Ponto validado com sucesso!")
                    pontos_registrados.append(edvuser)
            else:
                print("EDV incorreto")
    if menu == "2":
        edvuser = int(input("Digite seu EDV administrativo: "))
        if edvuser in edvadmin:
            print(f"Os EDV's registrados no dia de hoje foram: ", pontos_registrados)
            break
        else:
            print("EDV incorreto")

tempo()




import datetime
import time

edv = [1234, 2345, 3564]
edvadmin = [9999, 8888, 7777]
pontos_registrados = []
pontos_atrasados = []
horano = datetime.datetime.now()
hora = horano.strftime("%H:%M")
print(hora)


def tempo():
    if edvuser in pontos_registrados:
        horaponto = time.strptime("17:05", "%H:%M")
        if horaponto < time.strptime(hora, "%H:%M"):
            diferenca = 1
        else:
            diferenca = 0

    else:
        horaponto = time.strptime("13:05", "%H:%M")
        if time.strptime(hora, "%H:%M") < horaponto:
            diferenca = 1
        else:
            diferenca = 0
    return diferenca


print("-=" * 30)
print("Bem vindo ao Ponto Bosch!")
print("1 - Registro de ponto")
print("2 - Verificar pontos")
print("-=" * 30)
menu = input("Digite sua opção: ")
while True:
    if menu == "1":
            edvuser = int(input("Digite seu EDV: "))
            if edvuser in edv:
                print("EDV correto")
                diferenca = tempo()
                diftempo = diferenca
                if diftempo == 1:
                    print("Ponto validado, porém você esta atrasado.")
                    pontos_atrasados.append(edvuser)
                else:
                    print("Ponto validado com sucesso!")
                    pontos_registrados.append(edvuser)
            else:
                print("EDV incorreto")
    if menu == "2":
        edvuser = int(input("Digite seu EDV administrativo: "))
        if edvuser in edvadmin:
            print(f"Os EDV's registrados corretamente no dia de hoje foram: ", pontos_registrados)
            print(f"Os EDV's registrados atrasados no dia de hoje foram: ", pontos_atrasados)
            break
        else:
            print("EDV incorreto")

tempo()
