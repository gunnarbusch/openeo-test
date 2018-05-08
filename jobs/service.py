from nameko.rpc import rpc

class JobService:
    name = "job"

    @rpc
    def hello(self, name):
        return "Hello {0}!".format(name)