"""
Proxy, in general terms, is a system that intermediates between the seeker and provider.
Seeker is the one that makes the request, and provider delivers the resources in response to the request.
In the web world, we can relate this to a proxy server.
The clients (users in the World Wide Web), when they make a request to the website, first connect to a proxy server asking for resources such as a web page.
The proxy server internally evaluates this request, sends it to an appropriate server, and gets back the response, which is then delivered to the client.
Thus, a proxy server encapsulates requests, enables privacy, and works well in distributed architectures.
In the context of design patterns, Proxy is a class that acts as an interface to real objects.
Objects can be of several types such as network connections, large objects in memory and file, among others.
In short, Proxy is a wrapper or agent object that wraps the real serving object.
Proxy could provide additional functionality to the object that it wraps and doesn't change the object's code.
The main intention of the Proxy pattern is to provide a surrogate or placeholder for another object in order
to control access to a real object.

The following Python code implements this scenario where the Actor is the Proxy.
The Agent object is used to find out if the Actor is busy.
If the Actor is busy, the Actor().occupied() method is called and if the Actor is not busy, the Actor(). available() method gets returned.
"""

class Actor(object):
    def __init__(self):
        self.isBusy = False
    def occupied(self):
        self.isBusy = True
        print(type(self).__name__ , "is occupied with current movie")
    def available(self):
        self.isBusy = False
        print(type(self).__name__ , "is free for the movie")
    def getStatus(self):
        return self.isBusy

class Agent(object):
    def __init__(self):
        self.principal = None
    def work(self):
        self.actor = Actor()
        if self.actor.getStatus():
            self.actor.occupied()
        else:
            self.actor.available()


if __name__ == '__main__':
    r = Agent()
    r.work()
