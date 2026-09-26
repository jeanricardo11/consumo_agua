""""""""""""""""""""""""""""""""""""""""""""""""
"        Eco Aqua - Educação Ambiental         "
""""""""""""""""""""""""""""""""""""""""""""""""

# Solicita o tipo de imóvel ao usuário
tipo_imovel = input("Digite o tipo de imóvel (comercial, casa, apartamento): ")
try:
    # Solicita o consumo mensal de água e converte a entrada para número decimal (float)
    consumo = float(input("Digite o consumo mensal de água em m³: "))

    # Regra 1: Imóveis comerciais
    if tipo_imovel == "comercial":
        print("Tarifa comercial aplicada – consulte o plano corporativo.")
    
    # Regra 2: Apartamentos com consumo inferior a 10 m³
    elif tipo_imovel == "apartamento" and consumo < 10:
        print("Consumo econômico – excelente controle de água!")
    
    # Regra 3: Apartamentos ou casas com consumo de até 25 m³
    elif (tipo_imovel == "apartamento" or tipo_imovel == "casa") and consumo <= 25:
        print("Consumo moderado – dentro do padrão residencial.")
    
    # Regra 4: Qualquer outro caso (como casa/apartamento acima de 25 m³ ou tipos não listados com alto consumo)
    else:
        print("Consumo excessivo – adote medidas de economia e verifique vazamentos.")

finally:    
        print("Cuide da Agua. Agua é Vida!")
