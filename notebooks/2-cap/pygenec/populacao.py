#!/usr/bin/env python
# -*- Coding: UTF-8 -*-

from numpy.random import randint
from numpy import argsort, unique


class Populacao:
    """
    Cria e avalia uma população

    Attributes
    ----------
    func_avaliacao: func
        Função que recebe um indivívudo como entrada e retorna um valor numérico
    total_genes: int
        Número inteiro que representa o tamanho da cadeia
    total_populacao: int
        Numéro inteiro que representa o número total de indivíduos na população

    Methods
    -------
    gerar_populacao: None
        Gera uma população aleatória
    avaliar: numpy.array
        Retorna os valores da população ordernados
    """

    def __init__(self, func_avaliacao, total_genes, total_populacao):
        self.func_avaliacao = func_avaliacao
        self.total_genes = total_genes
        self.total_populacao = total_populacao
        self.populacao = None

    def gerar_populacao(self):
        """Gera uma população aleatória"""

        self.populacao = randint(0, 2, size=(self.total_populacao,
                                             self.total_genes),
                                 dtype='b')

    def avaliar(self):
        """
        Avalia e ordena a população

        Returns
        -------
        numpy.array: Os valores da população ordenados
        """
        u, indices = unique(self.populacao,
                            return_inverse=True,
                            axis=0)

        valores = self.func_avaliacao(u)

        valores = valores[indices]

        ind = argsort(valores)

        self.populacao[:] = self.populacao[ind]

        return valores[ind]
