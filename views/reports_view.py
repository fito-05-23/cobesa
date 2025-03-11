import flet as ft

class ReportesView(ft.Container):
    def __init__(self):
        super().__init__()
        self.content = ft.Text("Generación de Reportes", expand=True)
