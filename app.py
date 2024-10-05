import os

restaurantes = [
    {'nome': 'hotdog', 'categoria': 'cachorro quente', 'ativo': False},
    {'nome': 'fast hamburguer', 'categoria': 'hamburguer', 'ativo': True},
    {'nome':  'Pizza', 'categoria': 'pizza', 'ativo': False}
]

def exibir_nome_do_programa():
       print(""" 
 ░██████╗░░█████╗░██╗░░░██╗██████╗░███╗░░░███╗███████╗████████╗
██╔════╝░██╔══██╗██║░░░██║██╔══██╗████╗░████║██╔════╝╚══██╔══╝
██║░░██╗░██║░░██║██║░░░██║██████╔╝██╔████╔██║█████╗░░░░░██║░░░
██║░░╚██╗██║░░██║██║░░░██║██╔══██╗██║╚██╔╝██║██╔══╝░░░░░██║░░░
╚██████╔╝╚█████╔╝╚██████╔╝██║░░██║██║░╚═╝░██║███████╗░░░██║░░░
░╚═════╝░░╚════╝░░╚═════╝░╚═╝░░╚═╝╚═╝░░░░░╚═╝╚══════╝░░░╚═╝░░░

██████╗░███████╗██╗░░░░░██╗██╗░░░██╗███████╗██████╗░██╗░░░██╗
██╔══██╗██╔════╝██║░░░░░██║██║░░░██║██╔════╝██╔══██╗╚██╗░██╔╝
██║░░██║█████╗░░██║░░░░░██║╚██╗░██╔╝█████╗░░██████╔╝░╚████╔╝░
██║░░██║██╔══╝░░██║░░░░░██║░╚████╔╝░██╔══╝░░██╔══██╗░░╚██╔╝░░
██████╔╝███████╗███████╗██║░░╚██╔╝░░███████╗██║░░██║░░░██║░░░
╚═════╝░╚══════╝╚══════╝╚═╝░░░╚═╝░░░╚══════╝╚═╝░░╚═╝░░░╚═╝░░░
""")
       

def exibir_opcoes():
    print('1-Cadastrar restaurante')
    print('2-Listar restaurantes')
    print('3-Alternar status do restaurante')
    print('4-Sair')

def finalizando_app():
    exibir_subtitulo('Finalizando o app')

def voltar_ao_menu_principa():
    input('\nDigite uma tecla para voltar ao menu principal!')
    main()
  

def opcao_invalida():
    print('Opção inválida!\n')
    voltar_ao_menu_principa()

def exibir_subtitulo(texto):
    os.system('clear')
    linha = print('*' * len(texto))
    print(texto) 
    linha = print('*' * len(texto))

def cadastrar_novo_restaurante():
    '''Essa função é responsável por cadastrar um novo restaurante'''
    exibir_subtitulo('Cadastro de novos restaurantes')
    nome_do_restaurante = input('Digite o nome do restaurante que deseja cadastrar:')
    categoria = input(f'Digite a categoria do restaurante {nome_do_restaurante}: ')
    dados_do_restaurante = {'nome':nome_do_restaurante, 'categoria':categoria, 'ativo':False}
    restaurantes.append(dados_do_restaurante)
    print(f'O restaurante {nome_do_restaurante} foi cadastrado com sucesso!\n')
    voltar_ao_menu_principa()

def listar_restaurantes():
    exibir_subtitulo('Listando os restaurantes')

    print(f'{'Nome do restaurante'.ljust(22)} | {'Categoria'.ljust(22)} | Status do restaurante')

    for restaurante in restaurantes:
        nome_restaurante = restaurante['nome']
        categoria = restaurante['categoria']
        ativo = 'ativado' if restaurante['ativo'] else 'desativado'
        print(f'- {nome_restaurante.ljust(20)} | {categoria.ljust(20)} | {ativo}')

    voltar_ao_menu_principa()    



def alternar_status_restaurante():
    exibir_subtitulo('Alterando status do restaurante')
    nome_restaurante = input('Digite o nome do restaurante que deseja alterar o status: ')
    restaurante_encontrado = False

    for restaurante in restaurantes:
        if nome_restaurante == restaurante['nome']:
            restaurante_encontrado = True
            restaurante['ativo'] = not restaurante['ativo']
            mensagem = (f'O restaurante {nome_restaurante} foi ativado com sucesso' if restaurante['ativo'] else f'O restaurante {nome_restaurante} foi desativo com sucesso')
            print(mensagem)
  
    if not restaurante_encontrado:
        print('O restaurante não foi encontrado')


    voltar_ao_menu_principa()

def escolher_opcao():
    opcao_escolhida = int(input('Escolha uma opção: '))
    # opcao_escolhida = int(opcao_escolhida

    try:
        if opcao_escolhida == 1:
            # Cadastrar restaurante
            cadastrar_novo_restaurante()
        elif opcao_escolhida == 2:
            # Listar restaurantes
            listar_restaurantes()
        elif opcao_escolhida == 3:
            # Ativar restaurante')
            alternar_status_restaurante()
        elif opcao_escolhida == 4: 
            finalizando_app()   
        else:
            opcao_invalida()
    except:
        opcao_invalida()        


def main():
    os.system('clear')
    exibir_nome_do_programa()
    exibir_opcoes()
    escolher_opcao()


if __name__ == '__main__':
    main()
    
    
