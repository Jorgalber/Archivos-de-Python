import flet as ft

def main (page:ft.page):
    page.fonts = {"RobotoSlab": "https://github.com/google/fonts/raw/main/apache/robotoslab/RobotoSlab%5Bwght%5D.ttf"}
    page.title="Pokédex"
    t=ft.Text(value="Pokédex", color="red",font_family="RobotoSlab",weight=ft.FontWeight.W_100, style=ft.TextThemeStyle.DISPLAY_LARGE)
    page.controls.append(t)
    page.update()

ft.app(target=main)