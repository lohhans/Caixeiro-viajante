# Problema bitônico euclidiano do caixeiro-viajante

Implementação do *problema euclidiano bitônico do caixeiro-viajante* para a disciplina de "[Projeto e Análise de Algoritmos][PAA]", no curso de [Ciência da Computação na Universidade Federal Rural de Pernambuco - Unidade Acadêmica de Garanhuns][UFRPE]. Estruturas desenvolvidas conforme orientação do [Prof. Tiago B. A. de Carvalho][professor], atividade retirada do livro "[Algoritmos: Teoria e Prática][livro]".

## ***15.1 Problema euclidiano bitônico do caixeiro-viajante:***

O ***problema euclidiano do caixeiro-viajante*** é o problema de determinar o percurso fechado mais curto que conecta um dado conjunto de *n* pontos no plano. A Figura 15.9(a) mostra a solução para um problema de 7 pontos. O problema geral é NP-completo, e então se considera que sua solução exige mais do que o tempo polinomial (ver Capítulo 34).

J. L. Bentley sugeriu que simplificássemos o problema restringindo nossa atenção a ***percursos bitônicos***, isto é, percursos que começam no ponto mais à esquerda, seguem estritamente da esquerda para a direita até o ponto da extremidade direita, e depois seguem estritamente da direita para esquerda, voltando ao ponto de partida. A Figura 15.9(b) mostra o percurso bitônico mais curto dos mesmos 7 pontos. Nesse caso, é possível um algoritmo de tempo polinomial.

Descreva um algoritmo de tempo O(n²) para determinar um percurso bitônico ótimo. Considere por hipótese que não existem dois pontos com a mesma coordenada *x*. *(Sugestão: Desloque-se da esquerda para a direita, mantendo possibilidades ótimas para as duas partes do percurso.)*

<p align="center">
  <img src="https://github.com/lohhans/Caixeiro-viajante/blob/master/images/figura.png?raw=true?" alt="Figura 15.9"/>
</p>

<p align="center">
    <sub>(Imagem retirada do livro "[Algoritmos: Teoria e Prática][livro]")</sub>
</p>

**Autores:**

[![Antônio A. S. N.](https://avatars1.githubusercontent.com/u/33501786?s=64&v=4)](https://github.com/AntonioAdelino) |  [![Armstrong L. M. G. Q.](https://avatars0.githubusercontent.com/u/30741312?s=64&v=4)](https://github.com/lohhans)
|-------------------|-------------------|
| Antônio A. S. N. | Armstrong L. M. G. Q. |
| [@AntonioAdelino](https://github.com/AntonioAdelino) | [@lohhans](https://github.com/lohhans) |


<!-- Links -->

[PAA]: https://sites.google.com/site/tiagoufrpe/home/projeto-e-analise-de-algoritmos-2018-2
[UFRPE]: http://bcc.uag.ufrpe.br/~portal/
[professor]: https://sites.google.com/site/tiagoufrpe/
[livro]: https://g.co/kgs/gA1ukF
[Problema]: https://github.com/lohhans/MinesweeperProlog#english-below
