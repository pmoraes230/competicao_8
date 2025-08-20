## Music Hall

Sistema responsável pela gerencia e e venda de eventos que irão acontecer na casa de show de Senac Music Hall. O sistema vem como um facilitador do dia a dia dos funcionários desta casa, visando dar mais agilidade e organização em trabalhos relacionados a venda e emissão de ingressos para os shows, cadastros de novos eventos e setores relacionados ao evento e um dashboard com gráficos o funcionários de perfil administrador saber o andamento de venda de cada evento. Este sistema é exclusivamente dos funcionários da casa e os clientes finais não terão acesso.

## Funcionalidades
- Criação, apagar e atualizar: Eventos, setores e funcionários.
- Cadastrar clientes para venda de ingresso.
- listar eventos em destaque em tela inicial.
- Tela de validação de ingressos para entrada no show.
- Tela de dashboard com gráficos mostrando o andamento de venda de ingressos para cada setor.
- Telas personalizadas de acordo com o perfil de usuário de cada funcionário.

## Tecnologias usadas
As tecnologias usadas neste projeto são:
- Django/Python (Framework web)
- MySql (Banco de dados)
- Matplotlib (Criação de gráficos)
- Pdfkit (Criação e download de ingressos) / [wkhtmltopdf (Plugin binário para rodar o pdfkit)](https://wkhtmltopdf.org/downloads.html)
- Python-dotenv (Leitor de arquivos `.env`)

## Pré-requitos para rodar o projeto
Para rodar o projeto localmente em sua máquina é necessárias certos passos.

Instalar o python em sua máquina ( Urls para o site do python )
```bash
    https://www.python.org/downloads/ 
```

Criar o ambiente virtual em sua máquina (inserir código no terminal)
```bash
    virtualenv venv
```

Ativar ambiente virtual (inserir código no terminal)
```bash
    .\venv\Scripts\activate
```

Instalar arquivo requiments.txt com pacotes necessários para iniciação de projeto em sua máquina (inserir código no terminal)
```bash
    pip install -r requiments.txt
```

Rodar projeto localmente (inserir código no terminal)
```bash
    py manage.py runserver
```

## Protótipo figma

[Protótipo de telas figma](https://www.figma.com/proto/z4BZ5q7jon5Jx7oXNqXEig/music-hall?node-id=1-114&t=S3G9LkCVZUDul6mw-1&scaling=scale-down&content-scaling=fixed&page-id=0%3A1&starting-point-node-id=1%3A114&show-proto-sidebar=1)