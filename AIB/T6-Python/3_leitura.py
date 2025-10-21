from decimal import Decimal

total = int(input("Total de páginas do livro: "))

while True:
    lidas = int(input("Páginas lidas: "))

    if lidas > total:
        print("Erro: páginas lidas não podem ser maior que o total!\n")
        continue

    percent = (Decimal(lidas) / Decimal(total)) * 100
    print(f"Você leu {percent}% do livro")

    if lidas == total:
        print("Parabéns! Terminou o livro!")

    break
