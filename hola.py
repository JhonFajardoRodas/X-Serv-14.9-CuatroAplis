
#!/usr/bin/python


class hola:
    def parse(self, request, rest):
        return None

    def process(self, parsedRequest):
        return ("200 OK", "<html><body><h1>Hello !!</h1>" +
                "</body></html>")


class adios:
    def parse(self, request, rest):
        return None

    def process(self, parsedRequest):
        return ("200 OK", "<html><body><h1>Good bye!!</h1>" +
                "</body></html>")
