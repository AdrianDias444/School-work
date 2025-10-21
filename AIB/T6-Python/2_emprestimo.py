dias_semana = ["segunda", "terça", "quarta", "quinta", "sexta", "sábado", "domingo"]
livros = []

for dia in dias_semana:
    emprestimos = int(input(f"Livros emprestados na {dia}: "))
    livros.append(emprestimos)

total = sum(livros)
media = total / 7
maior_emprestimos = max(livros)
dia_maior = dias_semana[livros.index(maior_emprestimos)]

print(f"\nTotal de livros emprestados: {total}")
print(f"Média diária: {media:.1f}")
print(f"Dia com mais empréstimos: {dia_maior} ({maior_emprestimos} livros)")
