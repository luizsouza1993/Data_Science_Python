class crud():
    def __init__(self):
        import os
        self.os = os
        print('Cadastro')

    #Função para ler os dados cadastrados
    def ler(self):
        if not self.os.path.exists('base_dados.txt'):
            escrita = open('base_dados.txt', 'w')
            escrita.write('')
            escrita.close()
        leitura = open('base_dados.txt', 'r')
        retorno = ''
        for linha in leitura:
            retorno += linha.strip() + '\n'
        leitura.close()
        if len(retorno)>0:
            return retorno
        else:
            return 'nenhum registro encontrado'

    #Função para gerar os Id
    def codigo_id(self):
        self.ler()
        leitura = open('base_dados.txt', 'r')
        ultima_linha = ''
        for linha in leitura:
            ultima_linha = linha.strip()
        if len(ultima_linha)<=0:
            ultima_linha = 'ID: 0000000'
        id = int(ultima_linha[ultima_linha.find('ID: ')+4:11])+1
        id = str(id).rjust(7,'0')
        leitura.close()
        return id

    #Método para a inserção de dados
    def cadastrar(self, nome = '', idade=''):
        id = self.codigo_id()
        nome = str(nome).ljust(29, ' ')
        idade = str(idade).rjust(3, '0')

        texto = self.ler()
        if texto == 'nenhum registro encontrado':
            texto = ''
        escrita = open('base_dados.txt', 'w')
        linha = f'ID: {id} - Nome: {nome} - Idade: {idade} anos'
        escrita.write(texto + linha)
        escrita.close()

    #Método para alteração de dados
    def alterar(self, id = -1, nome = '', idade = ''):
        if len(id)< 7:
            id = str(id).rjust(7, '0')
        nome = str(nome).ljust(25, ' ')
        idade = str(idade).rjust(3, '0')

        texto = self.ler()
        linhas = texto.split('\n')
        escrita = open('base_dados.txt', 'r')
        texto = ''
        for linha in linhas:
            if linha.find('ID: {id}')>=0:
                if len(nome.strip())<=0:
                    nome = linha[linha.find('NOME: ')+6:linha.find(' - IDADE')]
                if '000' in idade:
                    idade = linha[linha.find('IDADE: ')+7:linha.find(' anos')]
                texto += (f'ID: {id} - Nome: {nome} - Idade: {idade} anos\n')
            else:
                texto += linha +'\n'
        escrita.write(texto.strip())
        escrita.close()

    #Método para exclusão de registros
    def deletar(self, id= -1):
        if len(str(id))< 7:
            id = str(id).rjust(7, '0')
        texto =  self.ler()
        linhas = texto.split('\n')
        escrita = escrita = open('base_dados.txt', 'w')
        texto = ''
        for linha in linhas:
            if linha.find(f'ID: {id}')>=0:
                texto += ''
            else:

                texto += linha + '\n'
        escrita.write(texto.strip())
        escrita.close()
    #Função para consultar os registros
    def consultar(self, id=-1):
        if len(id)<7:
            id = str(id).rjust(7,'0')
        if not self.os.path.exists('base_dados.txt'):
            escrita = open('base_dados.txt', 'w')
            escrita.write('')
        leitura = open('base_dados.txt', 'r')
        retorno = ''
        for linha in leitura:
            if linha.find(f'ID: {id}')>=0:
                retorno = linha.strip()+ '\n'
        leitura.close()
        return retorno

    #Metodo principal para executar o CRUD
    def executar(self):
        opcao = 1
        while opcao >0:
            print('\n(1) - LÊ \n(2) - CADASTRA \n(3) - ALTERA \n(4) - DELETA \n(5) - CONSULTA \n(0) - SAIR')
            opcao = int(input('Informe a sua opção: '))
            if opcao == 1:
                print('Dados\n'+ self.ler())
            elif opcao == 2:
                nome = str(input('Nome: '))
                idade = int(input('Idade: '))
                self.cadastrar(nome,idade)
                print('Registro cadastrado com sucesso')
            elif opcao == 3:
                id = int(input('ID: '))
                nome = str(input('Nome: '))
                idade = int(input('Idade: '))
                self.alterar(id,nome,idade)
                print('Dados Alterados com sucesso')
            elif opcao == 4:
                id = int(input('ID: '))
                self.deletar(id)
                print('Registro excluido com sucesso')
            elif opcao == 5:
                id = int(input('ID: '))
                linhas = self.consultar(id)
                print('Dados \n'+ linhas)
            else:
                print('Encerrado')

                            

















        
        

    
