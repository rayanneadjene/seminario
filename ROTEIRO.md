# ROTEIRO DE APRESENTAÇÃO – TEMA 4: QUALIDADE (SONAR)
# Tempo total: 20 minutos
# ============================================================

## SLIDE 1 – CAPA (30 segundos)
"Bom dia/tarde! Nosso tema hoje é Qualidade de Código com SonarQube.
Vamos falar sobre code smells — o que são, como detectar e como corrigir.
Dividimos em conceito + demonstração prática."


## SLIDE 2 – O QUE É QUALIDADE? (1 min 30 s)
"Antes de falar de ferramenta, o que é qualidade de código?
Não é só 'funcionar'. Código de qualidade tem três pilares:
  - Legibilidade: outro dev consegue entender sem precisar do autor
  - Manutenibilidade: dá pra alterar sem quebrar o resto
  - Confiabilidade: não tem bugs escondidos nem vulnerabilidades

Por que isso importa? Código ruim aumenta o custo de manutenção,
torna o trabalho em equipe difícil e impede a modularização."


## SLIDE 3 – O QUE É SONARQUBE? (2 min)
"SonarQube é uma ferramenta de análise estática — ela lê o código
SEM executar e aponta os problemas.

O que ela detecta?
  - Bugs potenciais
  - Vulnerabilidades de segurança
  - Code smells (o foco de hoje)
  - Código duplicado
  - Cobertura de testes

Ela gera um dashboard com métricas. Vamos ver isso na prática.
Versão gratuita roda local ou no sonarcloud.io.
Plugin SonarLint funciona diretamente no VS Code e IntelliJ."


## SLIDE 4 – CODE SMELLS (2 min)
"Code Smell — 'cheiro de código ruim' — é um padrão que indica problema.
Não é necessariamente um bug agora, mas vai virar um no futuro.

Os mais comuns detectados pelo SonarQube:
  - Código Morto: variáveis declaradas e nunca usadas
  - Método Longo: função que faz coisa demais (regra: máx ~20 linhas)
  - Código Duplicado: mesma lógica em dois lugares — se mudar uma, esquece a outra
  - Nome Ruim: variável 'x', 'temp', 'data' — não comunica nada
  - Complexidade alta: muitos ifs dentro de ifs (difícil de testar)
  - Acoplamento alto: classe que depende de 10 outras

Hoje vamos focar em 2: Código Duplicado e Método Longo."


## SLIDE 5 – RELAÇÃO COM MODULARIDADE (1 min 30 s)
"Por que isso é relevante para programação modular?

  1. Módulo bom = alta coesão (faz uma coisa só)
  2. Code smell de método longo = baixa coesão (faz tudo junto)
  3. Código duplicado viola DRY — a lógica fica espalhada em vários módulos
  4. SonarQube garante que cada módulo segue o SRP (já viram no Tema 3)
  5. Resultado: módulos pequenos, testáveis, reutilizáveis"


## SLIDE 6 – PROBLEMA 1: CÓDIGO DUPLICADO (2 min)
"Vamos ver o primeiro problema prático.

[Mostrar arquivo 'codigo_com_problemas.py']

Temos duas funções: calcular_desconto_cliente_vip e calcular_desconto_cliente_novo.
Olhando o código — são idênticas! Mesma lógica, mesmo retorno.

O SonarQube detecta isso como 'Duplicated Blocks' e mostra
exatamente as linhas repetidas.

O problema: se a regra de negócio mudar (ex: de 10% para 15%),
você precisa lembrar de alterar em DOIS lugares. E vai esquecer um.

[Mostrar 'codigo_refatorado.py']

A correção é simples: uma função única chamada calcular_desconto().
Os dois contextos chamam a mesma função. Mudança em um lugar, efeito em todos."


## SLIDE 7 – PROBLEMA 2: MÉTODO LONGO (2 min)
"Segundo problema: a função processar_pedido() no arquivo original.

[Mostrar o código]

Ela faz três coisas completamente diferentes:
  1. Valida os dados do pedido
  2. Calcula o total com descontos
  3. Salva no banco de dados

SonarQube aponta: Cognitive Complexity = 8 (acima do limite de 5).
Isso significa que pra entender a função você precisa guardar muita coisa na cabeça.

[Mostrar código refatorado]

Separamos em 3 funções: validar_pedido(), calcular_total(), salvar_pedido().
Cada uma faz UMA coisa. processar_pedido() agora é só o orquestrador.

Benefícios:
  - Fácil de testar cada parte individualmente
  - Se a regra de desconto mudar, só muda calcular_total()
  - Se trocar o banco de dados, só muda salvar_pedido()"


## SLIDE 8 – DEMONSTRAÇÃO PRÁTICA (5 min)
"Agora a demonstração ao vivo:

PASSO 1: Mostrar o código com problemas
  → Abrir 'codigo_com_problemas.py' no editor
  → Apontar visualmente os problemas

PASSO 2: Análise no SonarQube / SonarLint
  → [Opção A] Mostrar o SonarLint no VS Code sublinhando os problemas
  → [Opção B] Mostrar screenshot/demo do SonarQube Cloud com o relatório
  → Mostrar: número de code smells, onde estão, qual a gravidade

PASSO 3: Código refatorado
  → Abrir 'codigo_refatorado.py'
  → Mostrar que os problemas sumiram
  → SonarLint não aponta mais nenhum smell

[DICA: Se não tiver SonarQube rodando, use o SonarLint no VS Code —
instale a extensão, abra o arquivo com problemas e ele sublinha tudo automaticamente]"


## SLIDE 9 – RESUMO (1 min)
"Recapitulando:
  - Qualidade = legibilidade + manutenibilidade + confiabilidade
  - Code smells são sinais de problema — não bugs agora, mas no futuro
  - SonarQube detecta automaticamente, integra no CI/CD
  - Corrigimos 2 problemas: duplicação e método longo
  - Código limpo é base para modularização de qualidade

Alguma pergunta?"


# ============================================================
# DICAS GERAIS DE APRESENTAÇÃO
# ============================================================
# - Cada membro apresenta pelo menos 1 slide
# - Na demo, um faz a narrativa e outro mexe no código/tela
# - Se perguntarem sobre SonarQube vs pylint: SonarQube é mais
#   completo e tem interface web; pylint é só linha de comando
# - Se perguntarem custo: SonarQube Community é gratuito e open source
# ============================================================
