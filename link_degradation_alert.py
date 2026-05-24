# -*- coding: utf-8 -*-
# PROJETO SOH V2.1 & XCORTEX ZERO - MONITOR DE ESTABILIDADE DE LINK TÁTICO
# Fase 5: Homologação de Resiliência de Comunicação de Rádio Transmissor (Heartbeat)
import hashlib

def executar_monitor_link():
    print("[LOG] Inicializando Módulo de Detecção de Desvio de Firmeza de Link...")
    
    # Amostragem de latência de pacotes Heartbeat recebidos (em milissegundos inteiros)
    # Janela deslizante estática com 5 medições nominais consecutivas
    janela_latencias_ms = [13, 14, 15, 28, 45]  # Últimos pulsos indicam degradação rápida
    
    limite_tolerancia_media_ms = 20
    
    # Cálculo manual da média móvel por aritmética inteira rígida (Zero floats)
    soma_latencias = sum(janela_latencias_ms)
    media_latencia_calculada = soma_latencias // len(janela_latencias_ms)
    
    print(f"\n[RF MONITOR] Histórico da Janela Deslizante: {janela_latencias_ms} ms")
    print(f"[MÉTRICA] Média móvel de tempo de resposta: {media_latencia_calculada} ms")
    
    link_estavel = True
    # Verificação estrita contra o teto de tolerância do edital ROADS
    if media_latencia_calculada > limite_tolerancia_media_ms:
        link_estavel = False
        print("[ALERTA CRÍTICO RF] Degradação severa de link detectada!")
        print("[SISTEMA] Sinal abaixo do limiar de firmeza. Ativando Contingência Inercial Fria.")
    else:
        print("[SUCESSO] Canal de transmissão opera dentro da latência nominal estável.")
        
    hash_link = hashlib.sha256(f"{media_latencia_calculada}{link_estavel}".encode('utf-8')).hexdigest()
    
    print("\n--- [RELATÓRIO DE FIRMEZA DE SINAL DE RF - LINK DEGRADATION ALERT] ---")
    print(f"ESTADO ATUAL DO CANAL:   {'CONEXÃO NOMINAL' if link_estavel else 'DEGRADADO / EM ANOMALIA'}")
    print(f"DIRETRIZ DO TRANSMISSOR: {'MANTER EMISSÃO FHSS' if link_estavel else 'ABRIR RETORNO AUTÔNOMO SOH'}")
    print("---------------------------------------------------------------------")
    print(f"[HASH DE CONTROLE DE LINK]: {hash_link}")
    print("[SISTEMA] Status: ANÁLISE DE FLUXO CONCLUÍDA. Proteção de rádio ativa.\n")
    return True

if __name__ == '__main__':
    executar_monitor_link()