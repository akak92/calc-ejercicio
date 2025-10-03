from typing import Union
import logging

logger = logging.getLogger(__name__)

class Calculadora:
    """
    Calculadora básica para operaciones aritméticas.

    Métodos
    -------
    suma(a, b)
        Retorna la suma de a y b.
    resta(a, b)
        Retorna la resta de a y b.
    producto(a, b)
        Retorna el producto de a y b.
    division(a, b)
        Retorna la división de a entre b.
    """

    def suma(self, a: Union[int, float], b: Union[int, float]) -> Union[int, float]:
        """
        Suma dos números.

        Parameters
        ----------
        a : int or float
            Primer sumando.
        b : int or float
            Segundo sumando.

        Returns
        -------
        int or float
            Resultado de la suma.

        Raises
        ------
        TypeError
            Si los argumentos no son numéricos.
        """
        if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
            logger.error("Los argumentos deben ser numéricos.")
            raise TypeError("Los argumentos deben ser numéricos.")
        return a + b

    def resta(self, a: Union[int, float], b: Union[int, float]) -> Union[int, float]:
        """
        Resta dos números.

        Parameters
        ----------
        a : int or float
            Minuendo.
        b : int or float
            Sustraendo.

        Returns
        -------
        int or float
            Resultado de la resta.

        Raises
        ------
        TypeError
            Si los argumentos no son numéricos.
        """
        if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
            logger.error("Los argumentos deben ser numéricos.")
            raise TypeError("Los argumentos deben ser numéricos.")
        return a - b

    def producto(self, a: Union[int, float], b: Union[int, float]) -> Union[int, float]:
        """
        Multiplica dos números.

        Parameters
        ----------
        a : int or float
            Primer factor.
        b : int or float
            Segundo factor.

        Returns
        -------
        int or float
            Resultado del producto.

        Raises
        ------
        TypeError
            Si los argumentos no son numéricos.
        """
        if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
            logger.error("Los argumentos deben ser numéricos.")
            raise TypeError("Los argumentos deben ser numéricos.")
        return a * b

    def division(self, a: Union[int, float], b: Union[int, float]) -> float:
        """
        Divide dos números.

        Parameters
        ----------
        a : int or float
            Dividendo.
        b : int or float
            Divisor.

        Returns
        -------
        float
            Resultado de la división.

        Raises
        ------
        TypeError
            Si los argumentos no son numéricos.
        ValueError
            Si el divisor es cero.
        """
        if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
            logger.error("Los argumentos deben ser numéricos.")
            raise TypeError("Los argumentos deben ser numéricos.")
        if b == 0:
            logger.error("No se puede dividir por cero.")
            raise ValueError("No se puede dividir por cero.")
        return a / b