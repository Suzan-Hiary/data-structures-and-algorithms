from code_challenges.stack_queue_animal_shelter.fifo_animal_shelter import AnimalShelter




def test_add_animal():
    #input
    animal=AnimalShelter()
    animal.enqueue('cat')

    #ouytput
    expected='cat'
    actul=animal.front.data
    assert expected==actul

def test_add_animals():
    #input
    animal=AnimalShelter()
    animal.enqueue('cat')
    animal.enqueue('dog')
    animal.enqueue('dog')

    #ouytput
    expected='cat'
    actul=animal.front.data
    assert expected==actul


def test_remove_animals():
    #input
    animal=AnimalShelter()
    animal.enqueue('cat')
    animal.enqueue('dog')
   

    #ouytput
    expected='cat'
    actul= animal.dequeue('cat')
    assert expected==actul

def test_remove_animals2():
    #input
    animal=AnimalShelter()
    animal.enqueue('cat')
    animal.enqueue('dog')
    #ouytput
    expected='dog'
    actul= animal.dequeue('dog')
    assert expected==actul


def test_remove_animals4():
    #input
    animal=AnimalShelter()
    animal.enqueue('cat')
    animal.enqueue('dog')
    animal.enqueue('dog')
    #ouytput
    expected=None
    actul= animal.dequeue('horse')
    assert expected==actul