# -*- coding: utf-8 -*-
import hashlib
import os
import datetime

def auditar_print_absoluto():
    print("[LOG] Inicializando barramento com variavel de ambiente...")
    
    nome_arquivo = "Captura de tela 2026-05-18 181110.png"
    user_profile = os.environ.get("USERPROFILE", "C:\\Users\\MARCO")
    
    caminhos_possiveis = [
        os.path.join(user_profile, r"OneDrive\Imagens\Capturas de Tela", nome_arquivo),
        os.path.join(user_profile, r"OneDrive\Pictures\Screenshots", nome_arquivo),
        os.path.join(user_profile, r"Pictures\Capturas de Tela", nome_arquivo),
        os.path.join(r"C:\XCortex_Zero", nome_arquivo)
    ]
    
    caminho_real = None
    for caminho in caminhos_possiveis:
        if os.path.exists(caminho):
            caminho_real = caminho
            break
            
    if not caminho_real:
        print(f"[ERRO] Arquivo '{nome_arquivo}' nao foi localizado.")
        print("Tente copiar o arquivo fisicamente para a pasta C:\\XCortex_Zero")
        return

    print(f"[SUCESSO] Alvo localizado em: {caminho_real}")

    sha256_hash = hashlib.sha256()
    with open(caminho_real, "rb") as f:
        for byte_block in iter(lambda: f.read(4096), b""):
            sha256_hash.update(byte_block)
            
    hash_resultado = sha256_hash.hexdigest().upper()
    print(f"\n[HASH SHA-256 SINAL VERDE]:\n{hash_resultado}")

if __name__ == '__main__':
    auditar_print_absoluto()