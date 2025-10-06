# Sistema de Diagnóstico Baseado em Sintomas com Python e SQLite

⚠️ **Aviso Importante:** Este projeto **Não deve ser utilizado para diagnósticos médicos reais.**

Este repositório contém um sistema especialista simples, desenvolvido em Python que fiz durante minhas aulas de Inteligência Artificial Aplicada na Uninter quando o professor nos fez um desafio de como recalibrariamos os pesos após erros da LLM. Ele simula um diagnóstico de resfriado com base nos sintomas relatados pelo usuário. O projeto utiliza um banco de dados **SQLite** para armazenar e ajustar dinamicamente os "pesos" de cada sintoma, criando um mecanismo de aprendizagem primitivo baseado no feedback do usuário.

## 🎯 Principais Características

* **Sistema de Diagnóstico Interativo**: O script interage com o usuário através do terminal, fazendo perguntas sobre seus sintomas.
* **Lógica Baseada em Pesos**: O diagnóstico é calculado atribuindo-se pesos a cada sintoma e a combinações de sintomas.
* **Persistência de Dados com SQLite**: Os pesos são armazenados em um banco de dados SQLite, o que significa que o "conhecimento" do sistema persiste entre as execuções.
* **Mecanismo de Aprendizagem por Feedback**: Ao final, o sistema pergunta se o diagnóstico estava correto. Se a resposta for negativa, ele ajusta os pesos no banco de dados, "aprendendo" com o erro para tentar ser mais preciso no futuro.

## 🔧 Pré-requisitos

Apenas uma instalação padrão do Python 3 é necessária. A biblioteca `sqlite3` já vem incluída na instalação padrão do Python, então não são necessárias instalações adicionais.

## 🚀 Como Executar

1.  Clone este repositório:
    ```bash
    git clone https://github.com/Leturnos/uninter-python-symptom-checker.git
    ```
2.  Navegue até o diretório do projeto:
    ```bash
    cd uninter-python-symptom-checker
    ```
3.  Execute o script Python:
    ```bash
    python ex2.py
    ```
Na primeira execução, o script criará um arquivo de banco de dados chamado `testeIA.db` com os pesos iniciais.

## ⚙️ Como Funciona?

1.  **Inicialização do Banco de Dados**: O script verifica se a tabela `Chance` existe no banco de dados. Se não, ela é criada. Se a tabela estiver vazia, os pesos iniciais são inseridos.
2.  **Coleta de Sintomas**: O programa faz quatro perguntas de "sim" ou "não" ao usuário para determinar os sintomas presentes.
3.  **Cálculo do Diagnóstico**: Os pesos são lidos do banco de dados. Uma pontuação de "chance" é calculada somando os pesos dos sintomas relatados. Combinações específicas (ex: Febre + Garganta) têm pesos próprios para aumentar a precisão.
4.  **Apresentação do Resultado**: Com base em um limiar (50%), o sistema informa ao usuário se ele provavelmente está ou não resfriado.
5.  **Loop de Feedback e Aprendizagem**:
    * O sistema pergunta se acertou o diagnóstico.
    * Se o usuário responder **"não"**, o script identifica quais pesos contribuíram para o resultado e os **reduz ligeiramente**, atualizando os valores no banco de dados.
    * Essa alteração é salva com `conn.commit()`, garantindo que o sistema usará os novos pesos na próxima execução.

Este mecanismo de feedback é uma forma simples de aprendizado por reforço, onde o sistema é "punido" por um erro e ajusta seu comportamento futuro.

<img width="600" height="400" alt="Captura de tela 2025-08-28 200103" src="https://github.com/user-attachments/assets/1dfdbb16-7afc-4cad-aa43-a6ceb6353f3f" />
<img width="600" height="400" alt="Captura de tela 2025-08-28 200124" src="https://github.com/user-attachments/assets/324be772-d71d-4f5e-b2c1-7ce9d4595a2f" />


