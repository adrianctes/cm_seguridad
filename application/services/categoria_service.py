from domain.repositories.categoria_repositorio_interface import ICategoriaRepository

class CategoriaService:

    def __init__(self, repo:ICategoriaRepository):
        self.repo = repo

    # 🔹 Listar
    def listar(self):
        return self.repo.listar()
