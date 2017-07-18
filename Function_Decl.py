class Function_Decl(object):
    def __init__(self, name, body):
        self.name = name
        self.body = body
        print self.name + ' is stored with body.'

    def __init__(self, name):
        self.name = name
        self.body = []
        print self.name + ' is not stored with body.'

    def __init(self):
        self.name = ""
        self.body = []
        print 'Function init'
