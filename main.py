# main.py

import flet as ft
from controllers.state_manager import app_state
from controllers.navigation_manager import NavigationManager
from components.menu_left import menu_left
from components.header import header
from components.footer import footer
from components.body import body
from views.home_view import EscritorioView
from views.clients_view import ClientesView
from views.invoices_view import FacturacionView
from views.reports_view import ReportesView

def get_view(view_name):
    views = {
        "escritorio": EscritorioView,
        "clientes": ClientesView,
        "facturacion": FacturacionView,
        "reportes": ReportesView,
    }
    return views.get(view_name, EscritorioView)()

class UI(ft.Container):
    def __init__(self, page: ft.Page):
        super().__init__(expand=True)
        self.page = page
        self.page.padding = 0
        self.page.title = "Gestión de Agua Potable"
        self.page.theme_mode = app_state.theme_mode

        # Pasar la referencia de la página a AppState
        app_state.set_page_reference(page)

        # Crear componentes
        self.menu = menu_left(self.change_view, self.page)
        self.header = header(self.toggle_drawer, self.menu, self.page, app_state)
        self.footer = footer(self.page, app_state)
        self.body = body(self.page)
        self.nav_manager = NavigationManager(self.change_view, self.page)

        # Contenedor principal que envolverá toda la UI
        self.main_container = ft.Container(
            content=ft.Column(
                controls=[self.header, self.body, self.footer],
                expand=True,
                spacing=0,
                alignment=ft.MainAxisAlignment.START,
            ),
            expand=True,
            bgcolor='#f8f9ff',  # Se actualizará dinámicamente
            padding=10,  # Espaciado interno opcional
            border_radius=10,  # Bordes redondeados opcionales
        )

        # Layout general con menú lateral y contenido
        self.content = ft.Row(
            controls=[
                self.menu,  # Menú lateral
                self.main_container,  # Contenedor principal
            ],
            expand=True,
        )

        # Establecer el `self.content` como el contenido del Container de UI
        self.content = ft.Container(
            content=self.content,
            expand=True,
            bgcolor='#f8f9ff',
        )

        self.change_view(app_state.current_page)  # Cargar la vista inicial

    def toggle_drawer(self, menu):
        menu.visible = not menu.visible
        self.page.update()

    def change_view(self, vista):
        app_state.set_page(vista)
        self.body.content = get_view(vista)
        self.page.update()

def main(page: ft.Page):
    ui = UI(page)
    app_state.set_page_reference(page)  # Pasar la referencia de la página a AppState
    page.add(ui)

    def on_resize(e):
        ui.menu.width = 150 if page.width <= 600 else 250
        ui.menu.padding = ft.padding.all(5 if page.width <= 600 else 10)
        page.update()

    page.on_resize = on_resize

ft.app(target=main)