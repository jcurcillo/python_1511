import pytest
from example_class import Dog

@pytest.fixture
def dog():
    dog = Dog('Buddy', 'Golden Retriever')
    return dog

#test Dog init

def test_dog_initialization(dog):
    assert dog.get_name() == 'Buddy'
    assert dog.get_breed() == 'Golden Retriever'
    assert dog._tricks == []

def test_dog_add_trick(dog):
    dog.add_trick('roll over')