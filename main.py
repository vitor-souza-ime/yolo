# Passo 1: Instalar a biblioteca Ultralytics
!pip install ultralytics --quiet  # --quiet reduz logs desnecessários

# Passo 2: Verificar a versão do Ultralytics
import ultralytics
print(f"Ultralytics version: {ultralytics.__version__}")  # Deve mostrar 8.3.169 ou superior

# Passo 3: Baixar uma imagem da internet
!wget -O imagem.jpg https://upload.wikimedia.org/wikipedia/commons/thumb/f/f5/Chinese_honor_guard_in_column_070322-F-0193C-014.JPEG/640px-Chinese_honor_guard_in_column_070322-F-0193C-014.JPEG --quiet

# Passo 4: Carregar o modelo YOLOv11
from ultralytics import YOLO

# Carregar o modelo YOLOv11n (nano) pré-treinado
try:
    model = YOLO("yolov8l.pt")
    print("Modelo YOLOv8l carregado com sucesso!")
except Exception as e:
    print(f"Erro ao carregar o modelo: {e}")
    print("Tentando baixar o modelo novamente...")
    model = YOLO("yolov8l.pt")  # Tenta novamente (Ultralytics baixa automaticamente)

# Passo 5: Executar a detecção de objetos
results = model.predict(source="imagem.jpg", conf=0.25, save=True, project="runs", name="detect")

# Passo 6: Exibir a imagem com detecções
from PIL import Image
import matplotlib.pyplot as plt

# Caminho da imagem salva com detecções
resultado_imagem_path = "runs/detect/imagem.jpg"

# Verificar se a imagem existe
import os
if os.path.exists(resultado_imagem_path):
    resultado_imagem = Image.open(resultado_imagem_path)
    plt.figure(figsize=(10, 10))
    plt.imshow(resultado_imagem)
    plt.axis('off')  # Remover eixos
    plt.show()
else:
    print(f"Imagem não encontrada em: {resultado_imagem_path}")

# Passo 7: Mostrar detalhes das detecções
for r in results:
    print("Caixas delimitadoras:", r.boxes)  # Informações das caixas
    print("Nomes das classes:", r.names)  # Nomes das classes detectadas
