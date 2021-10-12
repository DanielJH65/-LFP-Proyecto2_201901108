import webbrowser

class HTML:
    def generarHTML(html, nombre):  
        pagina = open(nombre+'.html', 'w')
        salida=""
        salida =f"""<html lang="es">
    <head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link href="https://bootswatch.com/4/superhero/bootstrap.min.css" rel="stylesheet" type="text/css">
    <title>{nombre}</title>
    </head>
    <body style="margin:0;padding:0;">"""
        salida+=html
        salida += """</body>
        </html>
        """
        
        pagina.write(salida)
        pagina.close()
        webbrowser.open_new_tab(nombre+'.html')