import flet as ft

def main(page: ft.Page):
    page.title = "Flet counter"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER

    txt_number = ft.TextField(value="0", text_align=ft.TextAlign.RIGHT, width=100)

    def minus_click(event):
        txt_number.value = str(int(txt_number.value) - 1)
        page.update()

    def plus_click(event):
        txt_number.value = str(int(txt_number.value) + 1)
        page.update()

    page.add(
        ft.Row(
            [
                ft.IconButton(ft.icons.REMOVE, on_click=minus_click),
                txt_number,
                ft.IconButton(ft.icons.ADD, on_click=plus_click),
            ],
            alignment=ft.MainAxisAlignment.CENTER,
        )
    )

#Modo Desktop
ft.app(target=main)

#Modo web
#ft.app(target=main, view=ft.AppView.WEB_BROWSER)

