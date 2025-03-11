# components/menu_left.py 

import flet as ft
from controllers.navigation_manager import NavigationManager
from controllers.state_manager import app_state  # Importamos el estado global

def menu_left(change_view, page: ft.Page):
    nav_manager = NavigationManager(change_view, page)

    menu_container = ft.Container(
        width=85,
        bgcolor=app_state.menu_bgcolor,
        content=ft.Column(
            [
                nav_manager.get_navigation_menu(),
                ft.Container(
                    content=ft.IconButton(
                        icon=ft.icons.LOGOUT,
                        icon_color=ft.colors.ON_PRIMARY_CONTAINER,
                        tooltip="Salir",
                        on_click=lambda e: print("Cerrar sesión")
                    ),
                    bgcolor=app_state.menu_bgcolor,
                    alignment=ft.alignment.center,
                ),
                ft.Container(
                    ft.Switch(
                        value=app_state.theme_mode == ft.ThemeMode.DARK,
                        on_change=lambda e: toggle_theme(e, page),
                        thumb_color=ft.colors.ON_PRIMARY_CONTAINER if app_state.theme_mode == ft.ThemeMode.LIGHT else ft.colors.WHITE,  # Color del ícono cuando está en modo claro o oscuro
                        track_color=ft.colors.PRIMARY_CONTAINER if app_state.theme_mode == ft.ThemeMode.LIGHT else ft.colors.DARK_GRAY,  # Color de la pista según el tema
                        track_outline_color=ft.colors.ON_PRIMARY_CONTAINER if app_state.theme_mode == ft.ThemeMode.LIGHT else ft.colors.GRAY,  # Color del borde de la pista
                        thumb_icon=ft.icons.LIGHT_MODE if app_state.theme_mode == ft.ThemeMode.DARK else ft.icons.DARK_MODE,  # Ícono dinámico según el tema
                    ),
                    bgcolor=app_state.menu_bgcolor,  # Color de fondo del contenedor
                    padding=10,  # Espaciado interno para que no quede pegado a los bordes
                    alignment=ft.alignment.center,  # Centrar el Switch dentro del contenedor
                )
            ],
            expand=True,
            spacing=1,
            #alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
        )
    )

    return menu_container

def toggle_theme(e, page):
    """Alternar entre modo claro y oscuro."""
    app_state.toggle_theme()
    page.theme_mode = app_state.theme_mode
    page.update()  # Actualizar la página para reflejar los cambios