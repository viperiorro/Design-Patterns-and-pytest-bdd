from pytest_bdd import given, when, then, parsers, scenario

from module_2_factory_method.factory import RoadLogistic, SeaLogistic, AirLogistic
from module_2_factory_method.transport import Transport

feature = 'transport_logistic.feature'


@scenario(feature, 'Factory creates appropriate transport types')
def test_factory():
    pass


@scenario(feature, 'Plan delivery using different transport types')
def test_plan_delivery():
    pass


@scenario(feature, 'All factories create only transports')
def test_all_factories():
    pass


logistic_classes = {
    "RoadLogistic": RoadLogistic,
    "SeaLogistic": SeaLogistic,
    "AirLogistic": AirLogistic
}


@given(parsers.parse('logistic "{logistic_type}"'), target_fixture="logistic")
def get_logistic(logistic_type):
    return logistic_classes[logistic_type]()


@given("all logistics", target_fixture="all_logistics")
def get_all_logistics():
    return [l() for l in logistic_classes.values()]


@when("using the logistic")
def using_logistic(logistic):
    return logistic


@when("using the logistics")
def using_logistics(all_logistics):
    return all_logistics


@then(parsers.parse('it should create transport "{transport_type}"'))
def created_transport(logistic, transport_type):
    transport = logistic.create_transport()
    assert type(transport).__name__ == transport_type


@when(parsers.parse("plan delivery to \"{destination}\""), target_fixture="planned_delivery")
def planned_delivery(logistic, destination, capsys):
    logistic.plan_delivery(destination)
    captured = capsys.readouterr()
    return captured.out.strip()


@then(parsers.parse("the output should be \"{message}\""))
def compare_output(planned_delivery, message):
    assert planned_delivery == message


@then("they should create only transports")
def validate_logistics_creates_transport(all_logistics):
    for logistic in all_logistics:
        transport = logistic.create_transport()
        assert isinstance(transport, Transport)
