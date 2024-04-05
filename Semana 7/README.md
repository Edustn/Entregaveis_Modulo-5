O seguinte sistema funciona primeiraemnte se o robô estiver desconectado do robô o usuário só poderá acessar a /log. Caso o robô esteja conectado o usuário terá acesso as demais rotas, como /print que demonstra somente que a rota está funcioando. Outra rota é /posicao que o usuário poderá checar qual a posição atual do sistema.
Ademais, outra rota é /mover que possibilita a movimentação do robô, onde os valores de x,y,z e r serão passados pela URL.

*Instalação para execução do sistema*

1 - Instale o venv, com o comando python -m venv venv

2- Isntale as dependências do requirements.txt no projeto, para isso faça o comando pip install -r .\requirements.txt

3 - Após isso execute o comando python .\main.py, pois esse é o código responsável por executar todo o sistema.

4- Para ter aos vários acessos as aplicações utilize a URL do seu navegador para executar os comandos.