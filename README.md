# 🏥 Health Analytics: Inteligência de Dados Aplicada à Saúde Pública

Bem-vindo ao meu repositório de Health Analytics! Este espaço foi criado para documentar e apresentar projetos práticos de Análise Exploratória de Dados (EDA), Estatística Descritiva e Inferência Científica, utilizando dados do Sistema Único de Saúde (SUS) e de gestão hospitalar.

O objetivo principal é demonstrar como o rigor metodológico da Ciência de Dados e do Analytics Engineering pode ser aplicado para otimizar processos assistenciais, gerenciar recursos de forma eficiente (FinOps) e fundamentar tomadas de decisão estratégicas em saúde pública.

## 👩‍💻 Sobre Mim & Proposta de Valor

Sou uma profissional com mais de 15 anos de trajetória sênior na saúde pública, atuando em liderança, Vigilância Epidemiológica e assessoria técnica de Secretarias de Saúde. Unindo essa sólida bagagem de regras de negócio à minha transição de carreira para a tecnologia, me especializei em Análise de Dados e Analytics Engineering.

Acredito que a tecnologia e a governança de dados na nuvem são os pilares para transformar registros brutos em desfechos clínicos positivos e eficiência operacional.

## 📂 Estrutura do Repositório e Projetos

Este repositório está organizado em módulos que refletem diferentes níveis de maturidade analítica e técnicas estatísticas:

0. **[Módulo 00] Engenharia de Dados & Data Wrangling — Pipeline Hospitalar**
   * **Conceitos Aplicados:** Sanitização de dados, tratamento de valores nulos, normalização de strings, validação temporal e padronização de categorias (*Data Wrangling*).
   * **Cenário de Negócio:** Tratamento de uma base de dados bruta (*Hospital Patients*) obtida via Kaggle, simulando os desafios reais de bases legadas na saúde para estruturar um pipeline limpo, versionado via Git/GitHub e pronto para análises avançadas.

1. **[Módulo 01] Análise Amostral Exploratória — UBS Bernoulli**
   * **Conceitos Aplicados:** Sanitização de dados, algoritmos de ordenação, distribuição de frequências (absoluta, relativa e acumulada) e análise de histograma.
   * **Cenário de Negócio:** Avaliação do perfil de atendimento de uma amostra de 50 pacientes ao longo de 1 ano em uma Unidade Básica de Saúde. O projeto identifica um grupo crítico de 20% de hiperfrequentadores (com mais de 100 consultas/ano), fornecendo insumos para auditoria de prontuários, busca ativa e planejamento de escalas da enfermagem.

2. **[Módulo 02] Análise Bivariada e Teste de Hipóteses — Gestão de Fluxos Hospitalares**
   * **Conceitos Aplicados:** Estatística Descritiva Avançada (Quartis, Decis, Coeficiente de Variação), Correlação Linear e Teste t de Student para duas amostras independentes (análise de p-valor bicaudal e valor crítico).
   * **Cenário de Negócio:** Estudo da interdependência entre duas variáveis contínuas: o tempo de resposta (Lead Time) na triagem da enfermagem e a Taxa de Ocupação Crítica de leitos de retaguarda. O modelo infere com segurança estatística (nível de significância de 5%) se a alteração de um protocolo de fluxo de trabalho gerou um impacto real na eficiência do hospital.

## 🛠️ Tecnologias, Ferramentas e Conceitos Fundamentais

* **Linguagens e Bibliotecas:** Python (Pandas, NumPy) e SQL para manipulação e limpeza.
* **Estatística:** Modelagem univariada e bivariada, testes de hipóteses e distribuições contínuas.
* **Governança & Arquitetura:** Conceitos de FinOps (otimização de custos de infraestrutura em nuvem), LGPD e desenho de pipelines de dados seguros (AWS IAM).

*Projetos desenvolvidos como aplicação prática e conexão de negócios com base nos modelos analíticos do MBA em Data Science (USP ESALQ).*
