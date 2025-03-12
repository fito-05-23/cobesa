# controllers/navigation_manager.py

import flet as ft
from controllers.state_manager import app_state  # Importamos el estado global

class NavigationManager:
    def __init__(self, change_view, page: ft.Page):
        self.change_view = change_view
        self.page = page
        self.nav_menu = None  # Guarda el menú para futuras actualizaciones

        # Definir las vistas disponibles
        self.views = [
            "escritorio",
            "clientes",
            "facturacion",
            "pagos",
            "reportes",
            "configuracion"
        ]

    def on_nav_change(self, e):
        """Maneja el cambio de vista cuando se selecciona un nuevo destino."""
        selected_page = e.control.data  # Obtener el identificador de la vista
        app_state.set_page(selected_page)  # Actualizar el estado global
        self.update_navigation_menu()  # Actualizar la UI
        self.change_view(selected_page)
        self.page.update()

    def create_nav_button(self, icon, view_name):
        """Crea un botón de navegación con estado dinámico."""
        return ft.Container(
            padding=ft.padding.only(left=15),  # Aplica padding izquierdo al contenedor
            content=ft.TextButton(
                content=ft.Row(
                    controls=[ft.Container(
                        padding=ft.padding.only(right=15),  # Padding derecho al contenedor del icono
                        content=ft.Icon(icon, size=24)
                    )],
                    alignment=ft.MainAxisAlignment.CENTER,  # Alineación de los iconos en el Row
                ),
                on_click=self.on_nav_change,
                data=view_name,
                style=ft.ButtonStyle(
                    bgcolor='#f8f9ff' if app_state.current_page == view_name else "transparent",
                    shape=ft.RoundedRectangleBorder(
                        radius=ft.border_radius.only(top_left=20, bottom_left=20),
                    ),
                ),
                height=50,
                width=75,  # Ancho del botón
            )
        )

    def get_navigation_menu(self):
        """Crea el menú lateral con botones y logo, si aún no existe."""
        if not self.nav_menu:
            self.nav_menu = ft.Column(
                controls=[
                    ft.Container(
                        content=ft.Image(
                            src="assets/logo_ON_PRIMARY_CONTAINER.svg",
                            width=36,
                            height=36,
                            fit=ft.ImageFit.CONTAIN,
                            color=ft.colors.ON_PRIMARY_CONTAINER
                        ),
                        padding=ft.padding.only(top=20, bottom=20),
                    ),
                    # Colocamos todos los botones en la misma columna
                    self.create_nav_button(ft.icons.HOME, "escritorio"),
                    self.create_nav_button(ft.icons.PERSON, "clientes"),
                    self.create_nav_button(ft.icons.ASSESSMENT, "facturacion"),
                    self.create_nav_button(ft.icons.PAYMENT, "pagos"),
                    self.create_nav_button(ft.icons.RECEIPT, "reportes"),
                    self.create_nav_button(ft.icons.SETTINGS, "configuracion"),
                ],
                expand=True,
                spacing=10,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,  # Centra todos los elementos dentro de la columna
            )

        self.page.update()
        return self.nav_menu

    def update_navigation_menu(self):
        """Actualiza dinámicamente los botones de navegación sin afectar el logo."""
        if self.nav_menu:
            # Mantener el logo en su lugar y actualizar los botones
            self.nav_menu.controls = [
                self.nav_menu.controls[0],  # Mantiene el logo en su lugar
                self.create_nav_button(ft.icons.HOME, "escritorio"),
                self.create_nav_button(ft.icons.PERSON, "clientes"),
                self.create_nav_button(ft.icons.ASSESSMENT, "facturacion"),
                self.create_nav_button(ft.icons.PAYMENT, "pagos"),
                self.create_nav_button(ft.icons.RECEIPT, "reportes"),
                self.create_nav_button(ft.icons.SETTINGS, "configuracion"),
            ]
            self.page.update()



