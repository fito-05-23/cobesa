import flet as ft

class FacturacionView(ft.Container):
    def __init__(self):
        super().__init__()
        self.content = ft.Text("Gestión de Facturación", expand=True)