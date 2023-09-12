from module_2_factory_method.transport import Truck, Ship, Airplane


class Logistic:
    """
    Logistic is an abstract class representing the factory.
    It contains a factory method create_transport for creating Transport objects.
    The plan_delivery method uses the factory method to create and use a Transport object.
    """

    def create_transport(self):
        pass

    def plan_delivery(self, destination):
        transport = self.create_transport()
        transport.deliver(destination)


class RoadLogistic(Logistic):
    """
    RoadLogistic is a concrete factory for creating Truck Transport objects.
    """

    def create_transport(self):
        return Truck()


class SeaLogistic(Logistic):
    """
    SeaLogistic is a concrete factory for creating Ship Transport objects.
    """

    def create_transport(self):
        return Ship()


class AirLogistic(Logistic):
    """
    AirLogistic is a concrete factory for creating Airplane Transport objects.
    """

    def create_transport(self):
        return Airplane()