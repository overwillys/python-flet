import flet as ft


# def main(page: ft.Page):
#     page.add(
#         ft.Row(
#             controls=[
#                 ft.Text("A"),
#                 ft.Text("B"),
#                 ft.Text("C"),
#             ]
#         )
#     )

#Otra manera de crear lo mismo 

def main(page: ft.Page):
    lenguajes = ['C++', 'Java', 'Python', 'JavaScript']
    etiquetas = []
    
    #usando un array para la lista
    for e in lenguajes:
        etiquetas.append(ft.Text(e))
    
    row_datos = ft.Row(controls=etiquetas)    
        
    #row_datos = ft.Row(controls=[ft.Text('Python'), ft.Text('Flet'), ft.Text('Flutter')])
    page.add(row_datos)

ft.app(target=main, view=ft.AppView.WEB_BROWSER)
