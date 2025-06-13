from fastapi.responses import HTMLResponse #インポート

### コードいろいろ... ###

@app.get("/index")
def index():
    html_content = """
    <html>
        <head>
            <title>23FI103 webpage</title>
        </head>
        <body>
            <h1>Look! HTML!</h1>
        </body>
    </html>
    """
    return HTMLResponse(content=html_content, status_code=200)