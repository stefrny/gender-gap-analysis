import pandas as pd

arquivo_bruto = r"C:\Users\emanu\OneDrive\Área de Trabalho\projetos-senac\gender-gap-analysis\dados\raw\RAIS_VINC_PUB_SP.COMT"
arquivo_saida = r"C:\Users\emanu\OneDrive\Área de Trabalho\projetos-senac\gender-gap-analysis\dados\processed\rais_sp_limpo.csv"

# Seleciona apenas as colunas úteis para a análise salarial
colunas = [
    "Sexo - Código",
    "Vl Rem Média Nom",
    "CBO 2002 Ocupação - Código",
    "Qtd Hora Contr",
    "Escolaridade Após 2005 - Código",
    "Ind Vínculo Ativo 31/12 - Código",
]

print("Iniciando leitura e limpeza da RAIS (isso leva cerca de 30 a 60 segundos)...")

primeiro_bloco = True
total_linhas_salvas = 0

# Lê de 500 mil em 500 mil linhas usando sep="," para não estourar a memória RAM
for i, bloco in enumerate(
    pd.read_csv(
        arquivo_bruto, sep=",", encoding="latin1", usecols=colunas, chunksize=500_000
    ),
    start=1,
):
    # 1. Mantém apenas vínculos ativos em 31/12 (padrão metodológico para comparar salários)
    bloco = bloco[
        pd.to_numeric(bloco["Ind Vínculo Ativo 31/12 - Código"], errors="coerce") == 1
    ]

    # 2. Padroniza a coluna de gênero (1 = Masculino, 2 = Feminino)
    sexo_num = pd.to_numeric(bloco["Sexo - Código"], errors="coerce")
    bloco = bloco[sexo_num.isin([1, 2])].copy()
    bloco["genero"] = sexo_num.map({1: "Masculino", 2: "Feminino"})

    # 3. Converte o salário para número decimal válido (troca vírgula por ponto, se houver)
    salario_str = (
        bloco["Vl Rem Média Nom"].astype(str).str.replace(",", ".", regex=False)
    )
    bloco["salario_mensal"] = pd.to_numeric(salario_str, errors="coerce")

    # 4. Remove salários zerados ou inválidos
    bloco = bloco[bloco["salario_mensal"] > 0]

    # 5. Renomeia e mantém apenas as colunas finais organizadas
    tabela_final = bloco[
        [
            "genero",
            "salario_mensal",
            "CBO 2002 Ocupação - Código",
            "Qtd Hora Contr",
            "Escolaridade Após 2005 - Código",
        ]
    ].rename(
        columns={
            "CBO 2002 Ocupação - Código": "cbo_ocupacao",
            "Qtd Hora Contr": "horas_semanais",
            "Escolaridade Após 2005 - Código": "escolaridade_cod",
        }
    )

    # Salva no arquivo CSV final
    tabela_final.to_csv(
        arquivo_saida, mode="w" if primeiro_bloco else "a", index=False, header=primeiro_bloco
    )
    primeiro_bloco = False
    total_linhas_salvas += len(tabela_final)
    print(f"Bloco {i} processado | Registros válidos acumulados: {total_linhas_salvas:,}")

print(f"\nConcluído! Arquivo '{arquivo_saida}' gerado com {total_linhas_salvas:,} registros.")