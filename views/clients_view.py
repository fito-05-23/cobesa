import flet as ft

class ClientesView(ft.Container):
    def __init__(self):
        super().__init__()
        self.content = ft.Text("Gestión de Clientes", expand=True)