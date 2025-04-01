# 🎮 Jogo da Forca - Web App com Flask  

## 📌 Descrição  
Este é um jogo da forca desenvolvido com **Python** e **Flask**, disponibilizado como um container Docker ou em K8S. 

💡 **Objetivo:** Facilitar a execução do jogo sem necessidade de instalar dependências locais, utilizando **Docker Hub** ou k8s.  

🔗 **Imagem no Docker Hub:**  
[NicolasMartinns/Hangman](https://hub.docker.com/repository/docker/nicolasmartinss/hangman/general)  

---

## 🔧 Tecnologias Utilizadas  
- **Python** – Linguagem principal do projeto  
- **Flask** – Framework web para rodar a aplicação  
- **Docker** – Para empacotamento e distribuição da aplicação
- **Kuberenetes** - Para disponibilizar a aplicação no cluster

---

## 🐋 Como Executar com Docker

### ✅ Pré-requisitos  
✔ Ter o **Docker** instalado na máquina  

### 🏗️ Passo a Passo  

1️⃣ **Baixe e execute o container do jogo:**  
```bash
docker run -d -p 5000:5000 nicolasmartinss/hangman:v1
```

🎉 A sua aplicação estará disponível no localhost:5000


## ☸️ Como Executar com K8S

### ✅ Pré-requisitos  
✔ Ter o **KIND e kubectl** instalado na máquina  

### 🏗️ Passo a Passo  

1️⃣ **Crie o cluster kubernetes:**
```bash
kind create cluster --name nome-do-cluster --config k8s/kind-config.yaml
```

2️⃣ **Crie o Deployment e Service dentro do Cluster**  
```bash
kubectl apply -f k8s/deployment.yaml
```

🎉 A sua aplicação estará disponível no localhost:30000