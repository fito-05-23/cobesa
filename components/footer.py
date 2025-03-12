# components/footer.py 

import flet as ft
from config import COLORS

def footer(page: ft.Page, app_state):
    footer_container = ft.Container(
        content=ft.Row(
            controls=[ft.Text("© 2025 - D@Code", size=12, 
                weight=ft.FontWeight.W_900,
                color=COLORS["primary"])],
                alignment=ft.MainAxisAlignment.END,
        ),
        height=20,
        bgcolor=COLORS["background"], 
        padding=ft.padding.only(bottom=2, right=15),
        alignment=ft.alignment.center_right,  # Alinea el contenedor al margen derecho
    )

    return footer_container
