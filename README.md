# CP2 - RPA Utilizando Python: Automação de Compras e Câmbio Logístico

Automação em Python desenvolvida para resolver uma dor operacional no setor de Compras e Logística: a dependência de consultas manuais de cotações cambiais para precificação de insumos importados, conferência de custos e aprovações financeiras.

---

## 👥 Integrantes do Grupo

* **Felipe Hideki** - RM98323
* **Guilherme Milheiro** - RM550295
* **Jhonatan Curci** - RM94188
* **Enzo Vasconcelos** - RM550702
* **Ricardo Queiroz** - RM94241

---

## 📌 Problema Resolvido

No dia a dia operacional de logística e compras, a cotação de insumos e matérias-primas varia conforme moedas internacionais (USD e EUR). O processo manual de consultar cotações em sites externos, recalcular valores linha por linha em planilhas e identificar pedidos que demandam aprovação gerencial gera atrasos operacionais e risco de inconsistências.

Esta solução automatiza:
1. Consulta em tempo real das taxas de compra de Dólar (USD) e Euro (EUR) via API RESTful pública.
2. Cruzamento automático das moedas com a fila de pedidos pendentes de aquisição.
3. Conversão de custos unitários e totais para Real (BRL).
4. Aplicação de regra de conformidade financeira (marcação de pedidos a partir de R$ 30.000,00 que necessitam de aprovação da diretoria).
5. Exportação dos dados consolidados para planilha Excel (.xlsx) com auditoria via logs.

---

## 🛠️ Tecnologias Utilizadas

* **Python 3.11**
* **Requests:** Consumo de API RESTful (AwesomeAPI)
* **Pandas:** Estruturação e manipulação de dados em DataFrames
* **Openpyxl:** Manipulação e exportação para arquivos Excel
* **Logging:** Rastreamento estruturado das etapas de execução

---

## 📂 Estrutura do Projeto

- **automation.py:** Código-fonte principal da automação
- **requirements.txt:** Dependências do projeto
- **README.md:** Documentação do projeto
- **data/relatorio_compras_atualizado.xlsx:** Arquivo gerado pela execução

---

## 🚀 Como Executar

1. Clone o repositório:
   git clone https://github.com/GuiMilheiro/rpa-compras-logistica.git

2. Acesse a pasta:
   cd rpa-compras-logistica

3. Instale as dependências:
   pip install -r requirements.txt

4. Execute a automação:
   python automation.py

O relatório processado será salvo automaticamente em data/relatorio_compras_atualizado.xlsx.

---

## 🎥 Vídeo de Demonstração

* **Link da Apresentação:** [Inserir link do YouTube (Não Listado) ou Drive/OneDrive]
