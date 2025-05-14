# Gráficos do 300

Este projeto gera visuais de acompanhamento das “300 horas” de estudo usando Python e uma planilha Excel.

## Preparar o ambiente

1. Clone o repositório:

   ```bash
   git clone https://github.com/moonshinerd/graficos-trezentos.git
   cd graficos-trezentos
   ```

2. Crie e ative um ambiente virtual:

   ```bash
   python -m venv .venv
   # Windows
   .venv\Scripts\activate
   # macOS/Linux
   source .venv/bin/activate
   ```
3. Instale dependências:

   ```bash
   pip install -r requirements.txt
   ```

## Configurar a planilha

* Use `trezentosteste999.xlsx` (ou copie/rename outra planilha e ajuste o nome nos scripts).
* Ela deve ter **duas colunas**:

  * **Grupo**: nome ou identificador de cada time ou célula de estudo.
  * **Média de Horas**: valor decimal (por exemplo, `1.5` = 1 h 30 min).

## Escolher o estilo de gráfico

Há duas opções de layout, cada uma em sua própria pasta:

* **gerador\_bob\_esponja/**
* **gerador\_mente\_superior/**

Abra aquela cujo visual preferir e siga para os ajustes.

## Ajustes principais

Em cada pasta você só precisará editar três arquivos:

### 1. Planilha de dados

* Substitua ou confirme o nome do arquivo Excel em cada script para apontar para `trezentosteste999.xlsx`.

### 2. `gerando_grafico_base.py`

* Ajuste as variáveis no topo do arquivo:

  ```python
  dias_totais = 300    # total de dias do ciclo
  dia_atual   = 45     # dia corrente (de 1 a 300)
  ```
* Rode:

  ```bash
  python gerando_grafico_base.py
  ```
* Resultado: `grafico_base.png` (em `images/`).

### 3. `imagem_final_gerador.py`

* Personalize os textos (título, legendas, rodapé) e sua posição para alinhar visualmente.
* Rode:

  ```bash
  python imagem_final_gerador.py
  ```
* Resultado: `images/imagem_final.png`.

## Personalização de cores e ícones

* Dentro de `assets/` (ou módulo `utils`), estão paletas e ícones.
* Troque cores ou imagens conforme seu tema, explorando esses arquivos.

## Quando há excesso de horas

Se algum valor de “Média de Horas” passar do limite:

1. No script de geração, localize a variável de limite (por exemplo, `horas_maximas = 8`).
2. Aumente esse limite ou comente a checagem.
3. Ajuste os textos no gerador final para comportar legendas maiores.
