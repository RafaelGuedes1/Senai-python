import pandas as pd
import matplotlib.pyplot as plt


#criar os dados para o dataframe

dados = {
    "Nome": ["Arthur", "MAria", "Matheus", "Carlos", "Bruna"],
    "Idade": [28, 22, 35, 30, 20],
    "Cidade": ["Cotia", "Carapikuiba", "Cotia", "Osasco", "Cotia"]
}

df = pd.DataFrame(dados)
#exibir dataframe
print(df)


#salvar dataframe no formato csv
df.to_csv("pandas_dados.csv", index=False)
#visualizar o arquivo csv
df_csv = pd.read_csv("pandas_dados.csv")
print(df_csv)

df_filtrado = df[df["Idade"] > 25]
print(df_filtrado)

df_ordenado = df.sort_values(by="Idade", ascending=False)
print(df_ordenado)

#exibir estadisticas do dataframe

print(df.describe())

media_cidade = df.groupby("Cidade")["Idade"].mean()
print(media_cidade)

#df.plot(kind="pie", x="Nome", y="Idade", color="blue")
#plt.title("Idade das pessoas")
#plt.xlabel("Nome")
#plt.ylabel("Idade")
#plt.show()

df.boxplot(column="Idade", by="Cidade", grid=False)
plt.title("Distribuição de Idade por Cidade")
plt.xlabel("Cidade")
plt.ylabel("Idade")

plt.show()

