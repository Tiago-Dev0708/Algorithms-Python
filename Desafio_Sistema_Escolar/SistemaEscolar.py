from time import sleep

# Criando o menu interativo
def Lercabecalho(txt):
  print('='*40)
  print(txt.center(40))
  print('='*40)

def Lermenu(lista):
  Lercabecalho('MENU PRINCIPAL')
  print('\033[35mComo posso te ajudar?\033[m')
  c = 1
  for item in lista:
    print(f'\033[33m{c}\033[m - \033[34m{item}\033[m')
    c += 1
  print('='*40)
  opc = LerInt()
  return opc

def Ler_Encerramento(lista):
  print('\033[31mTem certeza que deseja encerrar o sistema?\033[m')
  c = 1
  for item in lista:
    print(f'\033[33m{c}\033[m - \033[34m{item}\033[m')
    c += 1
  opc = LerInt()
  return opc

def LerInt():
  while True:
    try:
      print('\033[32mQual é a sua opção?\033[m')
      numero = int(input())
    except(ValueError, TypeError):
      print('\033[31mERRO: Por favor, digite uma opção válida!\033[m')
      continue
    else:
      return numero
    
def Ler_Matricula():
  while True:
    try:
      print('\033[32mDigite a matricula do aluno\033[m')
      numero = int(input())
    except(ValueError, TypeError):
      print('\033[31mERRO: Por favor, digite um inteiro como matricula!\033[m')
      continue
    else:
      return numero

def Ler_Nota():
  while True:
    try:
      print('\033[32mDigite as notas do aluno\033[m')
      numero = float(input())
    except(ValueError, TypeError):
      print('\033[31mERRO: Por favor, digite uma opção válida!\033[m')
      continue
    else:
      return numero

def Tratar_str(txt):
  while True:
    print(txt)
    palavra  = str(input())
    for i in palavra:
        if i == "0" or i == "1" or i == "2" or i == "3" or i == "4" or i == "5" or i == "6" or i == "7" or i == "8" or i == "9":
           print('\033[31mERRO: Por favor, digite um nome válido!\033[m')
           continue
        else:
           return palavra

# Finalizando o menu interativo
alunos = []      
# Criando a função matricular
def matricular():
  nome = Tratar_str('\033[32mDigite seu nome\033[m')
  matricula = Ler_Matricula()
  curso = Tratar_str('\033[32mDigite seu curso\033[m')
  notas = []
  i = 0
  while i != 3:
    nota = Ler_Nota()
    if nota > 10:
      print('\033[31mERRO: Por favor, digite uma nota válida!\033[m')
      continue
    else:
      notas.append(nota)
      i += 1

  aluno = {"Nome": nome,
           "Matricula": matricula,
           "Curso": curso,
           "Notas": notas}
  
  alunos.append(aluno)

  print("O aluno foi cadastrado")
  print(f"aluno cadastrado{aluno}")

  with open('alunos.txt', 'a') as arquivo:
    for chave, valor in aluno.items():
      if valor == notas:
        for a in notas:
          arquivo.write(str(f"{a}\n"))
      else:
        arquivo.write(f"{valor}\n")
    arquivo.write("\n")





def listar():
  with open('alunos.txt', 'r') as arquivo:
    for linha in arquivo:
      print(linha.strip())

def media(notas):
  
  media = sum(notas)/len(notas)
  
  return media 
  
  
def aprovacao(estudante): 
  
  m = media(estudante["Notas"])
  if m >= 6: 
    print("%s - Aluno aprovado"%estudante["Nome"]) 
  else: 
    print("%s - Aluno reprovado"%estudante["Nome"]) 


def calcular_aprovacao():
  for i in alunos:
    aprovacao(i)
    

def encerrar_sys():
  while True:
    enc = Ler_Encerramento(['Sim', 'Não'])
    if enc == 1:
        exit()
    elif enc == 2: 
      return res
  

while True:
  res = Lermenu(['Matricular', 'Listar', 'Saber Resultado', 'Encerrar Sistema'])
  if res == 1:
    matricular()
  elif res == 2:
    listar()
  elif res == 3:
    calcular_aprovacao() 
  elif res == 4:
    encerrar_sys()
  else:
    print('\033[31mERRO: Por favor, digite uma opção válida!\033[m')
  sleep(1)
