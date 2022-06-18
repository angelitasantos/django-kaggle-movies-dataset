<h1 align="center">API REST: Kaggle-Complete IMDB Movies</h1>
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
    <summary><strong>Criar uma API Rest</strong></summary>
    <br />
    <div>
        <p><b>Passo 1</b> - criar a pasta<br />
        - mkdir contact<br />
        - cd contact<br />
        <p><b>Passo 2</b> - criar e acessar um ambiente virtual<br />
        - python3 -m venv .venv<br />
        - source .venv/bin/activate<br />
        <p><b>Passo 3</b> - instalar as dependências do Django e Django Rest Framework<br />
        - pip install django djangorestframework<br />
        <p><b>Passo 4</b> - criar o projeto (utilizar ponto para instalar no diretório atual)<br />
        - django-admin startproject contact .<br />
        <p><b>Passo 5</b> - criar o app<br />
        - django-admin startapp people<br />
        <p><b>Passo 6</b> - criar as tabelas dentro do banco de dados<br />
        - python manage.py makemigrations<br />
        - python manage.py migrate<br />
        <p><b>Passo 7</b> - inicializar o servidor<br />
        - python manage.py runserver<br />
        - http://127.0.0.1:8000/<br />
        <p><b>Passo 8</b> - configurar o projeto no arquivo settings.py<br />
        - adicionar 
        INSTALLED_APPS = [
            'rest_framework',
            'people',
        ]<br />
        <p><b>Passo 9</b> - criar o model do projeto no arquivo models.py<br />
        - criar os campos da tabela de contatos<br />
        - importar a biblioteca from uuid import uuid4 para o campo id<br />
        <p><b>Passo 10</b> - criar o arquivo serializers dentro da pasta people/api<br />
        - from rest_framework import serializers<br />
        - from people import models<br />
        <p><b>Passo 11</b> - criar o arquivo viewsets dentro da pasta people/api<br />
        - from rest_framework import viewsets<br />
        - from people.api import serializers<br />
        - from people import models<br />
        <p><b>Passo 12</b> - criar as rotas no arquivo urls<br />
        - from rest_framework import routers<br />
        - from people.api import viewsets as peopleviewsets<br />
        <p><b>Passo 13</b> - criar as tabelas do novo modelo dentro do banco de dados<br />
        - python manage.py makemigrations<br />
        - python manage.py migrate<br />
        <p><b>Passo 14</b> - inicializar o projeto<br />
        - python manage.py runserver<br />
        <p><b>Passo 15</b> - incluir campo de opções no models.py<br />
        - python manage.py makemigrations<br />
        - python manage.py migrate<br />
        <p><b>Passo 16</b> - incluir o model no admin.py<br />
        - from .models import People<br />
        <p><b>Passo 17</b> - criar o super usuário<br />
        - python manage.py createsuperuser<br />
    </div>
</details>   
<details> 
    <summary><strong>Adicionar a opção de upload de imagens</strong></summary>
    <br />
    <div>
        <p><b>Passo 18</b> - upload de imagens<br />
        - incluir nova coluna image no models.py<br />
        <p><b>Passo 19</b> - criar uma função para armazenar o nome do arquivo<br />
        - def upload_image_people(instance, filename):<br />
        <p><b>Passo 20</b> - identificar aonde será armazenado as imagens no arquivo settings.py<br />
        - import os<br />
        - criar variáveis de ambiente<br />
            - MEDIA_URL = '/media/'<br />
            - MEDIA_ROOT = os.path.join(BASE_DIR, 'media')<br />
        <p><b>Passo 21</b> - instalar a biblioteca que trabalha com imagens<br />
        - pip install Pillow<br />
        <p><b>Passo 22</b> - incluir dentro das urls a especificação da url de imagem<br />
        - from django.conf.urls.static import static<br />
        - from django.conf import settings<br />
        <p><b>Passo 23</b> - incluir o campo image no banco de dados<br />
        - python manage.py makemigrations<br />
        - python manage.py migrate<br />
    </div>
</details>
<details> 
    <summary><strong>Deploy no Heroku</strong></summary>
    <br />
    <div>
        <p><b>Passo 24</b> - instalar o heroku cli<br />
        - Heroku: https://www.heroku.com/home<br />
        - verificar a versão: heroku --version<br />
        - logar: heroku login<br />
        <p><b>Passo 25</b> - criar um projeto dentro do heroku<br />
        - heroku create django-api-contacts<br />
        <p><b>Passo 26</b> - incluir a url dentro do arquivo settings.py<br />
        - ALLOWED_HOSTS = ['https://django-api-contacts.herokuapp.com/']<br />
        <p><b>Passo 27</b> - criar o arquivo Procfile<br />
        - dentro da pasta root do projeto<br />
        - para saber o nome do projeto: ROOT_URLCONF = 'contact.urls'<br />
        <p><b>Passo 28</b> - instalar pacotes para ajudar a configurar o deploy<br />
        - pip install django-heroku<br />
        - pip install gunicorn<br />
        caso aconteça erro de instalação no linux<br />
        - sudo apt-get install libpq-dev<br />
        - sudo apt-get install libpq-dev python-dev<br />
        <p><b>Passo 29</b> - criar o arquivo requirements.txt<br />
        - pip freeze > requirements.txt<br />
        <p><b>Passo 30</b> - subir a aplicação para o Heroku<br />
        - git push heroku master<br />
    </div>
</details>