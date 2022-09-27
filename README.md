# 27-09-2022
## Db Esquema 
- Formulação do esquema do banco de dados inicial
    - Não é um branch
- Criação da pasta db-scheme na raiz do projeto contendo o arquivo do esquema do banco de dados elaborado no drawio
## 004_Inclusao_Post
- Arquivos de atualização 
    - resouces/indicador.py
        - 1,2,3,4,5
    - app.py
        - 6
    - resouces/indicador.py
        - 7,8,9,10,11,12
- Processos incluidos
    - Introdução do metodo get para busca por indicadores através do ID e atraves do nome do indicador
        ![get_atraves_de_id_e_nome](/img/readme_img/0003.png)
    - Introdução do metodo post para incluir novos indicadores atraves do indicador_id ou indicador_nome, caso seja optado pelo indicador_nome, tanto o parse da url quanto o valor do json devem ser iguais, é checado também se o nome ja esta em uso 
        - Introdução pelo indicador_id, o id passado pelo parse da url não importa podendo ser não passado
        ![get_id](/img/readme_img/0004.png)
        - Introdução pelo indicador_nome, tanto o nome passado pelo parse da url quanto pelo arquivo json devem ser iguais 
        ![get_nome](/img/readme_img/0005.png)

# 26-09-2022
## 001_PrimeiraIteracao
- Teste de primeira iteração com a API realizada atravez do metodo get sobre o recurso hoteis 
    ![teste_get_indicadores](/img/readme_img/0001.png)

## 002_ListarIndicadoresSDB
- Listar atraves do comando get em indicares todos os indicadores do sistema 
- Atraves da requisição get em indicadores, todos os indicadores estão sendo listados 
    ![teste_get_indicadores_lista](/img/readme_img/0002.png)
- Os indicadores listados estão armazenados em uma lista não sendo utilizado um banco de dados

## 003_Refatoracao_001
- Criação do modulo resources com movimentação da classe indicadores para o mesmo 
- Estrutura da classe
    ~~~
    resources
        __init__.py
        indicador.py
    ~~~
- Requisição get/indicadores funcionando corretamente ainda
