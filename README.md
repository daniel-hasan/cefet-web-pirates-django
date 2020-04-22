Nesta tarefa, o projeto (nome `web_pirates`) já está criado e o app (nome `pirates`) também. Os templates foram criados e os modelos também.

![Resultado final da atividade prática](https://github.com/daniel-hasan/cefet-web-pirates-django/blob/master/imgs/django-pirates-final.png?raw=true)


## Execício 1 - Configuração - Media URL
Como iremos inserir imagens do tesouro, é importante colocarmos o seguinte código em `settings.py`:

```python
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
```
em que  `MEDIA_URL` é a URL base que serão acessadas as medias e,  `MEDIA_ROOT` é aonde serão armazenada as medias que foram feito o UPLOAD.

Logo após, para que possamos acessar as URLs de media, adicione `static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)` em `urls.py` da seguinte forma:

```
urlpatterns = [
    path('admin/', admin.site.urls),
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
```
## Exercício 2 - Listar Tesouros


**Criação da visão**
Primeiramente, crie a visão `ListaTesourosView` que processa as requisições GET.  Nela você deverá retornar o template `lista_tesouros.html` renderizado e, com ele, os dados em um dicionário com as seguintes chaves:
-- `lista_tesouros`: Faça uma busca pelos tesouros. Você deverá criar uma anotação para criar a coluna `valor_total` que representa a multiplicação das colunas  `preco` e `quantidade`. [Veja os slides sobre isso](https://daniel-hasan.github.io/cefet-web-grad/classes/python3/#django). Fique atento com os nomes das colunas!
- `total_geral`: Somátorio do valor total de todos os tesouros



Não esqueça de usar o `import` apropriadamente para utilizar a classe Tesouro do `models.py`

**URL**
Logo após, crie a URL para referenciar a visão criada. Esta URL deverá referenciar a raiz do site. Não esqueça do `import` apropriado para usar a visão


**Template**

-O template `lista_tesouros.html` já está pronto mas a lista de tesouros não está sendo exibida ainda. Faça com que as linhas da tabela de tesouros sejam criadas dinamicamente. Para imprimir a url da imagem do tesouro use apenas `tesouro.img_tesouro.url` **não** use static, pois você acessará uma imagem que foi enviada pelo usuário. Também apresente o total geral. Deixe as colunas de editar e excluir ainda apenas com suas respectivas imagens 'imgs/edit.png' e 'imgs/delete.svg', use a tag/comando `static` para isso. Ao imprimir os campos, fique atento para não errar o nome de cada campo em `models.py`.




Rode o servidor executando `python3 manage.py runserver` e verifique o resultado.

## Execício 3 - Inserir Tesouro
Para inserir o tesouro, você deverá (1) criar o ModelForm apropriado - o label da imagem do tesouro deverá ter o nome 'Imagem'; (2) crie a visão `SalvarTesouro`, para processar o `get` e `post` - get para apresentar o form e post para inserir; (3) alterar o template `salvar_tesouro.html` para apresentar o form - ele deve estar dentro de uma tag HTML `<form>` e o método deve ser `post`; (4) criar a URL para inserção. Caso tenha duvidas, [Veja como criar o ModelForm](https://daniel-hasan.github.io/cefet-web-grad/classes/python4/#model-form).

No post, deverá ser verificado se o formulário é valido. Caso seja válido, o tesouro é inserido e o usuário será redirecionado para a página que lista tesouro, caso contrário, será renderizado o `salva_tesouros.html` com o form inválido.



Altere template `lista_tesouros.html` para criar um link referenciando a página de inserção. Para isso, altere o link que possui o id HTML `inserir`. Crie o link usando o nome da url de inserir (use o comando/tag url igual na prática anterior).



Execute o makemigrations e o migrate e, logo após, teste no servidor a inserção de tesouros.

## Exercício 4 - Remover Tesouro

Faça a visão para remover o tesouro. Você deverá passar, via get, o id do tesouro para ser removido. Crie a visão e a URL de remoção. Logo após, altere o template criando um link para remoção de um determinado tesouro. Crie o link da mesma [forma que foi criado na prática anterior](https://daniel-hasan.github.io/cefet-web-grad/classes/python4/#urls): referenciando o nome da URL. Não esqueça de passar o id do tesouro como parametro também. [Para criar a URL e trata-la na view, veja os slides de hoje de como tratar os parametros da URL](https://daniel-hasan.github.io/cefet-web-grad/classes/python5/#urls-params). Ao finalizar, você deverá redirecionar para a página de listar os tesouros.

## Exercício 5 -  Atualizar Tesouro

Para fazer de forma simples, você deverá reaproveitar o template `salvar_tesouro.html` e a view `SalvarTesouro` para isso. Assim, crie uma URL, similar a de inserção, porém, agora, com um parâmetro que é o id do tesouro. Os métodos post e get da view deverá opcionalmente passar o `id` como parametro. Na view, caso tenha sido passado o id do tesouro, ao instanciar o ModelForm do tesouro você deverá passar como parametro do mesmo a instancia do tesouro que possui esse determinado id.  Veja slides para [criação da URL com parametros](https://daniel-hasan.github.io/cefet-web-grad/classes/python4/#urls-params) e sobre a atualização do form. Logo após, no template listar_tesouro.html, crie o link para o botão de editar. Não esqueça de passar o id do tesouro como parametro desta URL.
