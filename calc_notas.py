lista_alunos = []
lista_notas = []

def menu():
    print("="*30)
    print("Menu de Notas e médias")
    print("="*30)
    print("Bem vindo ao menu de notas!! \n Escolha uma das opções:")
    print("1- Cadastro do aluno")
    print("2- Cadastro da nota")
    print("3- Situação do aluno")
    print("4- Média faltante")
    print("5-sair")
    print("="*30)


def cadastro_nome():
    nome_aluno = input("qual o nome do aluno? ").title().strip()
    if not nome_aluno:
        print("O nome do aluno não pode estar vazio...")
        return
    if nome_aluno in lista_alunos:
        print("nome do aluno já está cadastrado,tente denovo...")
        return
    if not nome_aluno.replace(" ", "").isalpha():
        print("o nome deve conter apenas letras..")
        return

    

    lista_alunos.append(nome_aluno)
    lista_notas.append([])
    print(f"Parabéns {nome_aluno} !! você foi cadastrado com sucesso !")
    

def cadastro_notas():
    if not lista_alunos:
        print("Ainda não existe o cadastro de algum aluno, volte ao menu e tente novamente porfavor...")
        return
    
    print("Alunos cadastrados")
    for i in range(len(lista_alunos)):
        print(f"\n {i+1} = {lista_alunos[i]}")
    try:
        escolha = int(input("Escolha o número do aluno para cadastrar a nota: ")) -1
    
        if escolha >= 0 and escolha < len(lista_alunos):
            add_nota = float(input(f"Digite a nota de {lista_alunos[escolha]}: "))

        else:
            print("Erro tente novamente...")
            return
        
    except ValueError:
        print("opção inválida, digite apenas números")
        return

    if add_nota < 0 or add_nota >10:
                print("A nota só pode ser de 0 a 10...")
                return
    lista_notas[escolha].append(add_nota)
    print(f" Nota {add_nota} cadastrada para {lista_alunos[escolha]}!")

def situacao_aluno():
    if not lista_alunos:
        print("Ainda não existe o cadastro de algum aluno, volte ao menu e tente novamente porfavor...")
        return
    print("Alunos cadastrados:")
    for i in range(len(lista_alunos)):
        print(f"{i+1} - {lista_alunos[i]}")
    try:
        escolha = int(input("Escolha o número do aluno para ver a situação da nota: ")) - 1
        
   
        if escolha < 0 or escolha >= len(lista_alunos):
            print("Número de aluno inválido!")
            return

        if not lista_notas[escolha]:
            print("O aluno ainda não tem uma nota cadastrada.")
            return

        media = sum(lista_notas[escolha]) / len(lista_notas[escolha])
        print(f"A situação do(a) {lista_alunos[escolha]} é:")
        print(f"Notas: {lista_notas[escolha]} \nMédia: {media:.2f}")

        if media >= 6:
            print("Situação: Aprovado! Parabéns!")
        else:
            print("A média está abaixo de 6! Situação: Reprovado!")

    except ValueError:
        print("Opção inválida, digite apenas números.")
        return
    
    

def media_faltante():
    media_min = 6
    if not lista_alunos:
        print("Ainda não existe nenhum aluno cadastrado.")
        return

    print("Alunos cadastrados:")
    for i in range(len(lista_alunos)):
        print(f"{i+1} - {lista_alunos[i]}")
    try:
        escolha = int(input("Escolha o número do aluno para calcular a média faltante: ")) - 1
        
        if escolha >= 0 and escolha < len(lista_alunos):
            media_atual = sum(lista_notas[escolha]) / len(lista_notas[escolha])
            faltante = media_min * (len(lista_notas[escolha]) + 1) - sum(lista_notas[escolha])

            print(f"\nAluno: {lista_alunos[escolha]}")
            print(f"Notas atuais: {lista_notas[escolha]}")
            print(f"Média atual: {media_atual:.2f}")
            if not lista_notas[escolha]:
                        print(f"O aluno {lista_alunos[escolha]} ainda não tem notas cadastradas.")
                        return
            if media_atual >= 6:
                print("✅ O aluno já atingiu a média mínima!")
            elif faltante > 10:
                print("⚠️ Não é possível atingir a média mínima com a próxima nota.")
            else:
              print(f"Para atingir média {media_min}, o aluno precisa tirar {faltante:.2f} na próxima nota.")
        else:
            print("Erro tente novamente...")
    except ValueError:
        print("opção inválida, digite apenas números.")

    
    
    

def main():
    while True:
        menu()
        opcao = input("\nQue função que usar? ").lower().strip()
        match opcao:
            case "1":
                cadastro_nome()
            case "2":
                cadastro_notas()
            case "3":
                situacao_aluno()
            case "4":
                media_faltante()
            case "5" | "sair":
                print("saindo do sistema...")
                break
            case _: 
                print("Opção inválida")

if __name__ == "__main__":
    main()
