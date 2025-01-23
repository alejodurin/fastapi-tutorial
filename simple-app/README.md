# FastAPI simple-app

Este proyecto es una introducción básica a **FastAPI**.
La estructura está diseñada para ser simple y modular.

---

## **Estructura del Proyecto**
```bash
simple-app/
│
├── main.py
├── venv/
│   ├── bin/               
│   ├── Scripts/           
│   ├── lib/               
│   └── pyvenv.cfg         
├── requirements.txt
└── routes/
    └── simple_route.py
```

---

## **Requisitos**

- Python 3.11
- `pip` (Administrador de paquetes de Python)

---

## **Instalación**

1. Clona este repositorio:
   ```bash
   git clone https://github.com/alejodurin/fastapi-tutorial
   cd simple-app/
   ```
2. Crea el entorno virtual
  ```bash
   python3 -m venv venv
  ```
3. Activa el entorno virtual
   
   Para linux
   `source venv/bin/activate`
   
   Para windows
   `venv\Scripts\activate`
5. Instalar dependencias
   
   `pip install -r requirements.txt`

## USO

Ejecutar `python main.py`

Abre tu navegador y accede a:

- Documentación interactiva (Swagger UI): http://127.0.0.1:8000/docs
- Documentación alternativa (ReDoc): http://127.0.0.1:8000/redoc
- Ruta personalizada: http://127.0.0.1:8000/hello


