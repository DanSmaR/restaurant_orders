from src.models.ingredient import Ingredient, Restriction  # noqa: F401, E261, E501


# Req 1 - initial commit
def test_ingredient():
    farinha = Ingredient("farinha")
    farinha2 = Ingredient("farinha")
    ovo = Ingredient("ovo")

    farinha_hash = hash(farinha)
    assert farinha_hash == hash(farinha2)
    assert hash(ovo) != farinha_hash

    assert farinha2 == farinha
    assert ovo != farinha

    assert repr(farinha) == "Ingredient('farinha')"

    assert farinha.name == "farinha"
    assert farinha2.name == farinha.name

    assert farinha.restrictions == {Restriction.GLUTEN}
    assert ovo.restrictions == {Restriction.ANIMAL_DERIVED}
