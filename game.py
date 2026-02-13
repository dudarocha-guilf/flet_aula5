import flet as ft

def main(page: ft.Page):
    page.bgcolor="#fc03b6"
    mensagem = ft.Text("Escolha a opção correta!", color="white")
    resposta_correta = "Rosa"

    def verificar_resposta(e):
        if e.control.content == resposta_correta:
            mensagem.value = "Parabéns, Resposta Correta."
        else:
            mensagem.value = "Resposta Incorreta"
        page.update()

    page.title = "Game: Sapatilha da Barbie."
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.vertical_alignment = ft.MainAxisAlignment.CENTER

    page.add(
        ft.Column(
            controls=[
                ft.Text(
                    "Adivinhe a cor da sapatilha da Barbie.",
                    color="#fc03b6",
                    bgcolor="#ffb3e9",
                    size=24,
                    weight="bold",
                    text_align=ft.TextAlign.CENTER
                ),
                ft.Image(
                    src="images/barbie.sap.jpg",
                    height=200
                ),
                ft.Row(
                    controls=[
                        ft.Button(
                            content="Rosa",
                            bgcolor="#fa7ad6",
                            on_click=verificar_resposta
                        ),
                        ft.Button(
                            content="Roxo",
                            bgcolor="#cd7afa",
                            on_click=verificar_resposta
                        ),
                        ft.Button(
                            content="Verde-Água",
                            bgcolor="#7af1fa",
                            on_click=verificar_resposta
                        )
                    ],
                    alignment=ft.MainAxisAlignment.CENTER
                ),
                mensagem
            ],
            horizontal_alignment=ft.CrossAxisAlignment.CENTER

        )
    )

ft.run(main)