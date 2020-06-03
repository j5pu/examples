class A:
    def __init__(self, a):
        self.a = a
        print('A.a: ', self.a)

    def close(self):
        print('A.close()')
class B:
    def __init__(self, b):
        self.b = b
        print('B.b: ', self.b)

    def close(self):
        print('B.close()')
class C:
    def __init__(self, c):
        self.a = A('c')
        print('C.a: ', self.a)
        self.b = B('c')
        print('C.b: ', self.b)
        self.c = c
        print('C.c: ', self.c)
        print('self.a.close():', self.a.close())
    def close(self):
        print('C.close()')

a = A('a')
b = B('b')
c = C('c')

a.close()
b.close()
c.close()

response = a, b, c
response[0].close()
response[1].close()
response[2].close()

print(response)
class Response:
    def __init__(self, client, response, obj, code):
        self.client = client
        self.response = response
        self.obj = obj
        self.code = code

response = Response()

