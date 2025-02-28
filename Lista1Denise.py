#Etapa 1 - Bake & Deploy: Produzindo o Bolo em Buga


#1-
print('Programa 1')
print('Minha vida vai melhorar agora que estou aprendendo a programar... pelo menos o computador vai entender meus problemas!\n')


#2
print('Programa 2')
print('Programar um sistema de confeitaria é igual fazer um bolo: se errar a sintaxe, o código embatuma!')


#Programa 3 - Bolo de Leite Condensado
#VARIÁVEIS ABAIXO
xicaras = int(input("Informe a quantidade de xícaras\n"))
gramasxicara = float(input("Informe as gramas da xícara\n"))
leite = int(input("Informe a quanidade de caixas de leite\n"))
gramasleite = float(input("Informe as gramas da caixa de leite\n"))
ovos = int(input("Informe a quandidade de ovos\n"))


#VARIÁVEIS ML LEITE


mililitrosLeite = 0.0
mililitrosOvos = 0.0
mililitrosTrigo = 0.0
gramasovos = 0.0
gramasXicaraTotal = 0.0
gramasLeiteTotal = 0.0
MlTotalReceita = 0.0
VolumeFormaReta = float


#  INICIO PROGRAMA


print (f'A quantidade de xícaras é {xicaras}\nSua quantidade de gramas é {gramasxicara}\nSua quantidade de caixas e leite é {leite}\nA grama da caixa de leite é de {gramasleite}\nPossui {ovos} ovos na receita')
print("\n===================================================\n")
#gramas para ml do leite, ovos e trigo
def conversaoGramas_MLLeite():
    gramasLeiiteTotal = gramasleite * leite
    mililitrosLeite = gramasLeiiteTotal / 1.3
    return mililitrosLeite


def conversaoGramas_MLOvos():
    gramasovos = ovos * 54
    mililitrosOvos = gramasovos / 1.0
    return mililitrosOvos


def conversaoGramas_MLxicara():
    gramasXicaraTotal = gramasxicara * xicaras
    mililitrosTrigo = gramasXicaraTotal/ 0.59
    return mililitrosTrigo


mililitrosLeite = conversaoGramas_MLLeite()
mililitrosOvos = conversaoGramas_MLOvos()
mililitrosTrigo = conversaoGramas_MLxicara()
MlTotalReceita = mililitrosLeite + mililitrosOvos + mililitrosTrigo


print(f"A quantidade de ML total da sua receira é de {MlTotalReceita:.2f}ML\n")


#Calculando o volume da forma


print("Digite o número que representa o formato de sua forma:\n")
print("1 = Retangular ou quadrada\n")
print("2 = Redonda\n")


formatoForma= int(input("Digite o número correspondente"))
if formatoForma == 1:
    ComprimentoFormaQuadrada = float(input("Informe o comprimento da sua forma\n"))
    LarguraFormaQuadrada =  float(input("Informe a largura da sua forma\n"))
    AlturaFormaQuadrada = float(input("Informe a altura da sua forma\n"))
    VolumeFormaReta = ComprimentoFormaQuadrada * LarguraFormaQuadrada * AlturaFormaQuadrada
    AreaFormaQuadrada = ComprimentoFormaQuadrada * AlturaFormaQuadrada
    if VolumeFormaReta >= MlTotalReceita:
        print(f"Seu volume de forma é de {VolumeFormaReta:.2f}, sua receita caberá na forma\n")
        print(f"Para untar a forma seu papel deve ter {AreaFormaQuadrada:.2f}cm³")


    else:
        print(f"Sua receita não caberá na forma, sua quantidade de ingredientes é maior que {VolumeFormaReta:.2f}ML")


elif formatoForma == 2:
    raioFormaRedonda= float(input("Informe o raio da forma\n"))
    alturaFormaRedonda = float(input("Informe a altura da forma\n"))
    VolumeFormaRedonda = 3.14 * (raioFormaRedonda ** 2) * alturaFormaRedonda
    AreaBaseRedonda = 3.14 * (raioFormaRedonda ** 2)
    AreaLateralRedonda = 2 * 3.14 * raioFormaRedonda * alturaFormaRedonda
    if VolumeFormaRedonda >= MlTotalReceita:
        print(f"Seu volume de forma é de {VolumeFormaRedonda:.2f}, sua receita caberá na forma\n")
        print(f"Para untar a forma seu papel da base deve ter {AreaBaseRedonda:.2f}cm³")
        print(f"Para untar a forma seu papel da lateral deve ter {AreaLateralRedonda:.2f}cm³")
    else:
        print(f"Sua receita não caberá na forma, sua quantidade de ingredientes é maior que {VolumeFormaRedonda:.2f}ML")

