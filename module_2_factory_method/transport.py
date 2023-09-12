from abc import ABC, abstractmethod

class Transport(ABC):
    """
    The Transport class is an abstract base class that defines the interface
    for various transport methods. Subclasses should implement the deliver method.
    """

    @abstractmethod
    def deliver(self, destination):
        pass


class Truck(Transport):
    """
    The Truck class is a concrete implementation of the Transport interface
    for delivering goods by truck.
    """

    def deliver(self, destination):
        print(f"Delivering by Truck to the destination: {destination}")


class Ship(Transport):
    """
    The Ship class is a concrete implementation of the Transport interface
    for delivering goods by ship.
    """

    def deliver(self, destination):
        print(f"Delivering by Ship to the destination: {destination}")


class Airplane(Transport):
    """
    The Airplane class is a concrete implementation of the Transport interface
    for delivering goods by air.
    """

    def deliver(self, destination):
        print(f"Delivering by Airplane to the destination: {destination}")
