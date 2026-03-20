# Levantamento de Requisitos projeto: VagaVision.

## 1. Visão Geral

O **VagaVision** é um sistema de gestão de tráfego urbano com foco em **predição de disponibilidade de vagas de estacionamento**. A solução tem como objetivo auxiliar motoristas na tomada de decisão, reduzindo o tempo de busca por vagas e contribuindo para a mobilidade urbana.
O sistema utilizará dados históricos e variáveis externas para fornecer recomendações inteligentes aos usuários.
Este projeto foi desenvolvido como solução ao desafio proposto pela empresa parceira **Dsin**. Este documento detalha as funcionalidades e restrições do sistema.


## 2. Requisitos Funcionais (RF)

| ID | Requisito | Descrição | Prioridade |
| :--- | :--- | :--- | :--- |
| **RF01** | *Predição de vagas* | O sistema deve calcular a probabilidade de disponibilidade de vagas com base em dados históricos, exibindo percentuais por horário e localização. | **ALTA** |
| **RF02** | *Cadastro de usuário* | O sistema deve permitir o cadastro de usuários com e-mail e senha, incluindo validação de dados. | **ALTA** |
| **RF03** | *Autenticação* | O sistema deve permitir login e logout de usuários autenticados. | **ALTA** |
| **RF04** | *Filtros de busca* | O sistema deve permitir a aplicação de filtros como: horário, localização, probabilidade de vagas e popularidade da região. | **ALTA** |
| **RF05** | *Mapa interativo* | O sistema deve exibir um mapa interativo com indicação visual das regiões com maior probabilidade de vagas. | **ALTA** |
| **RF06** | *Roteamento* | O sistema deve fornecer rotas até a localização selecionada, priorizando regiões com maior probabilidade de vagas. | **MÉDIA** |
| **RF07** | *Notificações* | O sistema deve permitir que o usuário configure notificações baseadas em localização e horários de interesse. | **MÉDIA** |
| **RF08** | *Histórico do usuário* | O sistema deve armazenar e exibir o histórico de buscas e locais consultados pelo usuário. | **BAIXA** |
| **RF09** | *Recuperação de senha* | O sistema deve permitir recuperação de senha via e-mail. | **MÉDIA** |


## 3. Requisitos Não Funcionais (RNF)

* **RNF01 (Disponibilidade):**  O sistema deve estar disponivel *100%* do tempo para o usuário.
* **RNF02 (Desempenho):** O tempo de resposta para consultas e predições deve ser inferior a **3 segundos**.
* **RNF03 (Escalabilidade):** O sistema deve suportar crescimento horizontal da base de dados e usuários.
* **RNF04 (Segurança):** Senhas devem ser armazenadas utilizando algoritmos de hash seguro (ex: bcrypt).
* **RNF05 (Privacidade):**  O sistema deve estar em conformidade com a LGPD no tratamento de dados pessoais e de geolocalização.
* **RNF06 (Usabilidade):** A interface deve seguir o conceito *Mobile-First*, garantindo usabilidade em dispositivos móveis.
* **RNF07 (Manutenibilidade):** O código deve ser modular e documentado para facilitar manutenção e evolução.


## 4. Regras de Negócio (RN)

* **RN01 (Cálculo preditivo):** A predição deve considerar dados históricos de ocupação de vagas. 
* **RN02 (Variáveis externas):** O sistema deve considerar fatores externos como feriados, eventos locais e dias da semana. 
* **RN03 (Probabilidade mínima):** Recomendações só devem ser exibidas quando a probabilidade de vaga for superior a um limite configurável (ex: 60%).


## 5. Tecnologias

- **Backend:** Python  
- **Banco de Dados:** MySQL  
- **Frontend:** HTML5, CSS3  
- **Integrações:** APIs de mapas e geolocalização  
