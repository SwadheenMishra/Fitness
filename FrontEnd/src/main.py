import flet as ft
import Login

LogedIn = False

def main(page: ft.Page):
    page.window.height = 725
    page.window.width = 465

    if not LogedIn:
        Login.main(page)

if __name__ == "__main__":
    ft.app(target=main)