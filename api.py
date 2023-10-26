from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()

# Rutas en FastAPI para devolver HTML
@app.get('/', response_class=HTMLResponse)
def index():
    with open('templates/index.html', 'r') as file:
        html_content = file.read()
    return HTMLResponse(content=html_content)

# Rutas para clientes
@app.get('/clientrequest', response_class=HTMLResponse)
def clientrequest():
    with open('templates/clientrequest.html', 'r') as file:
        html_content = file.read()
    return HTMLResponse(content=html_content)

@app.get('/clientship', response_class=HTMLResponse)
def clientship():
    with open('templates/clientship.html', 'r') as file:
        html_content = file.read()
    return HTMLResponse(content=html_content)

@app.get('/clientsell', response_class=HTMLResponse)
def clientsell():
    with open('templates/clientsell.html', 'r') as file:
        html_content = file.read()
    return HTMLResponse(content=html_content)

# Rutas para T2 Piezas Electronicas
@app.get('/t2perequest', response_class=HTMLResponse)
def t2perequest():
    with open('templates/t2perequest.html', 'r') as file:
        html_content = file.read()
    return HTMLResponse(content=html_content)

@app.get('/t2peship', response_class=HTMLResponse)
def t2peship():
    with open('templates/t2peship.html', 'r') as file:
        html_content = file.read()
    return HTMLResponse(content=html_content)

@app.get('/t2pesell', response_class=HTMLResponse)
def t2pesell():
    with open('templates/t2pesell.html', 'r') as file:
        html_content = file.read()
    return HTMLResponse(content=html_content)

@app.get('/t2pewarehouse', response_class=HTMLResponse)
def t2pewarehouse():
    with open('templates/t2pewarehouse.html', 'r') as file:
        html_content = file.read()
    return HTMLResponse(content=html_content)

# Rutas para T2 Piezas Cosmeticas
@app.get('/t2pcrequest', response_class=HTMLResponse)
def t2pcrequest():
    with open('templates/t2pcrequest.html', 'r') as file:
        html_content = file.read()
    return HTMLResponse(content=html_content)

@app.get('/t2pcship', response_class=HTMLResponse)
def t2pcship():
    with open('templates/t2pcship.html', 'r') as file:
        html_content = file.read()
    return HTMLResponse(content=html_content)

@app.get('/t2pcsell', response_class=HTMLResponse)
def t2pcsell():
    with open('templates/t2pcsell.html', 'r') as file:
        html_content = file.read()
    return HTMLResponse(content=html_content)

@app.get('/t2pcwarehouse', response_class=HTMLResponse)
def t2pcwarehouse():
    with open('templates/t2pcwarehouse.html', 'r') as file:
        html_content = file.read()
    return HTMLResponse(content=html_content)

# Ruta para Logística
@app.get('/logship', response_class=HTMLResponse)
def logship():
    with open('templates/logship.html', 'r') as file:
        html_content = file.read()
    return HTMLResponse(content=html_content)
    
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)