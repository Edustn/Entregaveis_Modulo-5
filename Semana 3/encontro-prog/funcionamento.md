# Funcionamento do programa

Ao analisar o código presente no arquivo main.py da pasta src, observa-se que o mesmo utiliza o Typer para criar uma interface de linha de comando (CLI). A estrutura do código envolve a implementação de diversas funções, cada uma destinada a uma ação específica que o usuário pode escolher. Por exemplo, ao optar por mover o robô em um eixo específico, o usuário deve selecionar o eixo desejado e informar a distância de deslocamento.

A função "home" foi projetada para reposicionar o braço robótico na posição inicial predefinida. Já a função "ligar" ativa a ventosa do robô, enquanto a função "desligar" resulta no desativamento dessa peça.

Para executar o programa, utilize o terminal do Visual Studio Code e insira o seguinte comando: `python .\main.py "nome da função que deseja executar"`. É importante ressaltar que no trecho do código onde está `dobot = Dobot(port="COM9")`, a porta "COM9" deve ser ajustada conforme a porta COM correspondente ao seu computador.


