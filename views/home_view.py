# /views/home_view.py 

import flet as ft
from config import COLORS

class SampleRod(ft.BarChartRod):
    def __init__(self, y: float, hovered: bool = False):
        super().__init__()
        self.hovered = hovered
        self.y = y
        self.width = 20  # Aumenté el ancho de la barra

    def _before_build_command(self):
        self.to_y = self.y + 1 if self.hovered else self.y
        self.color = COLORS["bar_hover"] if self.hovered else COLORS["bar_default"] 
        self.border_side = (
            ft.BorderSide(width=1, color=COLORS["bar_border_hover"])
            if self.hovered
            else ft.BorderSide(width=0, color=COLORS["bar_border_default"])
        )
        super()._before_build_command()

    def _build(self):
        self.tooltip = str(self.y)
        self.width = 40
        self.color = ft.Colors.WHITE
        self.bg_to_y = 20
        self.bg_color = ft.Colors.WHITE
        
class EscritorioView(ft.Container):
    def __init__(self):
        super().__init__()

        def on_chart_event(e: ft.BarChartEvent):
            for group_index, group in enumerate(chart.bar_groups):
                for rod_index, rod in enumerate(group.bar_rods):
                    rod.hovered = e.group_index == group_index and e.rod_index == rod_index
            chart.update()
            
        chart = ft.BarChart(
            min_y=0,  # Altura mínima de la gráfica
            max_y=15, 
            bar_groups=[
                ft.BarChartGroup(
                    x=0,
                    bar_rods=[SampleRod(5)],
                ),
                ft.BarChartGroup(
                    x=1,
                    bar_rods=[SampleRod(6.5)],
                ),
                ft.BarChartGroup(
                    x=2,
                    bar_rods=[SampleRod(5)],
                ),
                ft.BarChartGroup(
                    x=3,
                    bar_rods=[SampleRod(7.5)],
                ),
                ft.BarChartGroup(
                    x=4,
                    bar_rods=[SampleRod(9)],
                ),
                ft.BarChartGroup(
                    x=5,
                    bar_rods=[SampleRod(11.5)],
                ),
                ft.BarChartGroup(
                    x=6,
                    bar_rods=[SampleRod(6)],
                ),
            ],
            bottom_axis=ft.ChartAxis(
                labels=[
                    ft.ChartAxisLabel(value=0, label=ft.Text("Enero")),
                    ft.ChartAxisLabel(value=1, label=ft.Text("Febrero")),
                    ft.ChartAxisLabel(value=2, label=ft.Text("Marzo")),
                    ft.ChartAxisLabel(value=3, label=ft.Text("Abril")),
                    ft.ChartAxisLabel(value=4, label=ft.Text("Mayo")),
                    ft.ChartAxisLabel(value=5, label=ft.Text("Junio")),
                    ft.ChartAxisLabel(value=6, label=ft.Text("Julio")),
                ],
            ),
            on_chart_event=on_chart_event,
            interactive=True,
        )
        
        # Función para crear una tarjeta pequeña
        def create_card(icono, numero, nombre, porcentaje, color_icono, sube=True):
            return ft.Container(
                expand=True,
                border_radius=10,
                bgcolor='#f8f9ff',
                padding=ft.padding.only(top=1, left=15, right=10, bottom=5),
                alignment=ft.alignment.center,  # Centra el contenido dentro del contenedor
                content=ft.Column(
                    controls=[
                        # Icono redondo arriba
                        ft.Container(
                            content=ft.Icon(icono, color=color_icono, size=18),  # Aumenté el tamaño del ícono
                            bgcolor=ft.colors.BLUE_GREY_100,
                            width=33,  # Ajusté el tamaño del círculo
                            height=33,
                            border_radius=20,
                            alignment=ft.alignment.center,  # Centra el ícono dentro del contenedor
                        ),
                        ft.Container(
                            content=ft.Column(
                                controls=[
                                    ft.Text(
                                        str(numero), 
                                        size=22,  # Aumenté el tamaño del número
                                        color=COLORS["primary"], 
                                        weight=ft.FontWeight.BOLD, 
                                        text_align=ft.TextAlign.CENTER
                                    ),
                                    # Nombre de la tarjeta
                                    ft.Text(nombre, size=14, color=COLORS["primary"], text_align=ft.TextAlign.CENTER),
                                ],
                                spacing=2  # Espacio entre los textos
                            ),
                            alignment=ft.alignment.center,
                            padding=ft.padding.only(top=10),
                        ),
                      
                        # Porcentaje con icono de subida o bajada
                        ft.Row(
                            controls=[
                                ft.Icon(ft.icons.TRENDING_UP if sube else ft.icons.TRENDING_DOWN, 
                                        color=ft.colors.GREEN if sube else ft.colors.RED, size=14),
                                ft.Text(f"{porcentaje}%", size=12, color=ft.colors.GREEN if sube else ft.colors.RED),
                            ],
                            alignment=ft.MainAxisAlignment.END  # Centra el porcentaje
                        )
                    ],
                    alignment=ft.MainAxisAlignment.CENTER,  # Asegura que todo el contenido de la tarjeta esté centrado
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,  # Asegura el centrado horizontal
                    spacing=0,  # Espaciado entre elementos
                )
            )

        # Contenedor 1 con filas internas
        contenedor_1 = ft.Container(
            bgcolor=ft.colors.WHITE,
            #expand=True,
            height=180,
            border_radius=10,
            border=ft.border.all(1, ft.colors.GREY_200),  # Borde suave
            content=ft.Column(
                controls=[
                    # Row superior (título e icono de tres puntos)
                    ft.Row(
                        controls=[
                            ft.Text("Diario", color=COLORS["primary"], size=16, weight=ft.FontWeight.BOLD),
                            ft.Icon(ft.icons.MORE_VERT, color=COLORS["primary"])  # Icono de tres puntos
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
                                chart, 
                                bgcolor=ft.Colors.WHITE, 
                                padding=ft.padding.only(top=10, left=20, right=20, bottom=20),
                                border=ft.border.all(1, ft.colors.GREY_200),  # Borde suave
                                border_radius=10, 
                                expand=True,
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
                    content=ft.Column(
                        controls=[
                            ft.Container(
                                bgcolor=ft.Colors.WHITE, 
                                padding=ft.padding.only(top=10, left=20, right=20, bottom=20),
                                border=ft.border.all(1, ft.colors.GREY_200),  # Borde suave
                                border_radius=10, 
                            ),
                            ft.Container(
                                content=ft.Text("Contenedor 5"),
                                alignment=ft.alignment.center,
                                bgcolor=ft.colors.WHITE,
                                border=ft.border.all(1, ft.colors.GREY_200),  # Borde suave
                                border_radius=10,
                            ),
                        ],
                        spacing=10,
                    ),
                    #expand=True,
                    alignment=ft.alignment.center,
                    bgcolor=ft.colors.WHITE,
                    width=450,
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

