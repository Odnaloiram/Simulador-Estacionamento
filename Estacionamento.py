lista_vagas: list[bool] = [False] * 30

while True:
    for i in range(30):
        if not lista_vagas[i]:
            print("Vaga", i + 1, "livre")
        else:
            print("Vaga", i + 1, "ocupada")

    indice_vaga = int(input("Escolha qual vaga você quer estacionar: "))
    indice_vaga = indice_vaga - 1

    if indice_vaga > 29 or indice_vaga < 0:
        print("Existe apenas 30 vagas, insira o número correspondente")
        continue

    if not lista_vagas[indice_vaga]:
        lista_vagas[indice_vaga] = True
        print("Vaga escolhida: ", indice_vaga + 1)
    else:
        print("Vaga", indice_vaga + 1, "ocupada")

    reiniciar = str(input("Deseja continuar? [S/N] ")).upper()
    if reiniciar == "N":
        break