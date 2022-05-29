# roboParafusador
EP1 - Alg &amp; Prog - Python


Exercício programa - 1
Algorítimos e Programação.

Descrição da atividade:

Algoritmos e Programação I
Exercício Programa 1 - Robô Parafusador
4 de maio de 2022
1 Descrição do problema
Um robô parafusador foi colocado em atividade em uma montadora de veículos para auxílio na produção e montagem de carros. O robô recebe tarefas
simples de um operador, como “parafusar capô” ou “parafusar rodas”. Após
receber uma instrução do operador, o robô a executa e, finalizada a tarefa, ou
conjunto de tarefas, espera a próxima instrução do operador.
O operador pode solicitar ao robô, através de uma única instrução, um
conjunto de até 8 tarefas simultâneas, já que o robô tem 8 braços parafusadores
e, por isso, pode realizar até 8 tarefas ao mesmo tempo, identificadas por um
código de 1 a 8.
Uma instrução descrita pelo operador é, na verdade, um conjunto de tarefas
que o robô deve realizar ao mesmo tempo. A instrução é codificada pelo operador como um número inteiro no intervalo [0, 255] e fornecida ao robô. Como o
robô compreende apenas números na base 2, ele transforma a instrução do operador em uma instrução na base 2, que representa um conjunto de tarefas que
ele deve executar. A figura abaixo mostra a instrução 145, em que o robô tem
de realizar 3 tarefas ao mesmo tempo: parafusar o assoalho (tarefa 8), parafusar
o motor (tarefa 5) e parafusar o capô (tarefa 1).
_________________
|1 0 0 1 0 0 0 1|
8) assoalho
7) chassi
6) portas
5) motor
1) capô
2) tampa do porta-malas
3) eixos
4) rodas
instrução
O robô passa várias horas do dia realizando suas tarefas. Ao final de um
dia de trabalho, o supervisor desativa o robô, digitando a instrução 0 (zero), e
recebe um relatório com algumas estatísticas:
1
2 IMPLEMENTAÇÃO
• a quantidade total de cada tarefa realizada pelo robô;
• a tarefa mais realizada pelo robô;
• a tarefa menos realizada;
• a instrução que exigiu menos tarefas simultâneas do robô, juntamente com
a quantidade exigida; e
• a instrução que exigiu mais tarefas simultâneas do robô, juntamente com
a quantidade correspondente.
2 Implementação
Neste EP, você deve implementar um programa na linguagem Python 3 que
recebe uma sequência não vazia de números inteiros (um número por linha) finalizada por 0 (zero), representando as instruções que o operador fornecerá ao
robô. O seu programa deve imprimir na tela o relatório de estatísticas contendo
12 linhas. Nas primeiras oito linhas devem ser apresentadas as quantidades
de cada tarefa executada. Nas duas linhas seguintes devem ser apresentadas a
tarefa mais realizada e a tarefa menos realizada, respectivamente. No caso de
empate, deve ser considerada a tarefa com o menor código. Nas duas últimas
linhas devem ser apresentadas as instruções que exigiram menos e mais tarefas
simultâneas, respectivamente. No caso de empate, deve ser considerada a instrução mais recente, ou seja, a última digitada pelo operador. Veja os exemplos
abaixo.
Exemplo 1:
Entrada:
24
41
0
Saída:
1. parafusar capo: 1.
2. parafusar tampa do porta-malas: 0.
3. parafusar eixos: 0.
4. parafusar rodas: 2.
5. parafusar motor: 1.
6. parafusar portas: 1.
7. parafusar chassi: 0.
8. parafusar assoalho: 0.
A tarefa mais realizada foi parafusar rodas: 2 vezes.
A tarefa menos realizada foi parafusar tampa do porta-malas: 0 vezes.
A instrucao que exigiu menos tarefas simultaneas do robo foi a 24: 2 tarefas.
A instrucao que exigiu mais tarefas simultaneas do robo foi a 41: 3 tarefas.
2
3 INSTRUÇÕES
Exemplo 2:
Entrada:
15
129
24
51
128
85
0
Saída:
1. parafusar capo: 4.
2. parafusar tampa do porta-malas: 2.
3. parafusar eixos: 2.
4. parafusar rodas: 2.
5. parafusar motor: 3.
6. parafusar portas: 1.
7. parafusar chassi: 1.
8. parafusar assoalho: 2.
A tarefa mais realizada foi parafusar capo: 4 vezes.
A tarefa menos realizada foi parafusar portas: 1 vezes.
A instrucao que exigiu menos tarefas simultaneas do robo foi a 128: 1 tarefas.
A instrucao que exigiu mais tarefas simultaneas do robo foi a 85: 4 tarefas.
3 Instruções
1. Você deverá entregar apenas o seu arquivo .py através do AVA até a
data/horário limite que consta no próprio AVA. Não deixe para o último
minuto, não serão aceitos códigos com atraso;
2. No desenvolvimento do código deverá ser utilizado o conceito de funções,
caso contrário o programa será desconsiderado;
3. Não devem ser utilizadas bibliotecas externas ou mesmo métodos da classe
list que não foram apresentados nos slides das aulas. Na dúvida, pergunte
através do fórum do AVA;
4. Crie os seus casos de teste para testar o seu programa com várias entradas
possíveis;
5. O EP é individual. Plágio/cola acarreta em nota zero para os envolvidos na média dos exercícios-programa (ME) no cálculo da
média de aproveitamento. Lembrem-se: a ética é inegociável.
