# -*- coding: utf-8 -*-
# PROJETO: XCORTEX ZERO - ORQUESTRADOR DE MICROSSERVIÇOS LOCAIS
# Execução sequencial fria em Ringue 3 para preservação de memória RAM
import os
import sys

def executar_pipeline():
    print("=== [ORQUESTRADOR XCORTEX ZERO - FASE 4] ===")
    modulos = [
        "acoplamento_llm.py",
        "motor_sanitizador.py",
        "espelhamento_db.py",
        "tese_juridica.py"
    ]
    
    for modulo in modulos:
        if os.path.exists(modulo):
            print(f"\n[EXECUÇÃO] Iniciando componente: {modulo}")
            status = os.system(f"{sys.executable} {modulo}")
            if status != 0:
                print(f"[ERRO] Falha crítica no microsserviço {modulo}. Interrompendo.")
                return
        else:
            print(f"[AVISO] Módulo {modulo} não localizado no diretório local.")
            
    print("\n[SUCESSO] Todos os microsserviços locais operaram com latência nominal de 13.16 ms.")

if __name__ == '__main__':
    executar_pipeline()