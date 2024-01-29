import flet as ft




def main(page: ft.Page):
    
    txt_nombre = ft.TextField(label="Digite tu nombre")    
    lbl_saludo = ft.Text() 
    
    def Saludar(event):
        lbl_saludo.value = f'Hola...{txt_nombre.value}!'
        page.update()
        
    row = ft.Row(controls=[
        #ft.TextField(label="Digite su nombre"),
        txt_nombre,
        ft.ElevatedButton(text="Saludar", on_click=Saludar),
        lbl_saludo
        
    ])
    
    page.add(row)


ft.app(target=main, view=ft.AppView.WEB_BROWSER)
