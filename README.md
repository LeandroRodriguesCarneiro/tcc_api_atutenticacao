# API de Autenticação - TCC

Esta API foi desenvolvida para suprir a necessidade de autenticação em uma arquitetura de microserviços voltada para um agente de Inteligência Artificial (IA). Ela garante que apenas usuários autenticados possam acessar o sistema e inserir documentos na base de dados (Banco Vetorial), reforçando a segurança do ambiente.

A API gera tokens JWT exclusivos para autenticação e renovação. Quando um novo token é gerado, o token anterior é invalidado automaticamente, evitando sessões múltiplas e aumentando a segurança.

## Tecnologias Utilizadas

- **Python** com o framework **FastAPI** para desenvolvimento rápido e eficiente da API REST.
- **PostgreSQL** como banco de dados relacional para armazenamento seguro e consistente de dados de usuários e sessões.
- **Docker** para containerização, garantindo ambientes controlados e consistentes para desenvolvimento, teste e produção.

## Funcionalidades Principais

- Registro e autenticação de usuários.
- Geração, validação e renovação de tokens JWT.
- Controle de sessões com invalidação de tokens antigos.
- Integração segura com outros microserviços do sistema, permitindo um fluxo confiável de autenticação.

## Como Utilizar
1. Buildar a imagem docker:
   
```bash
docker build -t tcc_api_autenticacao:latest .
```


2. **Gerar chave secreta:**

   - **No Linux:**
     
     - Base64, 32 bytes (256 bits):
     
       ```
       openssl rand -base64 32
       ```

     - Ou (sem OpenSSL):

       ```
       head -c 32 /dev/urandom | base64
       ```

   - **No Windows (PowerShell):**

     ```
     $bytes = New-Object byte[] 32
     [System.Security.Cryptography.RandomNumberGenerator]::Create().GetBytes($bytes)
     [Convert]::ToBase64String($bytes)
     ```

3. **Rodar a imagem Docker (substitua pelos seus dados):**


```       
  docker run -d -e SECRET_KEY="Colar aqui a chave gerada anteriormente" -e ALGORITHM="HS256" -e DB_HOST="Colar aqui o host do seu banco postgre" -e DB_PORT="5432" -e DB_USER="Seu usuário do banco" -e DB_PSW="Sua senha do banco de dados" -e     DB_DATABASE="Nome do seu banco de dados" -p 8000:8000 tcc_api_autenticacao:latest
```

4. **Criar um usuário:**

   
Precisa criar o primeiro usuário da aplicação para isso podemos usar um comando ao abrir o container execute o comando a baixo:
```
  python -m app.start_user 
```

5. Acesse a documentação interativa da API (Swagger UI) navegando para `http://localhost:8000/docs`.

## Importância para o Projeto

Esta API é um componente crítico dentro da arquitetura de microserviços do projeto, garantindo a segurança e integridade no acesso ao sistema de IA. Sem um mecanismo robusto de autenticação, o sistema ficaria vulnerável a acessos não autorizados, comprometendo a confiabilidade e a privacidade dos dados.

## Desenvolvimento Futuro

- Implementação de autenticação multifator (MFA).
- Integração com provedores externos de identidade (OAuth, OpenID Connect).
- Monitoramento e logging avançado de eventos de autenticação.

## Contatos e Contribuições

Contribuições são bem-vindas! Para sugestões, melhorias ou relatórios de bug, abra uma issue ou envie um pull request.

Leandro Rodrigues Carneiro  
[GitHub](https://github.com/LeandroRodriguesCarneiro) | Contato: leandrorodrigues131531@gmail.com

