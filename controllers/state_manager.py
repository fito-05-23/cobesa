# controllers/state_manager.py

import flet as ft

class AppState:
    def __init__(self):
        self._theme_mode = ft.ThemeMode.LIGHT  # Tema inicial: modo claro
        self._current_page = "escritorio"  # Página actual

        # Definir colores base
        self._primary_light = "#f8f9ff"  # Nuevo color base_light d1e4ff
        self._secondary_light = "#d1e4ff"  # Nuevo color base_light d1e4ff
        
        self._menu_bgcolor = self._get_menu_bgcolor()
        self._header_bgcolor = self._get_header_bgcolor()
        self._footer_bgcolor = self._get_footer_bgcolor()
        self._body_bgcolor = self._get_body_bgcolor()

        self._page = None  # Referencia a la página

    def _get_menu_bgcolor(self):
        return ft.colors.PRIMARY_CONTAINER if self._theme_mode == ft.ThemeMode.LIGHT else "#2E3440"

    def _get_header_bgcolor(self):
        return self._primary_light if self._theme_mode == ft.ThemeMode.LIGHT else "#4C566A"

    def _get_footer_bgcolor(self):
        return self._primary_light if self._theme_mode == ft.ThemeMode.LIGHT else "#3B4252"

    def _get_body_bgcolor(self):
        return self._primary_light if self._theme_mode == ft.ThemeMode.LIGHT else self._secondary_light

    @property
    def base_light(self):
        return self._primary_light  # Retornar color base_light

    @property
    def theme_mode(self):
        return self._theme_mode

    @property
    def current_page(self):
        return self._current_page

    @property
    def menu_bgcolor(self):
        return self._menu_bgcolor

    @property
    def header_bgcolor(self):
        return self._header_bgcolor

    @property
    def footer_bgcolor(self):
        return self._footer_bgcolor

    @property
    def body_bgcolor(self):
        return self._body_bgcolor

    def set_page_reference(self, page):
        """Establecer la referencia a la página."""
        self._page = page

    def toggle_theme(self):
        """Alternar entre modo claro y oscuro."""
        self._theme_mode = ft.ThemeMode.DARK if self._theme_mode == ft.ThemeMode.LIGHT else ft.ThemeMode.LIGHT
        self._update_colors()  # Actualizar colores al cambiar el tema
        if self._page:
            self._page.update()  # Actualizar la página para reflejar los cambios

    def _update_colors(self):
        """Actualizar los colores según el tema actual."""
        self._menu_bgcolor = self._get_menu_bgcolor()
        self._header_bgcolor = self._get_header_bgcolor()
        self._footer_bgcolor = self._get_footer_bgcolor()
        self._body_bgcolor = self._get_body_bgcolor()

    def set_page(self, page):
        """Establecer la página actual."""
        self._current_page = page

app_state = AppState()

