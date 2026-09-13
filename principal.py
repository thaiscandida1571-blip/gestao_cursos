import modelos

cursos = [
    modelos.Curso("Python", 50, 2),
    modelos.Curso("Excel", 25, 0),
    modelos.CursoOnline("SQL", 25, 1, "Teams"),
    modelos.Curso("Power BI", 25, 1)
]

for curso in cursos:
    print(curso.resumo())

print("Inscrição em Power BI:", cursos[3].inscrever())
print("Inscrição em Power BI:", cursos[3].inscrever())
print("Inscrição em Python:", cursos[0].inscrever())
print("Inscrição em Excel:", cursos[1].inscrever())
print("Inscrição em SQL:", cursos[2].inscrever())

print("Cursos com vagas:")
for curso in cursos:
    if curso.vagas > 0:
        print(curso.nome, curso.vagas)
# --- Cálculo da Duração Total ---
duracao_total = sum(curso.duracao for curso in cursos)
print(f"\nDuração total de todos os cursos: {duracao_total} horas")
