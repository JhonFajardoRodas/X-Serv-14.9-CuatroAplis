#!/usr/bin/python

import random


class aleat:
    def parse(self, request, rest):
        return None

    def process(self, parsedRequest):
        link = str(random.randrange(123456789))
        return ("200 OK", "<html><body><h1>Hello World!</h1>" + "<a href='" +
                link + "'>dame otra</a>" +
                "</body></html>")
