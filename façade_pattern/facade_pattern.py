"""
The façade is generally referred to as the face of the building, especially an attractive one.
It can be also referred to as a behavior or appearance that gives a false idea
of someone's true feelings or situation.

When people walk past a façade, they can appreciate the exterior face but aren't aware of the
complexities of the structure within. This is how a façade pattern is used.

Façade hides the complexities of the internal system and provides an interface to the client
that can access the system in a very simplified way.

The following points will give us a better idea of Façade:
    • It is an interface that knows which subsystems are responsible for a request
    • It delegates the client's requests to the appropriate subsystem objects using composition

For example, if the client is looking for some work to be accomplished, it need not have to
go to individual subsystems but can simply contact the interface (Façade) that gets the work done.

Putting it in the Façade pattern perspective:
    • Client: It's you who need all the marriage preparations to be completed in time before the wedding.
      They should be top class and guests should love the celebrations.
    • Façade: The event manager who's responsible for talking to all the folks that need to work
      on specific arrangements such as food, and flower decorations, among others
    • Subsystems: They represent the systems that provide services such as catering,
      hotel management, and flower decorations
"""

class EventManager(object):
    def __init__(self):
        print("Event Manager:: Let me talk to the folks\n")
    def arrange(self):
        self.hotelier = Hotelier()
        self.hotelier.bookHotel()
        self.florist = Florist()
        self.florist.setFlowerRequirements()
        self.caterer = Caterer()
        self.caterer.setCuisine()
        self.musician = Musician()
        self.musician.setMusicType()

class Hotelier(object):
    def __init__(self):
        print("Arranging the Hotel for Marriage? --")
    def __isAvailable(self):
        print("Is the Hotel free for the event on given day?")
        return True
    def bookHotel(self):
        if self.__isAvailable():
            print("Registered the Booking\n\n")

class Florist(object):
    def __init__(self):
        print("Flower Decorations for the Event? --")
    def setFlowerRequirements(self):
        print("Carnations, Roses and Lilies would be used for Decorations\n\n")

class Caterer(object):
    def __init__(self):
        print("Food Arrangements for the Event --")
    def setCuisine(self):
        print("Chinese & Continental Cuisine to be served\n\n")

class Musician(object):
    def __init__(self):
        print("Musical Arrangements for the Marriage --")
    def setMusicType(self):
        print("Jazz and Classical will be played\n\n")

class You(object):
    def __init__(self):
        print("You:: Whoa! Marriage Arrangements??!!!")
    def askEventManager(self):
        print("You:: Let's Contact the Event Manager\n\n")
        em = EventManager()
        em.arrange()
    def __del__(self):
        print("You:: Thanks to Event Manager, all preparations done! Phew!")

you = You()
you.askEventManager()
