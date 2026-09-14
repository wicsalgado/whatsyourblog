# What's Your Blog?

## Sobre o projeto

O What's Your Blog? é um portal de blogs e notícias voltado para conteúdos de entretenimento, cultura pop e outros temas de interesse dos usuários.

A proposta do projeto é permitir que cada usuário tenha seu próprio espaço dentro da plataforma para produzir e publicar conteúdos sobre os assuntos pelos quais se interessa. O perfil do usuário funciona como um blog, permitindo a criação de publicações, organização por categorias e tags e interação por meio de comentários.

Entre os temas que podem ser abordados estão filmes, séries, música, artistas, fandoms, jogos, livros, anime, cultura pop, nostalgia, curiosidades, histórias e outros assuntos relacionados ao entretenimento.

A plataforma também possui um processo de análise editorial. As publicações criadas pelos usuários passam por uma etapa de análise antes de serem disponibilizadas publicamente. Dessa forma, o conteúdo publicado oficialmente na plataforma passa por uma aprovação.

Além das publicações, os usuários podem sugerir novos temas para a plataforma. Essas sugestões também passam por análise antes de se tornarem categorias oficiais.

## Inspirações

A ideia do What's Your Blog? surgiu a partir da combinação de diferentes referências de sites, revistas e comunidades que possuem ou possuíam uma forte relação com produção de conteúdo e interesses pessoais.

Uma das principais referências é a Revista Recreio, principalmente a estética e a forma de apresentação de conteúdos voltados ao público jovem entre os anos de 2013 e 2015. A intenção é trazer para o projeto uma sensação de descoberta de conteúdos e temas variados.

Também foram utilizadas como inspiração plataformas e comunidades como Tumblr, MySpace, We Heart It e Blogspot. Essas plataformas influenciaram principalmente a ideia de cada usuário possuir um espaço próprio para publicar conteúdos relacionados aos seus interesses.

Outra referência é a revista Capricho, principalmente pela relação com cultura pop, música, artistas, filmes, séries e outros assuntos de entretenimento.

O projeto não tem como objetivo reproduzir nenhuma dessas plataformas. As referências foram utilizadas para definir a proposta, a organização dos conteúdos e parte da identidade visual do What's Your Blog?.

## Principais funcionalidades

Cadastro e login de usuários.

Criação e edição de perfil.

Escolha de uma categoria principal para o perfil.

Escolha de até três tags relacionadas ao perfil.

Criação de publicações.

Edição de publicações.

Classificação das publicações por categoria e tags.

Sistema de comentários.

Pesquisa de conteúdos.

Visualização de perfis e blogs.

Sugestão de novos temas.

Análise editorial das publicações.

Aprovação ou rejeição de publicações.

Área administrativa para gerenciamento do sistema.

## Categorias e tags

As categorias representam os temas mais amplos existentes na plataforma. Alguns exemplos são:

Filmes

Música

Cultura Pop

Séries

Anime

Gaming

Retro

Teatro

Livros

As tags representam assuntos mais específicos dentro ou relacionados a esses temas.

Por exemplo, um perfil pode ter a categoria principal "Filmes" e utilizar as tags "Terror", "Suspense" e "Slasher".

As tags não pertencem exclusivamente a uma categoria. Elas podem ser utilizadas em diferentes publicações e perfis quando fizer sentido.

Os perfis possuem no máximo três tags, enquanto as publicações podem utilizar uma quantidade maior de tags.

## Fluxo de publicação

As publicações possuem um fluxo de análise antes de serem disponibilizadas publicamente.

RASCUNHO

O usuário está criando ou editando a publicação. O conteúdo ainda não foi enviado para análise.

EM ANÁLISE

A publicação foi enviada para a análise editorial e aguarda uma decisão.

PUBLICADO

A publicação foi aprovada e está disponível publicamente no site.

REJEITADO

A publicação não foi aprovada. O usuário pode realizar alterações e enviar novamente para análise.

O fluxo principal é:

RASCUNHO -> EM ANÁLISE -> PUBLICADO

ou

RASCUNHO -> EM ANÁLISE -> REJEITADO -> RASCUNHO

Somente publicações com o status PUBLICADO ficam disponíveis para os demais usuários e podem receber comentários.

## Sugestão de novos temas

Os usuários podem sugerir novos temas que ainda não existem na plataforma.

A sugestão passa por uma análise editorial e pode ser aprovada ou rejeitada.

O objetivo desse sistema é permitir que a plataforma cresça de acordo com os interesses dos usuários, mantendo ao mesmo tempo uma organização dos temas existentes.

## Tecnologias utilizadas

Python

Django

Django Templates

HTML5

CSS3

JavaScript

MySQL 8.4

Django ORM

Docker

Docker Compose

Pillow

WhiteNoise

Gunicorn

Git e GitHub

## Estrutura do projeto

O projeto utiliza uma arquitetura monolítica baseada em Django.

As principais aplicações do sistema são:

users

Responsável pelo cadastro, autenticação e perfis dos usuários.

posts

Responsável pelas publicações, categorias e tags.

comments

Responsável pelos comentários das publicações.

A pasta principal do projeto Django é:

portal/

## Requisitos

Para executar o projeto localmente é necessário ter instalado:

Python 3.12 ou superior

Git

Docker Desktop

O Docker Desktop deve estar aberto durante a execução do banco de dados.

## Instalação

Clone o repositório:

git clone https://github.com/wicsalgado/whatsyourblog.git

Entre na pasta do projeto:

cd whatsyourblog

Crie o ambiente virtual:

python -m venv venv

Ative o ambiente virtual no Windows PowerShell:

.\venv\Scripts\Activate.ps1

Instale as dependências:

pip install -r requirements.txt

## Configuração do ambiente

O projeto utiliza variáveis de ambiente para as configurações do banco de dados e do Django.

Na raiz do projeto existe o arquivo:

.env.example

Crie uma cópia desse arquivo com o nome:

.env

No Windows PowerShell:

Copy-Item .env.example .env

Depois, abra o arquivo .env e preencha as informações necessárias.

O arquivo .env não deve ser enviado para o GitHub, pois contém informações de configuração que não devem ser compartilhadas.

## Banco de dados

O banco de dados utilizado no projeto é o MySQL 8.4, executado através do Docker.

Com o Docker Desktop aberto, execute:

docker compose up -d

Para verificar se o container está funcionando:

docker ps

O container utilizado pelo projeto é:

portal_mysql

Depois de iniciar o banco, execute as migrações:

python manage.py migrate

## Criar usuário administrador

Para criar um usuário administrador do Django:

python manage.py createsuperuser

O comando solicitará nome de usuário, e-mail e senha.

Esse usuário poderá acessar a área administrativa através de:

/admin/

## Executar o projeto

Depois de configurar o ambiente e iniciar o banco de dados, execute:

python manage.py runserver

O projeto ficará disponível localmente em:

http://127.0.0.1:8000/

A área administrativa pode ser acessada em:

http://127.0.0.1:8000/admin/

## Arquivos que não devem ser enviados para o GitHub

Alguns arquivos e pastas são gerados localmente ou possuem informações privadas e, por isso, estão no .gitignore.

.env

venv/

__pycache__/

*.pyc

db.sqlite3

media/

staticfiles/

O banco de dados MySQL também não é armazenado no GitHub. Em uma nova instalação, as tabelas são criadas novamente através das migrações do Django.

## Desenvolvimento em outro computador

Para executar o projeto em outro computador, é necessário clonar o repositório, criar um novo ambiente virtual, instalar as dependências, configurar o arquivo .env, iniciar o MySQL pelo Docker e executar as migrações.

O banco de dados utilizado no computador original não é copiado automaticamente para o novo computador. Portanto, uma nova instalação terá o banco vazio até que sejam cadastrados usuários, categorias, tags e demais dados.

Da mesma forma, arquivos enviados para a pasta media/ não são versionados no GitHub.

## Comandos principais

Criar ambiente virtual:

python -m venv venv

Ativar ambiente virtual:

.\venv\Scripts\Activate.ps1

Instalar dependências:

pip install -r requirements.txt

Iniciar banco de dados:

docker compose up -d

Parar banco de dados:

docker compose down

Executar migrações:

python manage.py migrate

Criar migrações:

python manage.py makemigrations

Criar usuário administrador:

python manage.py createsuperuser

Executar o servidor:

python manage.py runserver

Verificar o projeto:

python manage.py check

Coletar arquivos estáticos:

python manage.py collectstatic