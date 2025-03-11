# components/body.py 

import flet as ft
from controllers.state_manager import app_state  # Importamos el estado global
from config import COLORS

def body(page: ft.Page):
    # Usar el color de fondo dinámico del estado global
    body_container = ft.Container(
        content=ft.Text("Bienvenido al sistema", size=16),
        expand=True,  # Ocupa el espacio restante
        bgcolor=COLORS["background"], 
        alignment=ft.alignment.center,
        padding=ft.padding.all(20),
    )

    return body_container

