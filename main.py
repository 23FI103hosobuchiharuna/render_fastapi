from typing import Optional

from fastapi import FastAPI

from fastapi.responses import HTMLResponse #インポート

import random  # randomライブラリを追加

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: Optional[str] = None):
    return {"item_id": item_id, "q": q}




@app.get("/index")
def index():
    html_content = """
    <html>
        <head>
            <title>23FI103 webpage</title>
        </head>
        <body>
            <h1>Look! HTML!</h1>
            <h2>-------</h2>
            <h2>||||||||||</h2>
            <h2>-------</h2>
            <h1>My Number Is 23FI103</h1>
        </body>
    </html>
    """
    return HTMLResponse(content=html_content, status_code=200)


@app.post("/present")
async def give_present(present):
    return {"response": f"サーバです。メリークリスマス！ {present}ありがとう。お返しはキャンディーです。"}  # f文字列というPythonの機能を使っている