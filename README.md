# Challenge-SSYS
Desafio técnico do processo seletivo da SSYS. 

Nesse desafio, foi desenvolvida uma API em python com o framework Django.

Etapa cumprida: 
- API with employees CRUD:
    - GET: /employees/ (employee list)
    - POST: /employees/ (employee create)
    - UPDATE /employees/ID/ (employee update)
    - DELETE /employees/ID/ (employee delete)
    - GET /employees/ID/ (employee detail)

- Persist data in a database
- Use authentication to access

Etapa não cumprida:
- API with reports:
    - GET /reports/employees/salary/ (salary report)
    - GET /reports/employees/age/ (age report)

Bônus² (opcional): Foi realizado o deploy da aplicação com Heroku, segue o link de acesso: 
https://apiemployees.herokuapp.com/

- Observação: 
    - Para testar a aplicação, clone o repositório e instale todas as dependências do django no seu ambiente virtual, como descrito em requirements.txt. 
    - Nessa aplicação, utilizou-se também o Insomnia para testar o funcionamento da API e gerar o token de acesso.Assim, no método POST, utilizou-se a rota localhost:8000/token/ com a criação de uma variável JSON, descrita no arquivo acess_token.txt. 
    - Após gerar o token, foi possível utilizar o "acess" no método GET, contendo no Header: 
        - Authorization 
        - Bearer "acess"