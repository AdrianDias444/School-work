from datetime import datetime

def ordenar_artigos_por_data(artigos):
    """
    Ordena a lista de artigos por data de publicação, do mais antigo ao mais recente.
    
    Args:
        artigos: Lista de dicionários com informações sobre artigos
        
    Returns:
        Lista de artigos ordenada por data de publicação
    """
    # Ordena os artigos pela data de publicação
    # Converte a string de data para objeto datetime para ordenação correta
    artigos_ordenados = sorted(artigos, 
                              key=lambda artigo: datetime.strptime(artigo['data_publicacao'], '%d/%m/%Y'))
    
    return artigos_ordenados

def exibir_artigos(artigos):
    """
    Exibe os artigos de forma formatada.
    
    Args:
        artigos: Lista de dicionários com informações sobre artigos
    """
    for i, artigo in enumerate(artigos, 1):
        print(f"\n{i}. {artigo['titulo']}")
        print(f"   Autores: {', '.join(artigo['autores'])}")
        print(f"   Data de publicação: {artigo['data_publicacao']}")
        print(f"   Consultas: {artigo['consultas']}")

# Lista de artigos fornecida no desafio
artigos = [
    {
        'titulo': 'Applications of Artificial Intelligence in Academic Libraries',
        'autores': ['Vijayakumar, S.', 'Sheshadri, K.N.'],
        'data_publicacao': '16/05/2019',
        'consultas': 569
    },
    {
        'titulo': 'Data science in data librarianship: Core competencies of a data librarian',
        'autores': ['Semeler, A. R.', 'Pinto, A. L.', 'Rozados, H. B. F.'],
        'data_publicacao': '26/11/2019',
        'consultas': 1004
    },
    {
        'titulo': 'Data scientist: the sexiest job of the 21st century',
        'autores': ['Davenport, T.H.', 'Patil, D.J.'],
        'data_publicacao': '01/10/2012',
        'consultas': 10231
    },
    {
        'titulo': 'Bibliometria: evolução histórica e questões atuais',
        'autores': ['Araújo, C.A.A.'],
        'data_publicacao': '10/12/2006',
        'consultas': 650
    }
]

# Execução principal
print("=== Lista de Artigos Original ===")
exibir_artigos(artigos)

# Ordenar artigos por data de publicação
artigos_ordenados = ordenar_artigos_por_data(artigos)

print("\n" + "="*50)
print("=== Artigos Ordenados por Data (Mais Antigo ao Mais Recente) ===")
exibir_artigos(artigos_ordenados)

# Versão alternativa usando o método sort() (modifica a lista original)
def ordenar_artigos_por_data_sort(artigos):
    """
    Ordena a lista de artigos por data de publicação usando sort().
    Modifica a lista original.
    """
    artigos.sort(key=lambda artigo: datetime.strptime(artigo['data_publicacao'], '%d/%m/%Y'))

# Testando a versão com sort()
print("\n" + "="*50)
print("=== Usando sort() ===")

# Criar uma cópia da lista original
artigos_copia = artigos.copy()
ordenar_artigos_por_data_sort(artigos_copia)
exibir_artigos(artigos_copia)
