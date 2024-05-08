Claro, vou criar um README.md em Markdown explicando o MLOps Toolkit com os itens solicitados.

# MLOps Toolkit

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)



## Descrição

O MLOps Toolkit é uma coleção de ferramentas e tecnologias essenciais para a implementação eficiente de práticas de MLOps (Machine Learning Operations). Ele visa facilitar o gerenciamento e a automação de pipelines de machine learning, desde o desenvolvimento até a produção, garantindo a reproducibilidade, escalabilidade e monitoramento adequado de modelos de machine learning.

## Componentes Principais

### Orquestradores
O orquestrador é um componente essencial em qualquer pilha MLOps, pois é responsável por executar seus pipelines de aprendizado de máquina. Para isso, o orquestrador fornece um ambiente configurado para executar as etapas do seu pipeline. Ele também garante que as etapas do seu pipeline só sejam executadas quando todas as suas entradas (que são saídas das etapas anteriores do seu pipeline) estiverem disponíveis.

### Loja de Artefatos
O Artifact Store é um componente central em qualquer pilha MLOps. Como o nome sugere, ele atua como uma camada de persistência de dados onde são armazenados artefatos (por exemplo, conjuntos de dados, modelos) ingeridos ou gerados pelos pipelines de aprendizado de máquina.

### Registro de Contêineres
O registro do contêiner é uma parte essencial da maioria das pilhas MLOps remotas. Ele é usado para armazenar imagens de contêiner criadas para executar pipelines de aprendizado de máquina em ambientes remotos. A conteinerização do código do pipeline cria um ambiente portátil que permite que o código seja executado de maneira isolada.

### Validadores de Dados
Sem bons dados, mesmo os melhores modelos de aprendizado de máquina produzirão resultados questionáveis. Muito esforço é feito para garantir e manter a qualidade dos dados não apenas nos estágios iniciais de desenvolvimento do modelo, mas durante todo o ciclo de vida do projeto de aprendizado de máquina. Validadores de dados são uma categoria de bibliotecas, ferramentas e estruturas de ML que concedem uma ampla gama de recursos e práticas recomendadas que devem ser empregadas nos pipelines de ML para manter a qualidade dos dados sob controle e monitorar o desempenho do modelo para evitar sua degradação ao longo do tempo.

### Rastreadores de Experimentos
Os rastreadores de experimentos permitem que você acompanhe seus experimentos de ML registrando informações estendidas sobre seus modelos, conjuntos de dados, métricas e outros parâmetros e permitindo que você os navegue, visualize e compare entre execuções. 

### Implantadores de Modelo
Implantação de modelo é o processo de disponibilizar um modelo de aprendizado de máquina para fazer previsões e decisões sobre dados do mundo real. A obtenção de previsões de modelos treinados pode ser feita de diferentes maneiras, dependendo do caso de uso. Uma previsão em lote é usada para gerar previsões para uma grande quantidade de dados de uma só vez, enquanto uma previsão em tempo real é usada para gerar previsões para um único ponto de dados. de uma vez.

Os implantadores de modelos são componentes de pilha responsáveis ​​por servir modelos em tempo real ou em lote.

### Operadores de Etapa
O operador step permite a execução de etapas individuais de pipeline em ambientes de tempo de execução especializados otimizados para determinadas cargas de trabalho. Esses ambientes especializados podem dar acesso a recursos como GPUs ou estruturas de processamento distribuído como Spark .

### Alertas
Os alertas permitem que você envie mensagens para serviços de bate-papo (como Slack, Discord, Mattermost, etc.) de dentro de seus pipelines. Isso é útil para ser notificado imediatamente quando ocorrem falhas, para monitoramento/relatórios gerais e também para construir ML humano no circuito.

### Loja de Recursos
Os armazenamentos de recursos permitem que as equipes de dados forneçam dados por meio de um armazenamento offline e um armazenamento online de baixa latência, onde os dados são mantidos sincronizados entre os dois. Ele também oferece um registro centralizado onde os recursos (e esquemas de recursos) são armazenados para uso em uma equipe ou organização mais ampla.

### Anotadores
Anotadores são um componente de pilha que permite o uso de anotação de dados como parte de sua pilha e pipelines. Você pode usar o comando CLI associado para iniciar anotações, configurar seus conjuntos de dados e obter estatísticas sobre quantas tarefas rotuladas você tem prontas para uso.

A anotação/rotulagem de dados é uma parte essencial dos MLOps que frequentemente é deixada de fora da conversa. O começará a construir gradativamente recursos que suportam um fluxo de trabalho de anotação iterativo que vê as pessoas que fazem a rotulagem (e seus fluxos de trabalho/comportamentos) como partes integradas de seu(s) processo(s) de ML.

### Construtores de Imagens
O construtor de imagens é uma parte essencial da maioria das pilhas MLOps remotas. Ele é usado para criar imagens de contêiner de forma que seus pipelines e etapas de aprendizado de máquina possam ser executados em ambientes remotos.

### Registros de Modelos
Os registros de modelos são soluções de armazenamento centralizadas para gerenciar e rastrear modelos de aprendizado de máquina em vários estágios de desenvolvimento e implantação. Eles ajudam a rastrear as diferentes versões e configurações de cada modelo e permitem a reprodutibilidade. Ao armazenar metadados como versão, configuração e métricas, os registros de modelos ajudam a agilizar o gerenciamento de modelos treinados.


| Type of Stack Component | Description                                                   |
|-------------------------|---------------------------------------------------------------|
| Orchestrator            | Orchestrating the runs of your pipeline                       |
| Artifact Store          | Storage for the artifacts created by your pipelines           |
| Container Registry      | Store for your containers                                     |
| Step Operator           | Execution of individual steps in specialized runtime environments |
| Model Deployer          | Services/platforms responsible for online model serving       |
| Feature Store           | Management of your data/features                              |
| Experiment Tracker      | Tracking your ML experiments                                  |
| Alerter                 | Sending alerts through specified channels                      |
| Annotator               | Labeling and annotating data                                  |
| Data Validator          | Data and model validation                                     |
| Image Builder           | Builds container images.                                      |
| Model Registry          | Manage and interact with ML Models                            |







### BentoML

**BentoML** é uma estrutura de código aberto que simplifica o empacotamento de modelos de machine learning e serviços associados em contêineres Docker prontos para produção. Ele permite a criação de APIs RESTful e de artefatos de modelo de forma simples e rápida, garantindo a portabilidade e a facilidade de implantação em diferentes ambientes de produção.

### MLflow

**MLflow** é uma plataforma de código aberto para gerenciamento de ciclo de vida de modelos de machine learning. Ele oferece recursos para rastreamento de experimentos, gerenciamento de versões de modelos, reprodução de resultados e implantação de modelos em várias plataformas, facilitando a colaboração e a escalabilidade em equipes de machine learning.

### Pachyderm

**Pachyderm** é uma plataforma de código aberto para construção de pipelines de dados escaláveis e reprodutíveis. Ele oferece uma abordagem baseada em versionamento para o processamento de dados, permitindo a criação de pipelines de machine learning robustos e confiáveis que podem ser facilmente reproduzidos e escalados para grandes volumes de dados.

### Prefect

**Prefect** é uma estrutura de código aberto para automação de fluxos de trabalho e orquestração de pipelines de dados. Ele fornece uma API Python intuitiva para definir e executar fluxos de trabalho complexos, com suporte integrado para agendamento, monitoramento e tratamento de erros, tornando mais fácil e eficiente o gerenciamento de pipelines de machine learning.

### Seldon

**Seldon** é uma plataforma de implantação de modelos de machine learning em escala, projetada para Kubernetes. Ele oferece recursos para implantar, monitorar e gerenciar modelos de machine learning em produção, com suporte para exploração de modelos, monitoramento de desempenho e atualização contínua, garantindo a disponibilidade e a confiabilidade de sistemas de machine learning em produção.

### ZenML

**ZenML** é uma estrutura de código aberto para gerenciamento de pipelines de machine learning com foco na simplicidade e na escalabilidade. Ele oferece uma abordagem baseada em configuração para definir e executar pipelines de machine learning, com suporte integrado para versionamento de dados e modelos, experimentação automatizada e implantação de modelos em diferentes ambientes, facilitando o desenvolvimento e a operação de sistemas de machine learning em larga escala.

## Como Usar

Para começar a usar o MLOps Toolkit, siga as instruções de instalação e configuração para cada uma das ferramentas incluídas. Consulte a documentação oficial de cada ferramenta para obter mais detalhes sobre como utilizá-las em conjunto para criar e gerenciar pipelines de machine learning de ponta a ponta.

![MLOps Pipeline](./img/mlops1.png)
