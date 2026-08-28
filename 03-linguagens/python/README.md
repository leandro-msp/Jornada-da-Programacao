### Estudos em Python

Ambiente central para registro e organização dos meus estudos na linguagem Python. O projeto contém exercícios de fixação, scripts e pequenos algoritmos **focados** na aplicação prática de conceitos desenvolvidos em aulas e cursos. 

### Conteúdos do Repositório

* **Lógica & Algoritmos:** Resolução de problemas e estruturação de pensamento lógico.
* **Cenários Aplicáveis:** Casos de uso reais e simulações do dia a dia.
* **Uso de Bibliotecas:** Exploração de módulos nativos e externos.
* **Estruturas de Dados:** Manipulação de listas, dicionários, tuplas e conjuntos.
* **Pequenos Projetos:** Aplicações completas para consolidação do aprendizado.

### Como Executar os Scripts

Se você deseja clonar este repositório e executar os projetos localmente sem poluir o seu ambiente global do Python, siga os passos abaixo para configurar o ambiente virtual (`.venv`).

### 1. Clonar o repositório
```bash
git clone https://github.com/leandro-msp/Jornada-da-Programacao
cd jornada-da-programacao/03-linguagens/python
```
### 2. Criar e ativar o Ambiente Virtual (.venv)
  ainda no terminal dentro da pasta python, digite:
  ```bash
  python -m venv .venv
  ```
  e
  ```bash
  .\.venv\Scripts\Activate.ps1
  ``` 
### 3. Instalar as Dependências

Com o ambiente virtual ativado, instale todas as bibliotecas necessárias executando:
```bash
pip install -r requirements.txt
```
### Executando os Jupyter Notebooks (.ipynb) e arquivos.py que necessitam das bibliotecas
Para rodar os notebooks .ipynb no VS Code:

Abra o arquivo .ipynb desejado.

No canto superior direito do notebook, clique em **Select Kernel (ou Selecionar Kernel)**.

Selecione **Python Environments...** e escolha a versão referente à pasta .venv do projeto.

Caso não apareça automaticamente, selecione **"Enter interpreter path..."** e aponte para **.\.venv\Scripts\python.exe.**(navegue até onde você clonou o repositório, entre na pasta .venv\Scripts\ e selecione python.exe).
     


