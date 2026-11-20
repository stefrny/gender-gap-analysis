
import requests

# Endereço da API da C&A
url = "https://www.cea.com.br/api/catalog_system/pub/products/search"

# Parâmetros da pesquisa
parametros = {
    "_from": 0,
    "_to": 20
}

# Cabeçalhos da requisição
cabecalhos = {
    "Accept": "application/json",
    "User-Agent": "ProjetoIntegradorAcademico/1.0"
}

try:
    resposta = requests.get(
        url,
        params=parametros,
        headers=cabecalhos,
        timeout=20
    )

    print("Status HTTP:", resposta.status_code)
    print("URL consultada:", resposta.url)
    print("Content-Type:", resposta.headers.get("Content-Type"))

    if resposta.status_code in (200, 206):

        dados = resposta.json()

        print("\nTipo de resposta:", type(dados).__name__)

        if isinstance(dados, list):

            print("Quantidade de produtos:", len(dados))

            for produto in dados:

                print("\n-----------------------------")
                print("Nome:", produto.get("productName"))
                print("Marca:", produto.get("brand"))
                print("Categorias:", produto.get("categories"))
                print("Gênero:", produto.get("Gênero"))

                itens = produto.get("items", [])

                if itens:
                    item = itens[0]

                    print("\nPrimeira variação:")
                    print("Nome:", item.get("name"))
                    print("SKU:", item.get("itemId"))

                    vendedores = item.get("sellers", [])

                    if vendedores:
                        oferta = vendedores[0].get(
                            "commertialOffer", {}
                        )

                        print("Preço atual:", oferta.get("Price"))
                        print("Preço original:", oferta.get("ListPrice"))

        else:
            print("A resposta não possui o formato esperado.")

    else:
        print("\nNão foi possível acessar o catálogo.")
        print("Resposta:", resposta.text[:500])

except requests.exceptions.Timeout:
    print("A requisição demorou demais para responder.")

except requests.exceptions.RequestException as erro:
    print("Erro na requisição:", erro)

except ValueError:
    print("O servidor não retornou um JSON válido.")
