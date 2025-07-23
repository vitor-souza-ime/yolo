# YOLOv8 - Detecção de Objetos com Ultralytics

Este projeto utiliza o modelo YOLOv8 (You Only Look Once) da biblioteca [Ultralytics](https://github.com/ultralytics/ultralytics) para realizar detecção de objetos em imagens.

## 📌 Objetivo

Demonstrar como instalar, carregar e usar o modelo YOLOv8 para detectar objetos em uma imagem estática.

---

## ⚙️ Requisitos

- Python 3.8+
- pip

Instale as dependências com:

```bash
pip install -r requirements.txt
````

---

## ▶️ Execução

1. Clone este repositório:

```bash
git clone https://github.com/vitor-souza-ime/yolo.git
cd yolo
```

2. Execute o script:

```bash
python main.py
```

---

## 🧠 Modelo

Utiliza-se o modelo `yolov8l.pt`, carregado diretamente da API da Ultralytics. A detecção é feita sobre uma imagem baixada da internet (tropa de honra chinesa).

---

## 📦 Resultado

* A imagem com detecções será salva em: `runs/detect/imagem.jpg`.
* As classes detectadas e coordenadas das caixas delimitadoras serão exibidas no terminal.

---

## 📚 Referências

* [Ultralytics YOLO Docs](https://docs.ultralytics.com/)
* [YOLOv8 GitHub](https://github.com/ultralytics/ultralytics)

---

### ✅ `requirements.txt`

```txt
ultralytics>=8.3.169
matplotlib
Pillow
```

---

### ✅ Repositório GitHub

Você pode criar o repositório neste link:

[https://github.com/vitor-souza-ime/yolo](https://github.com/vitor-souza-ime/yolo)

Após criá-lo, basta executar os comandos:

```bash
git init
git add .
git commit -m "Versão inicial com YOLOv8"
git remote add origin https://github.com/vitor-souza-ime/yolo.git
git push -u origin master
```
