from classwork import Pokemon


def test_bulba():
    assert str(Pokemon("Bulbasaur", "grass")) == "Bulbasaur/grass"
