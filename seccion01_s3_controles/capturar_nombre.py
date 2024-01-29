import flet as ft




def main(page: ft.Page):
    
    txt_nombre = ft.TextField(label="Digite tu nombre")
    
    def Saludar(event):
        print(f'Hola...{txt_nombre.value}!')
        
    row = ft.Row(controls=[
        #ft.TextField(label="Digite su nombre"),
        txt_nombre,
        ft.ElevatedButton(text="Saludar", on_click=Saludar)
        
    ])
    
    page.add(row)


ft.app(target=main, view=ft.AppView.WEB_BROWSER)
