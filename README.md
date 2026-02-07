# 🤖 Chatbot em Python com OpenRouter

Este projeto é um **chatbot simples em Python**, executado diretamente no terminal, que utiliza um modelo de linguagem acessado via **OpenRouter** para responder às mensagens do usuário de forma interativa.

O foco do projeto é **aprendizado prático** e construção de um **portfólio inicial**, demonstrando integração com APIs, lógica de programação, uso de variáveis de ambiente e organização básica de código.

---

## 🧠 O que o projeto faz

* Recebe mensagens digitadas pelo usuário no terminal
* Envia essas mensagens para um modelo de linguagem via API
* Exibe a resposta do chatbot
* Mantém o histórico da conversa durante a execução
* Permite encerrar o chat com o comando `SAIR`

---

## 🛠️ Tecnologias utilizadas

* **Python 3**
* **OpenRouter API**
* **python-dotenv** (variáveis de ambiente)
* **OpenAI SDK** (compatível com OpenRouter)

---

## 📂 Estrutura do projeto

```
chatbot/
│
├── chatbot.py
├── .env
└── README.md
```

---

## ⚙️ Pré-requisitos

Antes de executar o projeto, você precisa ter:

* Python 3.10 ou superior instalado
* Conta no OpenRouter
* Uma chave de API válida

---

## 🔐 Configuração da API

Crie um arquivo chamado `.env` na raiz do projeto com o seguinte conteúdo:

```
OPENROUTER_API_KEY=sua_chave_de_api_aqui
```

⚠️ **Importante:** nunca envie o arquivo `.env` para o GitHub.

---

## 📦 Instalação das dependências

Execute o comando abaixo no terminal:

```
pip install python-dotenv
pip install openai
```

---

## ▶️ Como executar

No terminal, dentro da pasta do projeto:

```
python chatbot.py
```

Exemplo de uso:

```
Você: Olá
Chatbot: Olá! Como posso ajudar?

Você: SAIR
Chatbot: Até mais!
```

---

## 🎯 Objetivo do projeto

Este projeto foi desenvolvido com o objetivo de:

* Praticar lógica de programação em Python
* Aprender a consumir APIs externas
* Trabalhar com variáveis de ambiente
* Criar um projeto simples, funcional e explicável para portfólio

---

## 🚀 Possíveis melhorias futuras

* Separar o código em múltiplos arquivos
* Persistir o histórico da conversa em arquivo
* Criar uma interface gráfica ou web
* Melhorar o tratamento de erros
* Permitir troca dinâmica do modelo utilizado

---

## 👤 Autor

Projeto desenvolvido por **Pedro**.
