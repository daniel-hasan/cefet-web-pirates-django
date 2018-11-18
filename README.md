Nesta tarefa, você já possui todos os


## Execício 1 - Configuração - Media URL

```
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
```

## Exercício 2 - Listar Tesouros 


**Criação da visão** 
Primeiramente, crie um visão que processa as requisições GET. Nela você deverá retornar o template `lista_tesouros.html` renderizado e, com ele, os dados em um dicionário com as seguintes chaves:
- `lista_tesouros`: Faça uma busca pelos tesouros. Você deverá criar uma agregração para obter a coluna `valor_total` que representa a multiplicação das colunas  `valor` e `quantidade`. [Veja os slides sobre isso]().
- `total_geral`: Somátorio do valor total de todos os tesouros



Não esqueça de usar o `import` apropriadamente para utilizar a classe Tesouro do `models.py`

**URL**
Logo após, crie a URL para referenciar a visão criada. Esta URL deverá referenciar a raiz do site. Não esqueça do `import` apropriado para usar a visão


**Template** 

O template `lista_tesouros.html` já está pronto mas a lista de tesouros não está sendo exibida ainda. Faça com que as linhas da tabela de tesouros sejam criadas dinamicamente. Também apresente o valor total. [Você pode aplicar um filtro para apresentar os valores de moeda da melhor forma](https://docs.djangoproject.com/en/2.1/ref/templates/builtins/#floatformat). Deixe as colunas de editar e excluir ainda apenas com suas respectivas imagens 'imgs/edit.png' e 'imgs/delete.svg', use a tag/comando `static` para isso. Ao imprimir os campos, fique atento para não errar o nome de cada campo em `models.py`.

 
Rode o servidor executando `python3 manage.py runserver` e verifique o resultado.

## Execício 3 - Inserir Tesouro
Para inserir o tesouro, você deverá (1) criar o ModelForm apropriado - o label da imagem do tesouro deverá ter o nome 'Imagem'; (2) crie a visão `SalvarTesouro`, para processar o `get` e `post` - get para apresentar o form e post para inserir; (3) alterar o template `salvar_tesouro.html` para apresentar o form - ele deve estar dentro de uma tag HTML `<form>` e o método deve ser `post`; (4) criar a URL para inserção; 

No post, deverá ser verificado se o formulário é valido. Caso seja válido, o tesouro é inserido e o usuário será redirecionado para a página que lista tesouro, caso contrário, será renderizado o `salva_tesouros.html` com o form inválido.


Altere template `lista_tesouros.html` para criar um link referenciando a página de inserção. Para isso, altere o botão que possui o id HTML `inserir`. Crie o link usando o nome da url de inserir (igual na prática anterior).

Ao inserir tesouro, você verificará que automaticamente será criado a pasta "img" para salvar as imagens. Teste a inserção de tesouros.

## Exercício 4 - Remover Tesouro 

Faça a visão para remover o tesouro. Você deverá passar, via get, o id do tesouro para ser removido. Crie a visão e a URL de remoção. Logo após, altere o template criando um link para remoção de um determinado tesouro. Crie este link da mesma [forma que foi criado na prática anterior](https://daniel-hasan.github.io/cefet-web-grad/classes/python4/#urls): referenciando o nome da URL. Não esqueça de passar o id do tesouro como parametro também. 

## Exercício 5 -  Atualizar Tesouro

Para fazer de forma simples, você deverá reaproveitar o template `salvar_tesouro.html` e a view `SalvarTesouro` para isso. Assim, crie uma URL, similar a de inserção, porém, agora, com um parâmetro que é o id do tesouro. Os métodos post e get da view deverá opcionalmente passar o `id` como parametro. Na view, caso tenha sido passado o id do tesouro, ao instanciar o ModelForm do tesouro você deverá passar como parametro do mesmo a instancia do tesouro que possui esse determinado id. 

 


