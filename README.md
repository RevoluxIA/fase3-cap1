# 🌱 Sistema de Irrigação Automatizado

## 📝 Descrição do Projeto
Este projeto, desenvolvido para a **Fase 3 - Colheita de Dados e Insights**, implementa um sistema de irrigação automatizado utilizando o microcontrolador ESP32. O sistema monitora condições do solo (umidade, pH, presença de nutrientes) e ativa uma bomba de irrigação quando necessário, otimizando o cultivo com base em parâmetros específicos. A simulação foi realizada na plataforma **Wokwi**.

### 🛠️ Componentes Utilizados
- **ESP32**: Microcontrolador principal.
- **DHT22**: Sensor de umidade e temperatura (GPIO 27).
- **LDR**: Sensor de luz simulando pH (GPIO 25).
- **Botões**: Simulam a presença de Fósforo (GPIO 14) e Potássio (GPIO 12).
- **Relé**: Controla a bomba de irrigação (GPIO 26).
- **LED**: Indicador visual do estado da irrigação (GPIO 19).

### ⚙️ Regras de Negócio
- Monitora continuamente:
  - Umidade do solo (DHT22).
  - pH do solo (LDR, mapeado de 0 a 14).
  - Presença de Fósforo e Potássio (botões).
- **Ativa a bomba (relé)** se:
  - Umidade < 30%.
  - pH entre 6 e 8.
- **Desativa a bomba** se as condições não forem atendidas.
- **LED** acende quando a bomba está ligada.
- Indica no monitor serial se Fósforo ou Potássio estão sendo "adicionados" (botões pressionados).

---

## 💾 Simulação CRUD dos Dados de Sensores

Além da simulação física, este projeto inclui um script Python que simula o armazenamento e manipulação dos dados de sensores em um banco de dados SQL (SQLite), utilizando os dados do arquivo `data/data.json`.

### 🔄 Funcionalidades CRUD

- **Create (Inserção):** Insere os dados lidos do arquivo JSON em uma tabela do banco de dados.
- **Read (Consulta):** Permite consultar todos os registros ou filtrar por parâmetros como umidade, pH, status da bomba, etc.
- **Update (Atualização):** Permite atualizar valores de registros existentes, como corrigir leituras ou alterar status.
- **Delete (Remoção):** Permite remover registros específicos do banco de dados.

### 🗂️ Justificativa da Estrutura

A estrutura dos dados segue o modelo relacional proposto no MER da Fase 2, onde cada leitura de sensores é armazenada como um registro independente, facilitando consultas, análises e integridade dos dados. O uso do SQLite foi escolhido por ser leve, fácil de integrar e suficiente para simulação e testes acadêmicos.

### ▶️ Como Executar a Simulação CRUD

1. 📦 Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```
2. 🖥️ Execute o script Python:
   ```bash
   python crud_simulation.py
   ```
3. 💡 Siga as instruções no terminal para realizar operações CRUD.

## 📁 Estrutura de Pastas
```
FASE3-CAP1/
├── data/
│   └── data.json                # Dados simulados dos sensores
├── docs/
│   ├── Capturar.PNG             # Imagem do circuito exportada do Wokwi
│   └── diagram.json             # Diagrama do circuito (Wokwi)
├── src/
│   ├── crud.py                  # Operações CRUD em Python
│   ├── db.py                    # Configuração do banco de dados
│   ├── main.cpp                 # (Opcional) Código C++ se houver integração física
│   ├── main.py                  # Script principal Python para simulação CRUD
│   ├── models.py                # Modelos de dados Python
│   └── utils.py                 # Funções utilitárias Python
├── README.markdown              # Documentação do projeto (este arquivo)
└── requirements.txt             # Dependências do Python
```

## 🖼️ Diagrama do Circuito
![Diagrama do Circuito](docs/capturar.png)

## 🚀 Instruções de Uso
1. Monte o circuito no Wokwi conforme o diagrama.
2. Carregue o código (`src/main.cpp`) no ESP32 via Wokwi.
3. Inicie a simulação.
4. Pressione os botões para simular a presença de Fósforo e Potássio.
5. Ajuste o LDR (se possível) para variar o pH.
6. Observe o monitor serial para os dados e o estado da bomba.
7. Para simulação CRUD, siga as instruções na seção correspondente.

## ℹ️ Observações
- O DHT22 pode não ser simulado corretamente no Wokwi, então a umidade e temperatura podem mostrar "Falha ao ler".
- O pH é simulado pelo LDR; valores reais dependerão da intensidade de luz.
- O projeto pode ser expandido para incluir sensores reais e ajustes na lógica de irrigação.
