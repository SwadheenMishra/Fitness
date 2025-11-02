import flet as ft
from flet import Colors

def main(page: ft.Page):
    page.clean()
    page.title = "Fitness sing_up"
    page.theme_mode = ft.ThemeMode.DARK
    page.horizontal_alignment = "center"
    page.vertical_alignment = "center"
    page.bgcolor = Colors.BLACK
    page.padding = 0

    # Background layer (image + gradient)
    background = ft.Stack(
        [
            # Background image
            ft.Image(
                src="img1.png",
                width=page.width,
                height=page.height,
                fit=ft.ImageFit.COVER,
                expand=True,
            ),

            # Gradient overlay
            ft.Container(
                expand=True,
                gradient=ft.LinearGradient(
                    begin=ft.alignment.bottom_center,
                    end=ft.alignment.top_center,
                    colors=[
                        ft.Colors.with_opacity(0.85, Colors.BLACK),
                        ft.Colors.with_opacity(0.4, Colors.BLACK),
                    ],
                ),
            ),

            ft.Column(
                [
                    ft.Container(height=100),
                    ft.Text(
                        "FITNESS",
                        size=42,
                        weight=ft.FontWeight.BOLD,
                        color=Colors.WHITE,
                    ),
                    ft.Container(height=20),
                    ft.TextField(
                        label="OTP",
                        border_radius=14,
                        bgcolor=ft.Colors.with_opacity(0.4, Colors.BLACK),
                        color=Colors.WHITE,
                        border_color="transparent",
                        content_padding=ft.Padding(16, 12, 16, 12),
                        width=320,
                    ),
                    ft.Container(height=5),
                    ft.OutlinedButton(
                        text="Create Account",
                        width=320,
                        height=50,
                        style=ft.ButtonStyle(
                            shape=ft.RoundedRectangleBorder(radius=14),
                            color={ft.ControlState.DEFAULT: Colors.WHITE},
                            side={ft.ControlState.DEFAULT: ft.BorderSide(1, Colors.WHITE)},
                        ),
                    ),
                    ft.Container(height=40),
                ],
                alignment=ft.MainAxisAlignment.CENTER,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            ),
        ],
        expand=True,
    )

    page.add(background)

if __name__ == "__main__":
    ft.app(target=main)
