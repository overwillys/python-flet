import flet as ft

def main(page: ft.Page):
    lbl_texto = ft.Text(value="Hola mundo", color="green")
    page.controls.append(lbl_texto)
    page.update()

#Lanzar modo escritorio    
#ft.app(target=main)

#Lanzar modo web
ft.app(target=main, view=ft.AppView.WEB_BROWSER)   