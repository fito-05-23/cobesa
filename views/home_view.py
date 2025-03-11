# /views/home_view.py 

import flet as ft

class EscritorioView(ft.Container):
    def __init__(self):
        super().__init__()

         # Función para crear una tarjeta pequeña
        def create_card(icono, numero, nombre, porcentaje, color_icono, sube=True):
            return ft.Container(
                expand=True,
                height=90,
                border_radius=10,
                bgcolor='#f8f9ff',  # Se actualizará dinámicamente,
                padding=10,
                content=ft.Column(
                    controls=[
                        # Icono redondo arriba
                        ft.Container(
                            content=ft.Icon(icono, color=color_icono, size=24),
                            bgcolor=ft.colors.BLUE_GREY_100,
                            width=40,
                            height=40,
                            border_radius=20,
                            alignment=ft.alignment.center,
                            margin=ft.margin.only(top=-10),
                        ),
                        # Número grande
                        ft.Text(str(numero), size=24, weight=ft.FontWeight.BOLD, text_align=ft.TextAlign.CENTER),
                        # Nombre de la tarjeta
                        ft.Text(nombre, size=14, text_align=ft.TextAlign.CENTER),
                        # Porcentaje con icono de subida o bajada
                        ft.Row(
                            controls=[
                                ft.Icon(ft.icons.TRENDING_UP if sube else ft.icons.TRENDING_DOWN, color=ft.colors.GREEN if sube else ft.colors.RED, size=14),
                                ft.Text(f"{porcentaje}%", size=12, color=ft.colors.GREEN if sube else ft.colors.RED),
                            ],
                            alignment=ft.MainAxisAlignment.CENTER
                        )
                    ],
                    alignment=ft.MainAxisAlignment.CENTER,
                    spacing=5,
                )
            )
            
        # Contenedor 1 con filas internas
        contenedor_1 = ft.Container(
            bgcolor=ft.colors.WHITE,
            height=150,
            border_radius=10,
            border=ft.border.all(1, ft.colors.GREY_200),  # Borde suave
            content=ft.Column(
                controls=[
                    # Row superior (título e icono de tres puntos)
                    ft.Row(
                        controls=[
                            ft.Text("Diario", color=ft.colors.ON_PRIMARY_CONTAINER, size=16, weight=ft.FontWeight.BOLD),
                            ft.Icon(ft.icons.MORE_VERT)  # Icono de tres puntos
                        ],
                        alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                        vertical_alignment=ft.CrossAxisAlignment.CENTER,
                        height=33,
                    ),
                    # Row inferior (tarjetas pequeñas)
                     # Row inferior (tarjetas pequeñas mejoradas)
                    ft.Row(
                        controls=[
                            create_card(ft.icons.SHOW_CHART, 120, "Ventas", 5.2, ft.colors.BLUE, True),
                            create_card(ft.icons.SHOPPING_CART, 45, "Compras", -2.8, ft.colors.ORANGE, False),
                            create_card(ft.icons.PEOPLE, 320, "Clientes", 3.1, ft.colors.GREEN, True),
                            create_card(ft.icons.STAR, 89, "Puntos", -1.4, ft.colors.PURPLE, False),
                        ],
                        spacing=10,
                        alignment=ft.MainAxisAlignment.CENTER,
                    ),
                ],
                spacing=10,
            ),
            padding=ft.padding.only(left=15, right=10),
        )

        # Contenedor principal con un diseño de fila (Row)
        row_content = ft.Row(
            controls=[
                # Lado izquierdo: Tres tarjetas blancas apiladas verticalmente
                ft.Container(
                    alignment=ft.alignment.center,
                    bgcolor='#f8f9ff',  # Se actualizará dinámicamente,
                    width=550,
                    border_radius=10,
                    content=ft.Column(
                        controls=[
                            contenedor_1,  # Aquí se agrega el nuevo contenedor
                            ft.Container(
                                content=ft.Text("Contenedor 2"),
                                alignment=ft.alignment.center,
                                bgcolor=ft.colors.WHITE,
                                height=150,
                                border=ft.border.all(1, ft.colors.GREY_200),  # Borde suave
                                border_radius=10,
                            ),
                            ft.Container(
                                content=ft.Text("Contenedor 3"),
                                alignment=ft.alignment.center,
                                bgcolor=ft.colors.WHITE,
                                height=300,
                                border=ft.border.all(1, ft.colors.GREY_200),  # Borde suave
                                border_radius=10,
                            ),
                        ],
                        spacing=10,
                    ),
                    expand=True,
                ),
                # Lado derecho: Una tarjeta vertical que ocupa toda la altura
                ft.Container(
                    content=ft.Text("Clickable without Ink"),
                    alignment=ft.alignment.center,
                    bgcolor=ft.colors.WHITE,
                    width=350,
                    height=620,
                    border=ft.border.all(1, ft.colors.GREY_200),  # Borde suave
                    border_radius=10,
                ),
            ],
            expand=True,
        )

        # Agregar el scroll vertical al layout
        self.content = ft.Column(
            controls=[row_content],
            scroll=ft.ScrollMode.AUTO,
            expand=True,
        )

