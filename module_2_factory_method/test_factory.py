import unittest
from unittest.mock import patch
from io import StringIO
from factory import RoadLogistic, SeaLogistic, AirLogistic, Logistic
from transport import Truck, Ship, Airplane, Transport


class TestFactoryMethodPattern(unittest.TestCase):
    @patch('sys.stdout', new_callable=StringIO)
    def test_road_logistic_delivers_by_truck(self, mock_stdout):
        """Test the delivery method of the RoadLogistic factory."""
        logistic = RoadLogistic()
        logistic.plan_delivery("New York")

        self.assertEqual(mock_stdout.getvalue(), "Delivering by Truck to the destination: New York\n")

    @patch('sys.stdout', new_callable=StringIO)
    def test_sea_logistic_delivers_by_ship(self, mock_stdout):
        """Test the delivery method of the SeaLogistic factory."""
        logistic = SeaLogistic()
        logistic.plan_delivery("London")

        self.assertEqual(mock_stdout.getvalue(), "Delivering by Ship to the destination: London\n")

    @patch('sys.stdout', new_callable=StringIO)
    def test_air_logistic_delivers_by_airplane(self, mock_stdout):
        """Test the delivery method of the AirLogistic factory."""
        logistic = AirLogistic()
        logistic.plan_delivery("Paris")

        self.assertEqual(mock_stdout.getvalue(), "Delivering by Airplane to the destination: Paris\n")

    def test_transport_types(self):
        """Test if the factory methods create the correct transport types."""
        road_logistic = RoadLogistic()
        self.assertIsInstance(road_logistic.create_transport(), Truck)

        sea_logistic = SeaLogistic()
        self.assertIsInstance(sea_logistic.create_transport(), Ship)

        air_logistic = AirLogistic()
        self.assertIsInstance(air_logistic.create_transport(), Airplane)

    def test_switch_between_transport_types(self):
        """
        Test the flexibility of the Factory Method pattern
        to switch between transport types without changing code structure.
        """
        class NewLogistic(Logistic):
            def create_transport(self):
                return NewTransport()

        class NewTransport(Transport):
            def deliver(self, destination):
                print(f"Delivering by NewTransport to the destination: {destination}")


        logistic_plans = [
            {'logistic': RoadLogistic(), 'destination': 'New York'},
            {'logistic': SeaLogistic(), 'destination': 'London'},
            {'logistic': AirLogistic(), 'destination': 'Paris'},
            {'logistic': NewLogistic(), 'destination': 'Kyiv'}
        ]

        for plan in logistic_plans:
            logistic = plan['logistic']
            destination = plan['destination']
            with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
                logistic.plan_delivery(destination)
                expected_output = f"Delivering by {type(logistic.create_transport()).__name__} to the destination: {destination}\n"
                self.assertEqual(mock_stdout.getvalue(), expected_output)
