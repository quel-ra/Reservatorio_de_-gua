Total_Reservatorio=1000

Reservatorio_de_agua =float(input("Digite o volume de água do reservatório em litros: "))

Nivel_de_Reservatorio= ["Nivel 1", "Nivel 2", "Nivel 3", "Nivel 4", "Nivel 5"]

from colorama import Fore, Style

if Reservatorio_de_agua < 0.20*Total_Reservatorio and Reservatorio_de_agua >= 0.00*Total_Reservatorio:
        print(Fore.RED + str("Nivel 1:") + " Nivel de reservatório muito Abaixo (Crítico)")
elif Reservatorio_de_agua<0.40*Total_Reservatorio and Reservatorio_de_agua >= 0.20*Total_Reservatorio:
        print(Fore.YELLOW + str("Nivel 2:") + " Nivel de reservatório Baixo")
elif Reservatorio_de_agua < 0.60*Total_Reservatorio and Reservatorio_de_agua >= 0.40*Total_Reservatorio:
        print(Fore.GREEN + str("Nivel 3:") + " Nivel de reservatório Médio")
elif Reservatorio_de_agua < 0.80*Total_Reservatorio and Reservatorio_de_agua >= 0.60*Total_Reservatorio:
        print(Fore.CYAN + str("Nivel 4:") + " Nivel de reservatório Alto")
elif Reservatorio_de_agua <= 1.00*Total_Reservatorio and Reservatorio_de_agua >= 0.80*Total_Reservatorio:
        print(Fore.BLUE + str("Nivel 5:") + " Nivel de reservatório muito Alto (ALERTA!)")

print(Style.RESET_ALL)
