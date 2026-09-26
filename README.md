# ⚡ Calculadora de Consumo de Energia

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![Energia](https://img.shields.io/badge/Consumo_Elétrico-FFC107?style=for-the-badge&logo=lightning&logoColor=black)
![GitHub](https://img.shields.io/badge/github-%23121011.svg?style=for-the-badge&logo=github&logoColor=white)

## 🎯 Objetivo do Projeto
O **Calculadora de Consumo de Energia** é um sistema simples desenvolvido em terminal para calcular o consumo mensal de energia elétrica de aparelhos domésticos. Ele também estima o custo financeiro na conta de luz, ajudando no controle e planejamento de gastos! 💡💸

## 💻 Linguagem Utilizada
- **Python** 🐍

## 🧮 Fórmula Utilizada
O cálculo do consumo mensal (em kWh) é feito utilizando a seguinte fórmula padrão:

```python
consumoMensal = (potencia * horasDia * 30) / 1000
```
- `potencia`: Potência do aparelho em Watts (W).
- `horasDia`: Tempo médio de uso diário em horas.
- `30`: Quantidade média de dias em um mês.
- `1000`: Fator de conversão de Watts para Kilowatts (kW).

## 🚀 Como Executar o Programa

1. Certifique-se de ter o **Python** instalado em sua máquina.
2. Baixe os arquivos do projeto para uma pasta local.
3. Abra o terminal (ou prompt de comando).
4. Navegue até a pasta onde o arquivo se encontra e execute o seguinte comando:
   ```bash
   python calculadora_energia.py
   ```
5. Siga as instruções na tela e descubra o consumo dos seus aparelhos! 📊
