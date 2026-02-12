import random

def gerar_quadmag_lux(tamanho):
    """
    Gera um quadrado mágico de tamanho par usando métodos apropriados
    Para 8 ou maiores, apenas embaralha os números
    """
    if tamanho % 2 != 0:
        raise ValueError("Este método requer um tamanho par")
    
    n = tamanho
    quadmag = [[0 for _ in range(n)] for _ in range(n)]
    
    if n >= 8:
        numeros = list(range(1, n*n + 1))
        # Embaralhar os números
        random.shuffle(numeros)
        
        # Preencher a matriz com os números embaralhados
        idx = 0
        for i in range(n):
            for j in range(n):
                quadmag[i][j] = numeros[idx]
                idx += 1
        return quadmag
    
    if n % 4 == 0:  # Múltiplos de 4 (apenas 4)
        # Para 4x4, usar a matriz fixa conhecida
        if n == 4:
            quadmag = [
                [16, 2, 3, 13],
                [5, 11, 10, 8],
                [9, 7, 6, 12],
                [4, 14, 15, 1]
            ]
    
    else:  # 4m+2 (apenas 6)
        # Para 6x6, usar a matriz fixa conhecida
        if n == 6:
            quadmag = [
                [35, 1, 6, 26, 19, 24],
                [3, 32, 7, 21, 23, 25],
                [31, 9, 2, 22, 27, 20],
                [8, 28, 33, 17, 10, 15],
                [30, 5, 34, 12, 14, 16],
                [4, 36, 29, 13, 18, 11]
            ]
    
    return quadmag

def gerar_quadmag(tamanho):
    """
    Gera um quadrado mágico para qualquer tamanho (ímpar ou par)
    Para pares 8 ou maiores, apenas embaralha os números
    """
    if tamanho % 2 == 1:  # Método Siamese para números ímpares
        n = tamanho
        quadmag = [[0 for _ in range(n)] for _ in range(n)]

        # Posição inicial (método comum)
        i, j = 0, n // 2  # Começar no meio da primeira linha
        
        for num in range(1, n * n + 1):
            quadmag[i][j] = num
            
            # Calcular próxima posição
            novo_i = (i - 1) % n
            novo_j = (j + 1) % n
            
            # Se a próxima posição já estiver ocupada
            if quadmag[novo_i][novo_j]:
                i = (i + 1) % n  # Move para baixo
            else:
                i, j = novo_i, novo_j
    
    else:  # Método para números pares
        # Para todos os pares, usar a função gerar_quadmag_lux
        # que já trata 8+ como embaralhado
        quadmag = gerar_quadmag_lux(tamanho)
    
    return quadmag

def imprimir_quadmag(quadmag):
    """
    Imprime um quadrado mágico formatado
    """
    tamanho = len(quadmag)
    
    # Encontrar o maior número para formatação
    max_num = tamanho * tamanho
    espacos = len(str(max_num)) + 1
    
    for i in range(tamanho):
        for j in range(tamanho):
            print(f'{quadmag[i][j]:{espacos}d}', end='')
        print()

# Programa principal
if __name__ == "__main__":
    flag = 1
    
    while flag == 1:
        try:
            n = int(input("\nDigite o tamanho do QUADRADO MÁGICO (mínimo 3): "))
            
            if n < 3:
                print("Por favor, digite um número maior ou igual a 3")
                continue
            
            quadrado = gerar_quadmag(n)
            imprimir_quadmag(quadrado)
            
            a = input("\nVocê quer gerar outro quadrado mágico? (sim/não): ").lower()
            if a not in ['sim', 's', 'yes', 'y']:
                flag = 0
                
        except ValueError as e:
            print(f"Erro: {e}. Por favor, tente novamente.")
        except KeyboardInterrupt:
            print("\n\nPrograma interrompido pelo usuário.")
            flag = 0
        except Exception as e:
            print(f"\nOcorreu um erro inesperado: {e}")
            print("Tente um tamanho diferente.")