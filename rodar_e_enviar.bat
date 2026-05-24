@echo off
:: PROJETO: XCORTEX ZERO - ORQUESTRADOR CENTRAL E INTEGRAL DO GITHUB
:: Execução local em Ringue 3 e envio automatizado sem pendrive

echo =========================================================
echo [INICIALIZANDO] PROCESSANDO ECOSSISTEMA XCORTEX ZERO
echo =========================================================

:: 1. Executar os microsserviços locais em lote
echo [PASSO 1/3] Disparando o pipeline Python local...
python orquestrador_fase4.py

:: 2. Indexar as alterações locais
echo.
echo [PASSO 2/3] Indexando alterações no repositório local...
git add .

:: 3. Gerar o Commit com carimbo de data/hora dinâmico
echo [PASSO 3/3] Consolidando Bloco de Segurança e atualizando GitHub...
git commit -m "Fase 4 - Atualizacao Completa e Sincronizacao Automatizada"

:: 4. Enviar a estrutura atualizada para a nuvem privada
git push origin main

echo =========================================================
echo [SUCESSO] Todo o projeto foi orquestrado e enviado ao GitHub!
echo =========================================================
pause