import json

def converter_txt_para_json(n_arquivo_txt, n_arquivo_json):
    palavras = []
    try:
        with open(n_arquivo_txt, 'r', encoding='utf-8') as arquivo_txt:
            for linha in arquivo_txt:
                palavra = linha.strip()
                if palavra:
                    palavras.append(palavra)

        with open(n_arquivo_json, 'w', encoding='utf-8') as arquivo_json:
            json.dump(palavras, arquivo_json, ensure_ascii=False, indent=4)
        
        print(f"Sucesso! O arquivo '{n_arquivo_json}' foi criado com {len(palavras)} palavras.")

    except FileNotFoundError:
        print(f"Erro: O arquivo '{n_arquivo_txt}' não foi encontrado.")
    except Exception as e:
        print(f"Ocorreu um erro: {e}")

entrada = 'palavras.txt'
saida = 'palavras_convertidas.json'


converter_txt_para_json(entrada, saida)
