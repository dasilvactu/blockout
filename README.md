# blockout

## Desafio para resolver o problema disposto em  https://www.codingame.com/training/hard/blockout

Foi proposta uma heurística que consiste em avaliar qual a melhor jogada baseada na maior profundidade que a peça pode ir.

Para isso, as posições em relação aos eixos x e z são variadas, e a maior profundidade em cada posição é avaliada, retornando a jogada que obteve a maior profundidade.

No laço principal do programa, cada rotação é verificada usando a heurística proposta, e a rotação com o melhor posição para descida é a retornada como a melhor jogada.

Para facilitar a representação do ambiente e da peça, a representação foi alterada para a forma matricial, representando exatamente, por nível, quais posições estão ocupadas ou não. Isso fez com que avaliar os contatos entre a peça e o pit seja feita a partir de uma soma matricial e a verificação da existência de um número 2 na matriz resultante.

ps: O que faltou desenvolver no código foi a definição dos limites de translado da peça, para que ela respeite sempre os limites do pit.