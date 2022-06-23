import pandas as pd

dfClientes = pd.read_excel('analise_final/base_dados.xlsx',sheet_name= 'Cliente')
dfVendas = pd.read_excel('analise_final/base_dados.xlsx', sheet_name= 'Venda')
dfVendedores = pd.read_excel('analise_final/base_dados.xlsx', sheet_name= 'vendedor')

dfClientes.sample(10)
dfVendas.sample(10)
dfVendedores.sample(10)
print(dfClientes,'\n', dfVendas,'\n', dfVendedores)
