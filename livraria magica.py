class Livro: #classe que molda o formato dos livros
    def __init__(self, titulo, autor, genero):
        self.titulo = titulo
        self.autor = autor
        self.genero = genero

class Estante: #classe voltada para as funcionalidades da estante
    def __init__(self):
        self.livros = {}
        self.generos = set() #é usado para armazenar o gênero dos livros

    def adicionar_livro(self, livro, exibir_mensagem=True): #adiciona os livros e aciona o exibir_mensagem
        if not self.verificar_livro_duplicado(livro.titulo):
            self.livros[livro.titulo] = livro
            self.generos.add(livro.genero)
            if exibir_mensagem:
                print(f"O livro '{livro.titulo}' foi adicionado à estante.")
        else:
            if exibir_mensagem:
                print(f"Livro '{livro.titulo}' já está na estante. Não é possível adicionar duplicatas.")

    def verificar_livro_duplicado(self, titulo):
        return titulo in self.livros

    def remover_livro(self, titulo):
        if titulo in self.livros:
            del self.livros[titulo] #deleta o livro pelo titulo
            print(f"O livro '{titulo}' foi removido da estante.")
        else:
            print(f"Livro '{titulo}' não encontrado na estante.")

    def mostrar_livros(self):
        if not self.livros:
            print("\nNenhum livro disponível na estante.")
        else:
            print("\nLivros disponíveis na estante:\n")
            for livro in self.livros.values():
                print(f"Título: {livro.titulo}\nAutor: {livro.autor}\nGênero: {livro.genero}\n")

    def buscar_por_genero(self, genero):
        livros_genero = [livro for livro in self.livros.values() if livro.genero.lower() == genero.lower()]
        if livros_genero:
            print(f"\nLivros no gênero '{genero}':\n")
            for livro in livros_genero:
                print(f"- '{livro.titulo}' de {livro.autor}")
        else:
            print(f"\nNenhum livro encontrado no gênero '{genero}'.")

class Livraria: #classe voltada para as funcionalidades da livraria
    def __init__(self):
        self.estante = Estante() #traz as funcionalidades da estante para dentro da livraria
        self.inicializar_livros() #inicializa alguns livros pré definidos

    def inicializar_livros(self):
        livros_pre_definidos = [
            Livro("A Divina Comédia", "Dante Alighieri", "Poesia"),
            Livro("Alice no País das Maravilhas", "Lewis Carroll", "Fantasia"),
            Livro("1984", "George Orwell", "Ficção Distópica"),
            Livro("Orgulho e Preconceito", "Jane Austen", "Romance"),
            Livro("O Senhor dos Anéis", "J.R.R. Tolkien", "Fantasia")
        ]
        for livro in livros_pre_definidos:
            self.estante.adicionar_livro(livro, exibir_mensagem=False) #percorre os livros da lista pré definida e adiciona os livros na estante

    def menu_interativo(self):
        while True:
            print(f"Olá, seja bem-vindo à Jornada dos Magic Books!")
            print('''\nEscolha uma opção:
            1 - Adicionar um livro
            2 - Remover um livro
            3 - Mostrar todos os livros
            4 - Buscar livros por gênero
            5 - Sair''')
            
            escolha = input("Digite o número da sua escolha: ")

            if escolha == "1":
                titulo = input("Título: ")
                autor = input("Autor: ")
                genero = input("Gênero: ")
                novo_livro = Livro(titulo, autor, genero)
                self.estante.adicionar_livro(novo_livro)
            elif escolha == "2":
                titulo = input("Título do livro a remover: ")
                self.estante.remover_livro(titulo)
            elif escolha == "3":
                self.estante.mostrar_livros()
            elif escolha == "4":
                genero = input("Digite o gênero que deseja buscar: ")
                self.estante.buscar_por_genero(genero)
            elif escolha == "5":
                print("Encerrando o sistema.")
                break
            else:
                print("Opção inválida. Tente novamente.")

#inicializando a livraria e exibindo o menu
livraria = Livraria()
livraria.menu_interativo()