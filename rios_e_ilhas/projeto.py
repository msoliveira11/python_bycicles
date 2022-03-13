#!/usr/bin/env python
# coding: utf-8

# ## Projeto Módulo 3
# 
# Você irá receber uma lista bi-dimensional com altura e largura não necessáriamente iguais contendo apenas 0's e 1's. Cada 1 representa um pedaço de rio, enquanto os 0's representam terra. Rios são compostos por 1's adjacentes horizontalmente ou verticalmente (mas não diagonalmente). O número de 1's adjacentes representa o tamanho do rio.
# 
# Note que o rio pode fazer curvas, isto é, rios podem ter formato de L ou até mesmo de cruz e são considerados um rio só.
# 
# Crie um algoritmo que receba esta lista bi-dimensional e retorne uma lista com os tamanhos dos rios dentro dessa estrutura, os tamanhos de rios dentro da lista resposta não precisam ter uma ordem específica.
# 
# **Exemplo de entrada:**
# 
# ```python
# matrix = [
#     [1, 0, 0, 1, 0],
#     [1, 0, 1, 0, 0],
#     [0, 0, 1, 0, 1],
#     [1, 0, 1, 0, 1],
#     [1, 0, 1, 1, 0],
# ]
# ```
# 
# **Saída esperada:**
# 
# ```python
# [1, 2, 2, 2, 5] # Note que os números poderiam estar em qualquer ordem dentro da lista
# ```
# 
# podemos visualizar os rios claramente na seguinte estrutura:
# 
# ```python
# [1,  ,  , 1,  ]
# [1,  , 1,  ,  ]
# [ ,  , 1,  , 1]
# [1,  , 1,  , 1]
# [1,  , 1, 1,  ]
# ```

# ## Desafio: Implementar uma função que conta a quantidade de ilhas

# In[ ]:


matrix = [
    [1, 0, 0, 1, 0],
    [1, 0, 1, 0, 0],
    [0, 0, 1, 0, 1],
    [1, 0, 1, 0, 1],
    [1, 0, 1, 1, 0],
]


# In[ ]:


matrix

