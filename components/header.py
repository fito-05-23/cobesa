# components/header.py

import flet as ft
from config import COLORS

def open_profile(e):
    print("Abrir perfil")

def open_settings(e):
    print("Abrir configuraciones")

def close_menu(e):
    print("Cerrar sesión")

def header(toggle_drawer, menu, page: ft.Page, app_state):
    # Contenedor para la barra de búsqueda, icono de notificaciones, avatar de usuario y menú contextual
    search_notifications_container = ft.Container(
        content=ft.Row(
            controls=[
                # Input de búsqueda
                ft.TextField(
                    hint_text="Buscar...",
                    prefix_icon=ft.Icon(ft.icons.SEARCH),
                    border_radius=ft.border_radius.all(20),
                    height=35,
                    content_padding=ft.padding.only(left=10, right=10),
                    border_color=ft.colors.PRIMARY_CONTAINER,
                    width=250,
                ),
                # Icono de notificaciones
                ft.IconButton(
                    icon=ft.icons.NOTIFICATIONS,
                    #icon_color=ft.colors.ON_PRIMARY_CONTAINER,
                    tooltip="Notificaciones",
                    on_click=lambda e: print("Notificaciones clicked"),
                ),
                # Avatar de usuario
                ft.CircleAvatar(
                    foreground_image_src="https://avatars.githubusercontent.com/u/5041459?s=88&v=4",
                    radius=20,
                ),
                # Menú contextual de usuario
                ft.PopupMenuButton(
                    content=ft.Icon(ft.icons.ARROW_DROP_DOWN),
                    menu_position=ft.PopupMenuPosition.UNDER,  # Hace que el menú se despliegue debajo del icono
                    elevation=4,  # Reduce la sombra del menú para que no sea tan pronunciada
                    bgcolor=ft.colors.WHITE,  # Fondo blanco del menú
                    items=[
                        ft.PopupMenuItem(
                            content=ft.Row(
                                [
                                    ft.Icon(ft.Icons.PERSON),
                                    ft.Text("Perfil"),
                                ]
                            ),
                            on_click=open_profile,
                        ),
                        ft.PopupMenuItem(
                            content=ft.Row(
                                [
                                    ft.Icon(ft.Icons.SETTINGS),
                                    ft.Text("Configuraciones"),
                                ]
                            ),
                            on_click=open_settings,
                        ),
                        ft.Divider(),  # Separador
                        ft.PopupMenuItem(
                            content=ft.Row(
                                [
                                    ft.Icon(ft.Icons.LOGOUT),
                                    ft.Text("Cerrar sesión"),
                                ]
                            ),
                            on_click=close_menu,
                        ),
                    ],
                ),
            ],
            alignment=ft.MainAxisAlignment.END,  # Alinea los elementos a la derecha
            spacing=10,  # Espaciado entre los elementos
        ),
        alignment=ft.alignment.center_right,  # Alinea el contenedor al margen derecho
        padding=ft.padding.only(right=10),
    )

    # Contenedor principal del header
    header_container = ft.Container(
        content=ft.Row(
            controls=[
                # Texto de bienvenida
                ft.Text(
                    "Bienvenido, Usuario!", 
                    size=24, 
                    weight=ft.FontWeight.W_900,
                    color=ft.colors.ON_PRIMARY_CONTAINER
                ),
                # Contenedor con búsqueda, notificaciones, avatar y menú
                search_notifications_container,
            ],
            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,  # Separa el texto a la izquierda y el contenido a la derecha
            spacing=10,
        ),
        height=65,
        padding=ft.padding.only(left=10, right=10),
        bgcolor=COLORS["background"], 
    )

    return header_container





