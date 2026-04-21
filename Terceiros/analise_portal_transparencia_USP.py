# Direitor autorais inteiramente do autor do post https://www.reddit.com/r/USP/comments/1sqznx9/como_ganhar_10x_mais_do_que_o_seu_colega_na_mesma/

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import textwrap

# carregar base
df_cons = pd.read_csv('tabela - salários.xlsx - Servidor-Consolidado.csv')
df_p2 = pd.read_csv('tabela - salários.xlsx - Planilha2.csv')
df_p2.columns = ['Unid/Orgão', 'Escola', 'Jornada', 'Categoria', 'Data Ingresso/Aposentadoria', 'Classe', 'Ref/MS', 'Função', 'Função de Estrutura', 'Data designação', 'Tempo USP', 'Parcelas Eventuais', 'Salário Mensal', 'Líquido', 'Data de processamento', 'Column1']
df_all = pd.concat([df_cons, df_p2])

# Filtrar funcionarios inativos ou com valores abaixo do salário minimo >= 1621
df_filtered = df_all[df_all['Salário Mensal'] >= 1621].copy()

# excluir Superior and Docente
classes_superiores_docentes = ['Docente', 'Superior 1', 'Superior 2', 'Superior 3', 'Superior 4', 'Superior 5']
df_filtered = df_filtered[~df_filtered['Classe'].isin(classes_superiores_docentes)]
df_filtered = df_filtered.dropna(subset=['Classe', 'Data Ingresso/Aposentadoria', 'Salário Mensal'])

# separar grupo Básico vs Técnico
df_filtered['Nível'] = np.where(df_filtered['Classe'].str.contains('Técnic|Tec', case=False, na=False), 'Técnico', 'Básico')

# confirmação de selecionados
included_classes = df_filtered['Classe'].unique()
classes_str = ", ".join(sorted([str(c) for c in included_classes]))
wrapped_classes = textwrap.fill(f"Amostra Incluída: {classes_str}", width=110)

# separar grupos antes e pos reforma (Cutoff: May 10, 2011)
df_filtered['Data Ingresso'] = pd.to_datetime(df_filtered['Data Ingresso/Aposentadoria'], errors='coerce')
df_filtered = df_filtered.dropna(subset=['Data Ingresso'])
cutoff_date = pd.to_datetime('2011-05-10')
df_filtered['Grupo_Tempo'] = np.where(
df_filtered['Data Ingresso'] < cutoff_date,
'Antes (Até Mai/2011)',
'Após (A partir de Mai/2011)'
)

# criar grupos para plotagem
df_filtered['Grupo_Plot'] = df_filtered['Grupo_Tempo'] + ' - Nível ' + df_filtered['Nível']

# Cálculo de médias e medianas básico vs tecnico
stats = df_filtered.groupby('Grupo_Tempo')['Salário Mensal'].agg(['mean', 'median', 'count']).reset_index()

# Plot
plt.figure(figsize=(16, 8))
sns.set_style("whitegrid")

# cores
palette = {
'Antes (Até Mai/2011) - Nível Técnico': '#154360', # Azul Escuro
'Antes (Até Mai/2011) - Nível Básico': '#5dade2', # Azul Claro
'Após (A partir de Mai/2011) - Nível Técnico': '#145a32', # Verde Escuro
'Após (A partir de Mai/2011) - Nível Básico': '#58d68d' # Verde Claro
}
ax = sns.histplot(
data=df_filtered,
x='Salário Mensal',
hue='Grupo_Plot',
kde=True,
bins=60,
palette=palette,
alpha=0.5,
edgecolor='white',
hue_order=[
'Antes (Até Mai/2011) - Nível Técnico',
'Antes (Até Mai/2011) - Nível Básico',
'Após (A partir de Mai/2011) - Nível Técnico',
'Após (A partir de Mai/2011) - Nível Básico'
]
)

# Adicionar linhas
grupo_antes = 'Antes (Até Mai/2011)'
grupo_apos = 'Após (A partir de Mai/2011)'
mean_antes = stats[stats['Grupo_Tempo'] == grupo_antes]['mean'].values[0]
median_antes = stats[stats['Grupo_Tempo'] == grupo_antes]['median'].values[0]
mean_apos = stats[stats['Grupo_Tempo'] == grupo_apos]['mean'].values[0]
median_apos = stats[stats['Grupo_Tempo'] == grupo_apos]['median'].values[0]
plt.axvline(mean_antes, color='#154360', linestyle='--', linewidth=2.5, label=f'Média - Antes (R$ {mean_antes:,.2f})'.replace(',', 'X').replace('.', ',').replace('X', '.'))
plt.axvline(median_antes, color='#154360', linestyle='-', linewidth=2.5, label=f'Mediana - Antes (R$ {median_antes:,.2f})'.replace(',', 'X').replace('.', ',').replace('X', '.'))
plt.axvline(mean_apos, color='#145a32', linestyle='--', linewidth=2.5, label=f'Média - Após (R$ {mean_apos:,.2f})'.replace(',', 'X').replace('.', ',').replace('X', '.'))
plt.axvline(median_apos, color='#145a32', linestyle='-', linewidth=2.5, label=f'Mediana - Após (R$ {median_apos:,.2f})'.replace(',', 'X').replace('.', ',').replace('X', '.'))
plt.title('Distribuição de Remunerações: Efeito do Tempo, Reformulação de Carreira (2011) e Nível\n' +
wrapped_classes, fontsize=14, fontweight='bold', pad=15)
plt.xlabel('Salário Mensal Bruto (R$)', fontsize=12)
plt.ylabel('Frequência (Nº de Servidores)', fontsize=12)

# legendas e ajustes de layout
sns.move_legend(ax, "upper right", bbox_to_anchor=(1, 1), title='Legenda (Cor = Período | Tom = Nível)', frameon=True)
plt.xlim(left=1600)
plt.tight_layout()
plt.savefig('distribuicao_niveis.png', dpi=300)

print(stats)
