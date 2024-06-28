
# Inserir as datas 
data_inicial= input("Insira a data inicial - Ex 01012024: ")
data_final = input("Insira a data final-  Ex 31012024:  ")

#Inserir os valores das Receitas
receitas_vivo = float(input(" Insira o valor da Vivo: "))
receitas_rioluz = float(input(" Insira o valor da  Rio Luz: "))
receitas_santander = float(input(" Insira o valor do Santander: "))
atualizacao_dep_judicial = float(input(" Insira o valor de Atualização de Déposito Judicial: "))
atualizacao_cred_tributario = float(input(" Insira o valor de Atualização de Crédito Tributário: "))
descontos_obtidos = float(input(" Insira o valor de  Descontos Obtidos: "))
aplicacao_financeira =  float(input(" Insira o valor de Aplicações Financeiras: "))




# VALORES CHEIOS PARA RESULTADO FINAL
VIVO_FINAL = (f'{receitas_vivo:.2f}')
RECEITA_FINAL_VIVO = str(VIVO_FINAL)

RIOLUZ_FINAL = (f'{receitas_rioluz:.2f}')
RECEITA_FINAL_RIOLUZ = str(RIOLUZ_FINAL)

SANTANDER_FINAL  = (f'{receitas_santander:.2f}')
RECEITA_FINAL_SANTANDER = str(SANTANDER_FINAL)

DEP_JUDICIAL_FINAL = (f'{atualizacao_dep_judicial:.2f}')
RECEITA_FINAL_DEP_JUDICIAL = str(DEP_JUDICIAL_FINAL)

CREDITO_TRIBUTARIO_FINAL = (f'{atualizacao_cred_tributario:.2f}')
RESULTADO_FINAL_CREDITO_TRIBUTARIO = str(CREDITO_TRIBUTARIO_FINAL)

DESCONTOS_OBTIDOS_FINAL = (f'{descontos_obtidos:.2f}')
RESULTADO_DESCONTOS_OBTIDOS_FINAL = str(DESCONTOS_OBTIDOS_FINAL)

APLICACAO_FINAL = (f'{aplicacao_financeira:.2f}')
RESULTADO_APLICACAO_FINAL = str(APLICACAO_FINAL)


#LÓGICA PARA CALCULAR OS VALORES 

#Calculo da vivo 
calculo_vivo = receitas_vivo*1.65/100
calculo_vivo2 = receitas_vivo*7.60/100

#Transformar em String
vivo_para_string = (f'{calculo_vivo:.2f}')
resultado_vivo = str(vivo_para_string)

vivo_para_string2 = (f'{calculo_vivo2:.2f}')
resultado_vivo2 = str(vivo_para_string2)



#Calculo da Rio Luz 

calculo_rioluz = receitas_rioluz*1.65/100
calculo_rioluz2 = receitas_rioluz*7.60/100

#Transformar em String
rioluz_para_string = (f'{calculo_rioluz:.2f}')
resultado_rioluz = str(rioluz_para_string)

rioluz_para_string2 = (f'{calculo_rioluz2:.2f}')
resultado_rioluz2 = str(rioluz_para_string2)


# # Calculo Santander
calculo_santander = receitas_santander*1.65/100
calculo_santander2 = receitas_santander*7.60/100

#Transformar em String

santander_para_string = (f'{calculo_santander:.2f}')
resultado_santander = str(santander_para_string)

santander_para_string2 = (f'{calculo_santander2:.2f}')
resultado_santander2 = str(santander_para_string2)


# Calculo Deposito Judicial
calculo_dep_judicial = atualizacao_dep_judicial*1.65/100
calculo_dep_judicial2 = atualizacao_dep_judicial*7.60/100

#Transformar em String

deposito_judicial_para_string = (f'{calculo_dep_judicial:.2f}')
resultado_deposito_judicial = str(deposito_judicial_para_string)

deposito_judicial_para_string2 = (f'{calculo_dep_judicial2:.2f}')
resultado_deposito_judicial2 = str(deposito_judicial_para_string2)


# # Calculo Atualização de Crédito
calculo_atua_credito = atualizacao_cred_tributario*1.65/100
calculo_atua_credito2 = atualizacao_cred_tributario*7.60/100

#Transformar em String

atulizacao_credito_tributario_para_string = (f'{calculo_atua_credito:.2f}')
resultado_atualizacao_credito_tributario = str(atulizacao_credito_tributario_para_string)

atulizacao_credito_tributario_para_string2 = (f'{calculo_atua_credito2:.2f}')
resultado_atualizacao_credito_tributario2 = str(atulizacao_credito_tributario_para_string2)


# #Calculo Descontos Obtidos
calculo_desconto_obtidos = descontos_obtidos*1.65/100
calculo_desconto_obtidos2 = descontos_obtidos*7.60/100

#Transformar em String

descontos_para_string = (f'{calculo_desconto_obtidos:.2f}')
resultado_descontos = str(descontos_para_string)

descontos_para_string2 = (f'{calculo_desconto_obtidos2:.2f}')
resultado_descontos2 = str(descontos_para_string2)


#Calculo de Aplicação Financeira
calculo_aplic_financeira = aplicacao_financeira*1.65/100
calculo_aplic_financeira2 = aplicacao_financeira*7.60/100

#Transformar em String

aplicacao_financeira_para_string = (f'{calculo_aplic_financeira:.2f}')
resultado_aplicacao_financeira = str(aplicacao_financeira_para_string)

aplicacao_financeira_para_string2 = (f'{calculo_aplic_financeira2:.2f}')
resultado_aplicacao_financeira2 = str(aplicacao_financeira_para_string2)



print(f'''


|0000|006|0|||{data_inicial}|{data_final}| EMPRESA MUNICIPAL DE URBANIZACAO RIOURBE|31066178000169|RJ|3304557||00|9|
|0001|0|
|0100|GABRIEL DOS SANTOS ROSA|11863581731|RJ118407/O-9||20211178|Rua Dom Marcos Barbosa|2|salas 203 e 204|Cidade Nova|2129769245||gabriel.rosa@rio.rj.gov.com|3304557|
|0110|1|1|2||
|0140||EMPRESA MUNICIPAL DE URBANIZACAO RIOURBE|31066178000169|RJ||3304557|||
|0500|{data_inicial}|04|A|8|4.3.3.11.01.01.01|Receitas Imobiliárias|||
|0500|{data_inicial}|04|A|8|4.3.3.12.01.01.01|Receitas Imobiliárias|||
|0500|{data_inicial}|04|A|8|4.4.3.11.01.01.02|Variações Monetárias de Empréstimos Concedidos|||
|0500|{data_inicial}|04|A|8|4.4.3.91.01.01.04|Atualização de Depósitos Judiciais|||
|0500|{data_inicial}|04|A|8|4.4.3.93.01.01.02|Atualizacao de creditos tributarios|||
|0500|{data_inicial}|04|A|8|4.4.4.01.01.01.01|Descontos Financeiros Obtidos|||
|0500|{data_inicial}|04|A|8|4.4.5.21.01.01.01|Remuneração de Aplicações Financeiras|||
|0500|{data_inicial}|04|A|8|4.3.3.11.01.03.01|Receita de Cessão de Direitos de Oper de Pagamentos|||
|0500|{data_inicial}|04|A|8|4.5.1.12.01.01.01|Repasses |||
|0500|{data_inicial}|04|A|8|4.4.3.91.01.01.01|Atualização de Contas a Receber|||
|0500|{data_inicial}|04|A|8|4.9.9.91.01.01.99|Outras Variações Patrimoniais Aumentativas Decorrentes de Fa|||
|0500|{data_inicial}|04|A|8|4.9.9.61.01.01.99|Outras idenizações|||
|0500|{data_inicial}|04|A|8|4.4.2.91.01.01.99|Outros Juros e Encargos de Mora|||
|0500|{data_inicial}|04|A|8|4.6.4.11.01.01.01|ganho desincorporação caução|||
|0990|20|
|A001|1|
|A990|2|
|C001|1|
|C990|2|
|D001|1|
|D990|2|
|F001|0|
|F010|31066178000169|
|F100|1|||{data_final}|{RECEITA_FINAL_VIVO.replace('.', ',')}|01|{RECEITA_FINAL_VIVO.replace('.', ',')}|1,65|{resultado_vivo.replace('.', ',')}|01|{RECEITA_FINAL_VIVO.replace('.', ',')}|7,6|{resultado_vivo2.replace('.', ',')}|||4.3.3.11.01.01.01|||
|F100|1|||{data_final}|{RECEITA_FINAL_RIOLUZ.replace('.', ',')}|01|{RECEITA_FINAL_RIOLUZ.replace('.', ',')}|1,65|{resultado_rioluz.replace('.', ',')}|01|{RECEITA_FINAL_RIOLUZ.replace('.', ',')}|7,6|{resultado_rioluz2.replace('.', ',')}|||4.3.3.12.01.01.01|||
|F100|1|||{data_final}|{RECEITA_FINAL_SANTANDER.replace('.', ',')}|01|{RECEITA_FINAL_SANTANDER.replace('.', ',')}|1,65|{resultado_santander.replace('.', ',')}|01|{RECEITA_FINAL_SANTANDER.replace('.', ',')}|7,6|{resultado_santander2.replace('.', ',')}|||4.3.3.11.01.03.01|||
|F100|1|||{data_final}|{RECEITA_FINAL_DEP_JUDICIAL.replace('.', ',')}|02|{RECEITA_FINAL_DEP_JUDICIAL.replace('.', ',')}|0,65|{resultado_deposito_judicial.replace('.', ',')}|02|{RECEITA_FINAL_DEP_JUDICIAL.replace('.', ',')}|4|{resultado_deposito_judicial2.replace('.', ',')}|||4.4.3.91.01.01.04|||
|F100|1|||{data_final}|0,00|02|0,00|0,65|0,00|02|0,00|4|0,00|||4.4.3.91.01.01.01|||
|F100|1|||{data_final}|{RESULTADO_APLICACAO_FINAL.replace('.', ',')}|02|{RESULTADO_APLICACAO_FINAL.replace('.', ',')}|0,65|{resultado_aplicacao_financeira.replace('.',',')}|02|{RESULTADO_APLICACAO_FINAL.replace('.', ',')}|4|{resultado_aplicacao_financeira2.replace('.',',')}|||4.4.5.21.01.01.01|||
|F100|2|||{data_final}|0|07||||07||||||4.5.1.12.01.01.01|||
|F100|1|||{data_final}|{RESULTADO_DESCONTOS_OBTIDOS_FINAL.replace('.', ',')}|02|{RESULTADO_DESCONTOS_OBTIDOS_FINAL.replace('.', ',')}|0,65|4{resultado_descontos.replace('.', ',')}|02|{RESULTADO_DESCONTOS_OBTIDOS_FINAL.replace('.', ',')}|4|{resultado_descontos2.replace('.', ',')}|||4.4.4.01.01.01.01|||
|F100|1|||{data_final}|{RESULTADO_FINAL_CREDITO_TRIBUTARIO.replace('.', ',')}|02|{RESULTADO_FINAL_CREDITO_TRIBUTARIO.replace('.', ',')}|0,65|{resultado_atualizacao_credito_tributario.replace('.', ',')}|02|{RESULTADO_FINAL_CREDITO_TRIBUTARIO.replace('.', ',')}|4|{resultado_atualizacao_credito_tributario2.replace('.', ',')}|||4.4.3.93.01.01.02|||
|F990|11|
|I001|1|
|I990|2|
|M001|0|
|M200|6264,71|0|0|6264,71|0|0|6264,71|0|0|0|0|6264,71|
|M205|08|691201|6264,71|
|M210|01|368047,38|368047,38|0|0|368047,38|1,65|0||6072,78|0|0|0|0|6072,78|
|M210|02|29527,53|29527,53|0|0|29527,53|0,65|0||191,93|0|0|0|0|191,93|
|M400|07|2707975,49|4.5.1.12.01.01.01||
|M410|901|2707975,49|4.5.1.12.01.01.01||
|M600|29152,7|0|0|29152,7|0|0|29152,7|0|0|0|0|29152,7|
|M605|08|585601|29152,7|
|M610|01|368047,38|368047,38|0|0|368047,38|7,6|0||27971,6|0|0|0|0|27971,6|
|M610|02|29527,53|29527,53|0|0|29527,53|4|0||1181,1|0|0|0|0|1181,1|
|M800|07|2707975,49|4.5.1.12.01.01.01||
|M810|901|2707975,49|4.5.1.12.01.01.01||
|M990|14|
|P001|1|
|P990|2|
|1001|1|
|1990|2|
|9001|0|
|9900|0000|1|
|9900|0001|1|
|9900|0100|1|
|9900|0110|1|
|9900|0140|1|
|9900|0500|14|
|9900|0990|1|
|9900|1001|1|
|9900|1990|1|
|9900|9001|1|
|9900|9990|1|
|9900|9999|1|
|9900|A001|1|
|9900|A990|1|
|9900|C001|1|
|9900|C990|1|
|9900|D001|1|
|9900|D990|1|
|9900|F001|1|
|9900|F010|1|
|9900|F100|8|
|9900|F990|1|
|9900|I001|1|
|9900|I990|1|
|9900|M001|1|
|9900|M200|1|
|9900|M205|1|
|9900|M210|2|
|9900|M400|1|
|9900|M410|1|
|9900|M600|1|
|9900|M605|1|
|9900|M610|2|
|9900|M800|1|
|9900|M810|1|
|9900|M990|1|
|9900|P001|1|
|9900|P990|1|
|9900|9900|39|
|9990|42|
|9999|99|


''')