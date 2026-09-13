class Curso:
    area = "Informática"

    def __init__(self, nome, duracao, vagas):
        self.nome = nome
        self.duracao = duracao
        self.vagas = vagas

    def resumo(self):
        return (
            f"{self.nome} ({self.duracao} h), "
            f"vagas: {self.vagas}"
        )

    def alterar_nome(self, novo_nome):
        self.nome = novo_nome

    def inscrever(self):
        if self.vagas > 0:
            self.vagas -= 1
            return True

        return False


class CursoOnline(Curso):
    def __init__(
        self, nome, duracao, vagas, plataforma
    ):
        super().__init__(nome, duracao, vagas)
        self.plataforma = plataforma

    def resumo(self):
        base = super().resumo()
        return (
            f"{base}. Plataforma: {self.plataforma}"
        )
