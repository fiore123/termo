import json

def converter_txt_para_json(nome_arquivo_txt, nome_arquivo_json):
    palavras = []
    try:
        with open(nome_arquivo_txt, 'r', encoding='utf-8') as arquivo_txt:
            for linha in arquivo_txt:
                palavra = linha.strip()
                if palavra:
                    palavras.append(palavra)

        with open(nome_arquivo_json, 'w', encoding='utf-8') as arquivo_json:
            json.dump(palavras, arquivo_json, ensure_ascii=False, indent=4)
        
        print(f"Sucesso! O arquivo '{nome_arquivo_json}' foi criado com {len(palavras)} palavras.")

    except FileNotFoundError:
        print(f"Erro: O arquivo '{nome_arquivo_txt}' não foi encontrado.")
    except Exception as e:
        print(f"Ocorreu um erro: {e}")

arquivo_de_entrada = 'palavras.txt'
arquivo_de_saida = 'palavras_para_o_jogo.json'

converter_txt_para_json(arquivo_de_entrada, arquivo_de_saida)