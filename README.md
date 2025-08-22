## Senac Music Hall
O sistema Senac Music hall é um sistema de gerenciamento de evento para a casa de show de mesmo nome que fica na cidade de Brazili DF. Ele tem a responsabilidade para o gerenciamento, venda e cadastro de eventos, clientes e usuários, assim facilitando o dia a dia durante o trabalho, este sistema é exclusivamente para funcionários e sem acesso do cliente final.

## Funcionalidades de cada perfil de acesso
- Administrado (Usuário com acesso total ao sistema)
- Vendedor (Usuário que somente vende tem a função de vender os ingressos dos shows aos clientes finais)
- Validador (Usuário que tem a função de validar o ingresso do cliente antes dele participar e/ou assistir ao evento)

## Tecnologias utilizadas
- Python (Linguagem de programação usada para o projeto)
- Django (Framework python usado para criar a página web)
- MySql (Banco de dados utilizado para armazenamentos das informações precisas no site)
- Matplotlib (Criar os gráficos detalhados de dashboard)
- Pdf/kit (Exportar os ingressos de cada cliente após a conclusão das vendas)

## Pré-requisitos
Para o sistema rodar localmente em sua máquina se faz necessário seguir os passos de instalação abaixo:

Instalar o Python mais recente em sua máquina:
```
    https://www.python.org/downloads/
```

Clonar o repositório em sua máquina local
```
    git clone https://github.com/pmoraes230/competicao_8.git
```

Criar ambiente virtual em seu projeto (comando via cmd ou terminal do vs-code)
```
    virtualenv venv
```

Ativar ambiente virtual (comando via cmd ou terminal do vs-code)
```
    \venv\Scripts\activate
```

Instalar pacotes do arquivos requirements.txt (comando via cmd ou terminal do vs-code)
```
    pip freeze > requirements.txt
```

Rodar localmente o projeto (comando via cmd ou terminal do vs-code)
```
    py .\manage.py runserver 0.0.0.0:8000
```