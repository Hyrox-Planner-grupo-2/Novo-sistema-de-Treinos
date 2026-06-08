# 🏃 HYROX Planner - Sistema de Treinos

> Um sistema inteligente de planejamento e acompanhamento de treinos para a modalidade HYROX, desenvolvido como projeto de fundamentos da programação.

## 📋 Sobre o Projeto

**HYROX Planner** é uma aplicação em Python que oferece um sistema completo de gerenciamento de treinos especializados para HYROX (corrida híbrida com 8 estações funcionais). O sistema foi desenvolvido pelo **Grupo 2** como trabalho final de Fundamentos da Programação.

### O que é HYROX?

HYROX é uma competição de corrida híbrida onde os atletas enfrentam 8km de corrida intercalados com 8 estações funcionais:
- Empurrão/Puxada de Trenó (Sled)
- Lançamento de Bola na Parede (Wall Balls)
- Simulador de Esqui (SkiErg)
- Burpee com Salto em Distância (Broad Jump Burpee)
- Remo (Row)
- Caminhada do Fazendeiro (Farmer's Carry)
- Passada com Saco de Areia (Lunges)
- Resistência de Corrida

## ✨ Funcionalidades Principais

### 1. **Gerenciamento de Treinos (CRUD)**
- ✅ Adicionar novos treinos com detalhes completos
- ✅ Visualizar todos os treinos cadastrados
- ✅ Editar treinos existentes
- ✅ Excluir treinos

**Informações capturadas por treino:**
- Nome do treino
- Tipo: Corrida, Força ou Simulado HYROX
- Data do treino
- Duração
- Intensidade: Leve, Moderada ou Pesada

### 2. **Controle de Desempenho**
- 📊 Registro detalhado de exercícios
- 📈 Rastreamento de métricas:
  - **Tempo** (em minutos/segundos)
  - **Distância** (em km/m)
  - **Carga** (em kg)
  - **Repetições** (quantidade)
- 🔄 Histórico completo por exercício

### 3. **Gerenciamento de Competições**
- 📅 Cadastro de competições
- 📍 Armazenamento de local e categoria
- ⏳ Cálculo automático de dias restantes para a competição
- 📋 Visualização de todas as competições cadastradas

### 4. **Acompanhamento de Evolução**
- 📊 **Frequência de Treinos**: visualiza quantos treinos foram feitos por mês
- 📈 **Evolução de Exercícios**: acompanha o progresso de cada exercício com indicadores:
  - `↑ MELHORA` - Métrica melhorou desde o primeiro registro
  - `↓ PIORA` - Métrica piorou desde o primeiro registro
  - `→ ESTÁVEL` - Métrica permaneceu constante

### 5. **Sugestões Personalizadas**
- 🎯 Recomendações de treino baseadas no nível do atleta:
  - **Iniciante**: 3 dias por semana (técnica)
  - **Intermediário**: 4 dias por semana (força + funcional)
  - **Avançado**: 5 dias por semana (força + volume + velocidade)
- 💡 Estratégias específicas para melhorar pontos fracos
- 📋 Sugestões baseadas no histórico de exercícios

### 6. **Coach Inteligente (IA)**
- 🤖 Integração com API Groq (modelo Llama 3.3-70B)
- 💬 Análise inteligente do histórico de treinos
- 🎯 Recomendações personalizadas
- ⚠️ Alertas sobre overtraining e recuperação
- 📊 Análise de:
  - Volume semanal
  - Intensidade e progressão
  - Frequência dos grupos musculares
  - Equilíbrio corrida vs força
  - Risco de lesão
  - Preparação para competições

## 🎮 Como Usar

### Menu Principal
```
==========BEM VINDO AO HYROX PLANNER==========

[1] Adicionar               - Cria um novo treino
[2] Visualizar treinos     - Mostra todos os treinos cadastrados
[3] Visualizar competições - Mostra as competições agendadas
[4] Editar                 - Modifica um treino existente
[5] Excluir                - Remove um treino
[6] Controle de Desempenho - Registra exercícios e métricas
[7] Adicionar competição   - Cadastra uma nova competição
[8] Acompanhar Evolução    - Visualiza progresso
[9] Sugestões Personalizadas - Recomendações de treino
[10] 🤖 Coach Inteligente   - IA para análise personalizada
[11] Parar                 - Encerra o programa
```

### Exemplo de Fluxo

1. **Adicionar um treino:**
   - Escolha `[1]`
   - Digite o nome do treino (ex: "Perna Pesada")
   - Selecione o tipo: Corrida, Força ou Simulado HYROX
   - Informe a data (formato: DD/MM/AAAA)
   - Registre a duração
   - Indique a intensidade: Leve, Moderada ou Pesada

2. **Registrar desempenho:**
   - Escolha `[6]`
   - Digite um treino existente
   - Adicione exercícios e suas métricas

3. **Acompanhar evolução:**
   - Escolha `[8]`
   - Visualize gráficos de frequência e progresso

## 📁 Estrutura de Arquivos

```
Código do projeto/
├── main.py                      # Aplicação principal (1135 linhas)
├── Sistema de Treinos.txt       # Banco de dados de treinos
├── Controle_de_Desempenho.txt  # Histórico de desempenho
├── Competições.txt              # Registro de competições
└── README.md                    # Documentação
```

## 🛠️ Requisitos Técnicos

### Dependências
- **Python 3.7+**
- **Groq Python SDK** (para integração com Coach IA)

### Instalação

```bash
# Clone o repositório
git clone https://github.com/Hyrox-Planner-grupo-2/Novo-sistema-de-Treinos.git

# Navegue até o diretório
cd Novo-sistema-de-Treinos/Código\ do\ projeto/

# Instale as dependências
pip install groq

# Execute o programa
python main.py
```

### Configuração da IA
Para usar o **Coach Inteligente**, você precisa ter uma chave de API da Groq:

1. Acesse [groq.com](https://groq.com)
2. Obtenha sua chave de API
3. No `main.py`, linha 984, substitua a string vazia pela sua chave:
   ```python
   client = Groq(api_key="sua_chave_aqui")
   ```

## 💾 Armazenamento de Dados

Os dados são armazenados em **arquivos de texto simples** (TXT), facilitando:
- ✅ Portabilidade
- ✅ Visualização manual
- ✅ Backup simples
- ✅ Compatibilidade multiplataforma

### Formato dos Arquivos

**Sistema de Treinos.txt:**
```
Dados do Treino:
NOME DO TREINO: PERNA
TIPO DE TREINO: CORRIDA
DATA DO TREINO: 01/05/2026
DURAÇÃO DO TREINO: 2 horas
INTENSIDADE DO TREINO: Treino Moderado
```

**Controle_de_Desempenho.txt:**
```
NOME_DO_TREINO
  NOME_DO_EXERCICIO
    Tempos:     12:30   12:15   12:00
    Distâncias: 500m    520m    550m
    Cargas:     60kg    65kg    70kg
    Repetições: 10      10      12
```

**Competições.txt:**
```
==========Nome da Competição==========
DATA: 22/09/2026     Faltam 112 dias
LOCAL: Recife
CATEGORIA: Categoria
```

## 🔑 Principais Recursos de Código

### Funções Principais
- `clear()` - Limpa a tela (compatível com Windows e macOS)
- `abrir_leitura()` - Lê dados dos arquivos
- `nomeDOtreino()` - Valida nome único do treino
- `tipoDEtreino()` - Interface para seleção de tipo
- `intensidadeDEtreino()` - Seleção de intensidade
- `validar_data()` - Validação de formato de data
- `controledesempenho()` - Gerenciamento de métricas
- `acompanhamento_evolucao()` - Análise de progresso
- `sugerir_treinos_personalizados()` - Recomendações baseadas em nível

### Recursos de Programação Utilizados
- ✅ Funções e escopo
- ✅ Loops e controle de fluxo
- ✅ Manipulação de strings e datas
- ✅ Tratamento de exceções
- ✅ Operações com arquivos (I/O)
- ✅ Estruturas de dados (listas e dicionários)
- ✅ Integração com APIs externas

## 🎓 Conceitos Aplicados (Fundamentos da Programação)

Este projeto demonstra o domínio de conceitos essenciais:

1. **Variáveis e Tipos de Dados** - Uso de strings, inteiros, booleanos
2. **Estruturas Condicionais** - if/elif/else para validações
3. **Loops** - while e for para iterações
4. **Funções** - Modularização do código
5. **Tratamento de Erros** - try/except/finally
6. **Manipulação de Arquivos** - Leitura e escrita de dados
7. **Trabalho com Strings** - split(), replace(), strip(), upper()
8. **Estruturas de Dados** - Listas e dicionários
9. **Integração com Bibliotecas Externas** - Groq, datetime

## 📊 Dashboard

Ao iniciar o programa, você verá:
```
==========BEM VINDO AO HYROX PLANNER==========

    ==========DASHBOARD==========

    Treinos cadastrados: X
    Competições cadastradas: Y
```

## 🚀 Diferenciais

- 🤖 **IA Integrada** - Coach inteligente para análise profissional
- 📱 **Interface Intuitiva** - Menu em português, fácil de usar
- 📊 **Análise Completa** - Frequência, evolução e sugestões
- 🔄 **Persistência de Dados** - Tudo salvo automaticamente
- ⚠️ **Alertas Inteligentes** - Aviso sobre overtraining e riscos

## 🐛 Tratamento de Erros

O sistema é robusto e trata:
- Datas inválidas
- Entradas não numéricas
- Arquivos ausentes (cria automaticamente)
- Treinos inexistentes
- Respostas inválidas do usuário

## 📝 Exemplo de Uso Completo

```python
# 1. Iniciar programa
python main.py

# 2. Adicionar treino
[1] → "Simulado Hyrox" → "Corrida" → "08/06/2026" → "45 min" → "Pesado"

# 3. Registrar desempenho
[6] → "Simulado Hyrox" → Adicionar exercícios (Sled, Wall Ball, Remo, etc.)

# 4. Acompanhar evolução
[8] → Ver gráficos de frequência e progresso

# 5. Obter sugestões
[9] → "Avançado" → Receber plano personalizado

# 6. Conversar com Coach IA
[10] → "Estou preparado para minha competição?" → Análise completa
```

## 👥 Desenvolvido por

Grupo 2 - Fundamentos da Programação  
[Hyrox-Planner-grupo-2](https://github.com/Hyrox-Planner-grupo-2)

## 📄 Licença

Este projeto é uma avaliação acadêmica. Consulte os termos de uso da instituição.

---

**Versão:** 1.0  
**Data de Criação:** Junho 2026  
**Linguagem:** Python 3.7+  
**Status:** ✅ Em Funcionamento
