n_dias = int(input("O livro devolvido tem quantos dias em atraso: "))


if n_dias <= 3:
    multa = 0.50 * n_dias

if 4 <= n_dias <= 7:
    multa = 1.00 * n_dias

if n_dias > 7:
    multa = 2.00 * n_dias

print("O valor da sua multa é ", multa, "€")
