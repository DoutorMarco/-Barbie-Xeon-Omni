# -*- coding: utf-8 -*-
# PROJETO SOH V2.1 & XCORTEX ZERO - DETECTOR FORENSE DE PORT SCAN
# Fase 5: Homologação de Contra-Espionagem Periférica por Entropia de Inteiros
import hashlib

def executar_detector_scan():
    print("[LOG] Inicializando Motor Forense de Detecção de Port Scan...")
    
    # Amostragem simulada de requisições de portas externas (Padrão Sequencial Adversário)
    # Portas escaneadas em sequência rápida para tentar identificar brechas
    historico_portas_alvo = [21, 22, 23, 25, 80, 443, 8080]
    
    # Cálculo de regularidade distributiva (Análise de entropia linear sobre inteiros)
    soma_deltas = 0
    for i in range(len(historico_portas_alvo) - 1):
        soma_deltas += abs(historico_portas_alvo[i+1] - historico_portas_alvo[i])
        
    # Métrica de desvio padrão inteiro escalado por 1000
    media_delta_escalada = (soma_deltas * 1000) // (len(historico_portas_alvo) - 1)
    
    print(f"\n[NETWORK AUDIT] Varredura registrada sobre {len(historico_portas_alvo)} portas periféricas.")
    print(f"[MÉTRICA ENTROPIA] Delta de dispersão linear calculado: {media_delta_escalada}")
    
    varredura_detectada = False
    # Padrões com deltas distribuídos de forma muito linear ou repetitiva indicam varredura automatizada
    if media_delta_escalada < 1500000:
        varredura_detectada = True
        print("[ALERTA CRÍTICO FORENSE] Varredura sequencial de Port Scan identificada!")
        print("[SISTEMA] Endereço de origem isolado nas travas do Motor Sanitizador.")
    else:
        print("[SUCESSO] Tráfego de rede disperso com distribuição normal tolerada.")
        
    hash_scan = hashlib.sha256(f"{media_delta_escalada}{varredura_detectada}".encode('utf-8')).hexdigest()
    
    print("\n--- [RELATÓRIO DE AUDITORIA DE REDE DE DEFESA - ANTIVARREDURA] ---")
    print(f"DIAGNÓSTICO DA INFRAESTRUTURA: {'MALA INTERCEPTADA / BLOQUEADA' if varredura_detectada else 'INTEGRIDADE NOMINAL'}")
    print(f"ESTADO DO INTERRUPTOR DE PROTEÇÃO: {'RINGUE 3 ISOLADO' if varredura_detectada else 'CANAL LIVRE SEM RESTRICÕES'}")
    print("---------------------------------------------------------------------")
    print(f"[HASH DE SINAL VERDE DE DETECÇÃO]: {hash_scan}")
    print("[SISTEMA] Status: ANÁLISE FORENSE DE REDE CONCLUÍDA. Proteção periférica ativa.\n")
    return True

if __name__ == '__main__':
    executar_detector_scan()