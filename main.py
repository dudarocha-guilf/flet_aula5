import flet as ft

def main(page: ft.Page):
    page.title = "Olá Mundo!"
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.vertical_alignment = ft.MainAxisAlignment.CENTER

    page.add(
        ft.Column(
            controls=[
                ft.Text("Topo da Tela"),
                ft.Button(content="Botão do Meio"),
                ft.Text("Base da Tela")
            ],
            horizontal_alignment=ft.CrossAxisAlignment.CENTER
        ),
        ft.Row(
            controls=[
                ft.Text("Esquerda"),
                ft.Button(content="Botão no Meio"),
                ft.Text("Direita")
            ],
            alignment=ft.MainAxisAlignment.CENTER
        )
    )

ft.run(main)