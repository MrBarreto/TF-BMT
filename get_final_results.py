import pandas as pd
from scipy.stats import mode

def read_csv_files(csv_files):
    dfs = [pd.read_csv(file) for file in csv_files]
    combined_df = pd.concat(dfs, axis=1)
    return combined_df

def calculate_mode(df):
    response_columns = [col for col in df.columns if 'response' in col]
    df['final_vote'] = df[response_columns].mode(axis=1)[0]
    return df

# Lista de arquivos CSV
csv_files = ['result1.csv', 'result2.csv', 'result3.csv']

# Lê os arquivos CSV e combina em um DataFrame
combined_df = read_csv_files(csv_files)

# Calcula a moda das respostas
final_df = calculate_mode(combined_df)

# Salva o DataFrame final em um arquivo CSV
final_df.to_csv('final_classified_tweets.csv', index=False)

print(final_df)