from flet import *

def main(page: Page):
    BG='#041955'
    FWG='#97b4ff'
    FG='#3450a1'
    PINK='#eb06ff'
    
    page.add(
            Container(
            width=page.width * 0.9,  # 90% del ancho de la página
            height=page.height * 0.9,  # 90% del alto de la página
            bgcolor=BG,
            border_radius=35,
            alignment=alignment.center,  # Centra el contenido del contenedor
            )
        )    

app(target=main)