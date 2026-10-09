dia_semana = int(input("digite um numero entre 1 e 7 para representar os dias da semana: "))

match dia_semana:
    case 1:
        print("Domingo")
    case 2:
        print("Segunda")
    case 3:
        print("Terça")
    case 4:
        print("Quarta")
    case 5:
        print("Quinta")
    case 6:
        print("Sexta")
    case 7:
        print("Sábado")
    case _:
        print("dia da semana invalido")




