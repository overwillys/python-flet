# python-flet
 examples

#Init Commands:

pip install flet
pip install -r requirements.txt


#Flet Commands
ft.app(target=main, view=ft.AppView.WEB_BROWSER) <-- Execute app in web


ft.app(target=main) <-- execute for window

### Ayuda memoria
Al ejecutarse:
En web, cada pestaña represeará una sessión de usuario.
En ventana, solamente será una sección.
Una página representa un CANVAS donde se usan los controles, elementos en pantalla, de los cuales podemos modificarlos a gusto.

#Controles - Interfaz de usuarios o Widgets
Son visibles dentro de la Page, o dentro de otros controles.

Ejemplo:
    lbl_texto = ft.Text(value="Hola mundo", color="green")
    page.controls.append(lbl_texto)

Convenciones de nombres:
    lbl_direccion --> Label
    txt_direccion --> TextField
    cbx_nivel_academico --> ComboBox

Se puede resumir
    page.controls.append(lbl_texto)   <-->     page.add(lbl_texto)

Algunos controles, tipo page es (container) podemos usar para cuando tengamos varios controles, ejemplo puede contener otro controles, ejemplo el row y un esquema de filas:

 page.add(
    ft.Row(controls=[
        ft.Text("A"),
        ft.Text("B"),
        ft.Text("C")
    ])
)



