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

# 27-09-2022
## Db Esquema 
- Formulação do esquema do banco de dados inicial
    - Não é um branch
- Criação da pasta db-scheme na raiz do projeto contendo o arquivo do esquema do banco de dados elaborado no drawio
## 