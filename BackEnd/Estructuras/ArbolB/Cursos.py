class Cursos:
    def __init__(self, codigo, nombre, no_creditos,prerequisito,obligatorio):
        self.codigo = codigo
        self.nombre = nombre
        self.no_creditos = no_creditos
        self.prerequisitos = prerequisito
        self.obligatorio = obligatorio
