<h1 align="center">Kaggle-Complete IMDB Movies</h1>
<h2 align="center">Python, Django, Django Rest Framework</h2>


Aprendizado adquirido com a série de vídeos do canal Pedro Impulcetto
- Vídeo 1 - [Criar uma API REST com Django](https://www.youtube.com/watch?v=wtl8ZyCbTbg)
- Vídeo 2 - [Adicionar upload de imagens](https://www.youtube.com/watch?v=Syoz9ldmS6o)
- Vídeo 3 - [Versionar códigos no Github](https://www.youtube.com/watch?v=FL8RtqJJwmQ)
- Vídeo 4 - [Deploy no Heroku](https://www.youtube.com/watch?v=01iXLbvGcNE)
- Vídeo 5 - [Utilizar Storage Cloud](https://www.youtube.com/watch?v=_Rsclg1FpPY)


Base de Dados:
- [Kaggle - Complete IMDB Movies Dataset](https://www.kaggle.com/datasets/gorochu/complete-imdb-movies-dataset)
    <p>A dataset of complete movies scraped from IMDB</p>

<details> 
    <summary><strong>Configurações Iniciais</strong></summary>
    <br />
    <div>
        <p><b>Passo 1</b> - criar a pasta do projeto no repositório local<br />
        - mkdir nome_pasta<br />
        - cd nome_pasta
        <br />
        <p><b>Passo 2</b> - criar e acessar o ambiente virtual<br />
        - python3 -m venv venv<br />
        - source venv/bin/activate
        <br />
        <p><b>Passo 3</b> - instalar as dependências que serão utilizadas<br />
        - pip install django djangorestframework pillow<br />
        - pillow: biblioteca que trabalha com imagens
        <br />
        <p><b>Passo 4</b> - criar o projeto (utilizar ponto para instalar no diretório atual)<br />
        - django-admin startproject nome_projeto .
        <br />
        <p><b>Passo 5</b> - configurar o arquivo settings.py<br />
        - import os<br />
        - TEMPLATES = ['DIRS': [os.path.join(BASE_DIR, 'templates')],]<br />
        - INSTALLED_APPS = ['rest_framework',]<br />
        - LANGUAGE_CODE = 'pt-br'<br />
        - TIME_ZONE = 'America/Sao_Paulo'
        <br />
        <p><b>Passo 6</b> - criar o super usuário<br />
        - python manage.py createsuperuser
        <br />
        <p><b>Passo 7</b> - criar as tabelas iniciais dentro do banco de dados<br />
        - python manage.py makemigrations<br />
        - python manage.py migrate
        <br />
        <p><b>Passo 8</b> - inicializar o servidor<br />
        - python manage.py runserver<br />
        - http://127.0.0.1:8000/
        <br />
        <p><b>Passo 9</b> - criar o repositório remoto no Github<br />
        - GitHub: https://github.com/<br />
        - inicializar o repositório local e adicionar ao repositório remoto
        <br />
    </div>
</details>
 
<details> 
    <summary><strong>Criar uma API Rest</strong></summary>
    <br />
    <div>
        <p><b>Passo 1</b> - criar o app<br />
        - django-admin startapp nome_app
        <br />
        <p><b>Passo 2</b> - configurar o projeto no arquivo settings.py<br />
        - INSTALLED_APPS = ['nome_app',]
        <br />
        <p><b>Passo 3</b> - criar os campos do projeto no arquivo models.py<br />
        - criar os campos da tabela do projeto<br />
        - importar a biblioteca from uuid import uuid4 para o campo id
        - criar função para armazenar o nome do arquivo de imagem: def upload_image(instance, filename):
        <br />
        <p><b>Passo 4</b> - criar o arquivo serializers dentro da pasta nome_app/api<br />
        - from rest_framework import serializers<br />
        - from nome_app import models
        <br />
        <p><b>Passo 5</b> - criar o arquivo viewsets dentro da pasta nome_app/api<br />
        - from rest_framework import viewsets<br />
        - from nome_app.api import serializers<br />
        - from nome_app import models
        <br />
        <p><b>Passo 6</b> - identificar aonde será armazenado as imagens no arquivo settings.py<br />
        - import os<br />
        - criar variáveis de ambiente<br />
            - MEDIA_URL = '/media/'<br />
            - MEDIA_ROOT = os.path.join(BASE_DIR, 'media')<br />
        <p><b>Passo 7</b> - criar as rotas no arquivo urls<br />
        - from rest_framework import routers<br />
        - from nome_app.api import viewsets as nome_appviewsets<br />
        - from django.conf.urls.static import static<br />
        - from django.conf import settings
        <br />
        <p><b>Passo 8</b> - incluir o model no admin.py<br />
        - from .models import Nome_app
        <br />
        <p><b>Passo 9</b> - criar as tabelas do novo modelo dentro do banco de dados<br />
        - python manage.py makemigrations<br />
        - python manage.py migrate
        <br />
        <p><b>Passo 10</b> - inicializar o projeto<br />
        - python manage.py runserver
        <br />
    </div>
</details>

<details> 
    <summary><strong>Criar e Autenticar Usuários</strong></summary>
    <br />
    <div>
        <p><b>Passo 1</b> - criar o app users<br />
        - django-admin startapp users
        <br />
        <p><b>Passo 2</b> - configurar o projeto no arquivo settings.py<br />
        - INSTALLED_APPS = ['users',]
        <br />
        <p><b>Passo 3</b> - definir as urls<br />
        - from django.urls import path<br />
        - from . import views
        <br />
        <p><b>Passo 4</b> - criar as funções no arquivo views.py<br />
        - from django.http import HttpResponse<br />
        - return HttpResponse('login')
        <br />
        <p><b>Passo 5</b> - criar os campos do cadastro de usuários no arquivo models.py<br />
        - criar os campos
        <br />
    </div>
</details>

<details> 
    <summary><strong>Deploy no Heroku</strong></summary>
    <br />
    <div>
        <p><b>Passo 1</b> - instalar o heroku cli<br />
        - Heroku: https://www.heroku.com/home<br />
        - verificar a versão: heroku --version<br />
        - logar: heroku login
        <br />
        <p><b>Passo 2</b> - criar um projeto dentro do heroku<br />
        - heroku create nome_site
        <br />
        <p><b>Passo 3</b> - incluir a url dentro do arquivo settings.py<br />
        - ALLOWED_HOSTS = ['https://nome_site.herokuapp.com/']
        <br />
        <p><b>Passo 4</b> - criar o arquivo Procfile<br />
        - dentro da pasta root do projeto<br />
        - para saber o nome do projeto: ROOT_URLCONF = 'nome_app.urls'
        <br />
        <p><b>Passo 5</b> - instalar pacotes para ajudar a configurar o deploy<br />
        - pip install django-heroku<br />
        - pip install gunicorn
        <br />
        <p><b>Passo 6</b> - criar o arquivo requirements.txt<br />
        - pip freeze > requirements.txt
        <br />
        <p><b>Passo 7</b> - subir a aplicação para o Heroku<br />
        - git push heroku master
        <br />
    </div>
</details>
