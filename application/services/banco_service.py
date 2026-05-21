from domain.repositories.banco_repositorio_interface import IBancoRepository

class BancoService:

    def __init__(self, repo:IBancoRepository):
        self.repo = repo

    # 🔹 Listar
    def listar(self):
        return self.repo.listar()
