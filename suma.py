#!/usr/bin/python

import webapp
import random


class sumador:

    def parse(self, request, rest):
        try:
            operacion = rest.split("/")
            if len(operacion) != 2:
                return None
            numero1 = int(operacion[0])
            numero2 = int(operacion[1])
        except ValueError:
            return None
        return (numero1, numero2)

    def process(self, parsedRequest):
        if not parsedRequest:
            return ("404 Bad Request", "<html><body><h1>Enter a number!</h1>" +
                    "</body></html>")
        num1 = parsedRequest[0]
        num2 = parsedRequest[1]
        resultado = num1 + num2
        return ("200 OK", "<html><body><h1> " + str(num1) + " + " + str(num2) +
                " = " + str(resultado) +
                "</body></html>")
