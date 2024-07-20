# Análise de Tweets sobre Apostas Esportivas

## Descrição do Projeto

Este projeto analisa o discurso em torno das apostas esportivas no Twitter durante os dias que antecederam a final da Copa do Mundo de 2022. Utilizamos diferentes modelos de linguagem natural (LLMs) e abordagens distintas para identificar e quantificar as discussões relacionadas às apostas esportivas, distinguindo entre fãs de esporte e fãs de apostas.

## Estrutura do Projeto

O projeto está organizado nas seguintes pastas e arquivos:

### Pastas

- `clean_answers/`: Contém os dados de respostas limpos e processados.
- `raw_answers/`: Contém os dados de respostas brutos obtidos diretamente dos LLMs.
- `tweets/`: Contém os tweets coletados para análise e os tweets classificados manualmente.

### Arquivos

- `process_answers.ipynb`: Notebook Jupyter para limpeza dos dados e geração das estatísticas. Este arquivo inclui as etapas de pré-processamento e a criação de métricas de desempenho como precisão, recall e F1-Score.
- `tf.ipynb`: Notebook Jupyter para geração das respostas dos LLMs. Este arquivo contém o código utilizado para obter as respostas dos modelos informados e não informados sobre apostas esportivas.

## Requisitos

- Python 3.8 ou superior
- Jupyter Notebook
- Bibliotecas Python:
  - pandas
  - numpy
  - sklearn
  - transformers
  - llama_cpp
  - Ambiente configurado com cuda e rapidsAI
  

## Instruções de Uso

1. **Coleta e Armazenamento de Tweets**: Certifique-se de que a pasta `tweets/` contém os dados de tweets coletados para análise.

2. **Geração das Respostas dos LLMs**:
   - Abra o arquivo `tf.ipynb` no Jupyter Notebook.
   - Execute todas as células para gerar as respostas dos modelos de linguagem natural.
   - As respostas geradas serão armazenadas na pasta `raw_answers/`.

3. **Processamento e Análise das Respostas**:
   - Abra o arquivo `process_answers.ipynb` no Jupyter Notebook.
   - Execute todas as células para limpar os dados e gerar as estatísticas.
   - Os dados processados e as métricas de desempenho serão armazenados na pasta `clean_answers/`.


## Modelos Utilizados

Neste projeto, utilizamos diferentes modelos de linguagem natural para analisar os tweets relacionados às apostas esportivas. Os modelos utilizados foram:

1. **GPT 4(Generative Pre-trained Transformer)**
2. **LLama2**
3. **LLama3**

Os modelos foram empregados em duas abordagens distintas:

- **Abordagem Informada**: Nesta abordagem, fornecemos ao modelo uma explicação prévia sobre o conceito de apostas esportivas antes de perguntar sobre o conteúdo dos tweets.
- **Abordagem Não Informada**: Nesta abordagem, perguntamos diretamente sobre apostas esportivas sem fornecer explicações prévias.

Os modelos foram avaliados com base em métricas de desempenho como precisão, recall e F1-Score, para determinar sua eficácia na identificação de tweets sobre apostas esportivas.


## Licença

Este projeto está licenciado sob os termos da MIT License.
