# saucedemo-automation

### Descrição

Serão realizados seis casos de teste para o e-commerce fictício usado para casos de estudo (https://www.saucedemo.com/). Os 5 casos de teste mapeados serão realizados utilizando Selenium WebDriver e Pytest. Mais detalhes de cada cenário abaixo 

### CT01 - Realizar o login de um usuário

Pré-condições: Sem pré-condições

Procedimento:

1- Inserir um usuário válido
2- Inserir sua senha correspondente
3- Clicar em "Login" 

Resultado esperado: Acesso ao e-commerce

### CT02 - Realizar o logout de um usuário

Pré-condições: Estar logado

Procedimento:

1- Clicar no menu hamburguer 
2- Clicar na opção "Logout"

Resultado esperado: Voltar para a página de login

### CT03 - Adicionar dois itens ao carrinho

Pré-condições: Estar logado

Procedimento:
1- Clicar no botão "Add to cart" do Sauce Labs Backpack
2- Clicar no botão "Add to cart" do Sauce Labs Bike Light
3- Clicar no ícone de carrinho

Resultado esperado: Os dois inseridos estarão visíveis na página do carrinho

### CT04 - Remover um item do carrinho

Pré-condições: 

1- Estar logado
2- Ter pelo menos um item no carrinho 
3- Estar na página do carrinho

Procedimento:
1- Clicar em "Remove"

Resultado esperado: a página do carrinho ficar vazia

### CT05 - Realizar o fluxo completo de compra

Pré-condições: Estar logado

1- Inserir um item no carrinho 
2- Clicar no ícone do carrinho 
3- Clicar em "Checkout"
4- Inserir o primeiro nome do cliente
5- Inserir o último nome do cliente
6- Inserir o código postal 
7- Clicar em "Continue"
8- Clicar em "Finish"

Resultado esperado: Mensagem de sucesso
