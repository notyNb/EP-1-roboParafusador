#=============================================================
def binario(um: int, n: int, lista_binario: list, lista_comparativa: list, n_bkp: int, lista_comparativaNomes: list, tarefas: list, lista_comparativa2: list, n_bkp2: int, lista_comparativaNomes2: list):
    n_bkp = n
    n_bkp2 = n
    while n > 0:
        resto = n % 2
        n = n // 2
        lista_binario.append(resto)
    for i in range(len(lista_binario)):
        tarefas[i] += (lista_binario[i])
    simultaneaMenos(lista_binario, lista_comparativa, n_bkp, lista_comparativaNomes, um)
    simultaneaMais(lista_binario, lista_comparativa2, n_bkp2, lista_comparativaNomes2, um)
    lista_binario.clear()

#============================================================
def imprimir(tarefas: list):
    nomes = ["capo", "tampa do porta-malas", "eixos", "rodas", "motor", "portas", "chassi", "assoalho"]
    numeros1_8 = [1, 2, 3, 4, 5, 6, 7, 8]
    for i in range(len(tarefas)):
        print(f"{numeros1_8[i]}. parafusar {nomes[i]}: {tarefas[i]}.")
    tarefaMais(tarefas, nomes)
    tarefaMenos(tarefas, nomes)

#===========================================================
def tarefaMais(tarefas: list, nomes: list):
    maior = 0
    posicao = 0
    for i in range(len(tarefas)):
        if maior < tarefas[i]:
            maior = tarefas[i]
            posicao = i
    print(f"A tarefa mais realizada foi parafusar {nomes[posicao]}: {maior} vezes.")    

#===========================================================
def tarefaMenos(tarefas: list, nomes: list):
    menor = (tarefas[0] + 1)
    posicao = 0
    for i in range(len(tarefas)):
        if menor > tarefas[i]:
            menor = tarefas[i]
            posicao = i
    print(f"A tarefa menos realizada foi parafusar {nomes[posicao]}: {menor} vezes.")

#=========================================================
def simultaneaMenos(lista_binario, lista_comparativa: list, n_bkp, lista_comparativaNomes, um:int):
    soma = 0
    
    for i in range(len(lista_binario)):
        if lista_binario[i] != 0:
            soma += 1
    lista_comparativa.insert(0, soma)
    lista_comparativaNomes.insert(0, n_bkp)
    if lista_comparativa[0] == 0:
        del lista_comparativa[0]
    if lista_comparativaNomes[0] == 0:
        del lista_comparativaNomes[0]
    
    
    for i in range(1):
        if (len(lista_comparativa)) >= 2:
            if lista_comparativa[i] <= lista_comparativa[i+1]:
                menor = lista_comparativa[i]
                n_bkp = lista_comparativaNomes[i]
            elif lista_comparativa[i] > lista_comparativa[i+1]:
                menor = lista_comparativa[i+1]
                n_bkp = lista_comparativaNomes[i+1]
        else:
            menor = lista_comparativa[i]
            n_bkp = lista_comparativaNomes[i]
    
    if um == 0:
        imprimir2(n_bkp, menor)

#====================================================
def imprimir2(n_bkp: int, menor: int):
    print(f"A instrucao que exigiu menos tarefas simultaneas do robo foi a {n_bkp}: {menor} tarefas.")
    
#===================================================
def simultaneaMais(lista_binario, lista_comparativa2: list, n_bkp2, lista_comparativaNomes2: list, um:int):
    soma = 0
    
    for i in range(len(lista_binario)):
        if lista_binario[i] != 0:
            soma += 1
    lista_comparativa2.insert(0, soma)
    lista_comparativaNomes2.insert(0, n_bkp2)
    if lista_comparativa2[0] == 0:
        del lista_comparativa2[0]
    if lista_comparativaNomes2[0] == 0:
        del lista_comparativaNomes2[0]
         
    
    for i in range(1):
        if (len(lista_comparativa2)) >= 2:
            if lista_comparativa2[i] >= lista_comparativa2[i+1]:
                maior = lista_comparativa2[i]
                n_bkp2 = lista_comparativaNomes2[i]
            elif lista_comparativa2[i] < lista_comparativa2[i+1]:
                maior = lista_comparativa2[i+1]
                n_bkp2 = lista_comparativaNomes2[i+1]
        else:
            maior = lista_comparativa2[i]
            n_bkp2 = lista_comparativaNomes2[i]
        
    
    if um == 0:
        imprimir3(n_bkp2, maior)

#================================================
def imprimir3(n_bkp2: int, maior: int):
    print(f"A instrucao que exigiu mais tarefas simultaneas do robo foi a {n_bkp2}: {maior} tarefas.")

#=============================================
def main():
    um = 1 #variavel que vai identificar quando o valor digitado for 0
    lista_binario = []
    lista_comparativa = []
    lista_comparativa2 = []
    lista_comparativaNomes = []
    lista_comparativaNomes2 = []
    tarefas = [0] * 8
    menor = 0
    maior = 0
    n_bkp = 0
    n_bkp2 = 0
        
    while um != 0:
        n = int(input())
        if n != 0:
            um = um
            binario(um, n, lista_binario, lista_comparativa, n_bkp, lista_comparativaNomes, tarefas, lista_comparativa2, n_bkp2, lista_comparativaNomes2)
        else:
            um = um - 1
            imprimir(tarefas)
            simultaneaMenos(lista_binario, lista_comparativa, n_bkp, lista_comparativaNomes, um)
            simultaneaMais(lista_binario, lista_comparativa2, n_bkp2, lista_comparativaNomes2, um)
            
main()

#===============================================================================================================================================================================================
