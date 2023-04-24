from src.models.dish import Dish  # noqa: F401, E261, E501
from src.models.ingredient import Ingredient, Restriction
from pytest import raises


# Req 2
def test_dish():
    panqueca_frango_data = {"name": "Panqueca de Frango", "price": 15}
    panqueca_frango_str = (
        f"Dish('{panqueca_frango_data['name']}'"
        + f", R${panqueca_frango_data['price']:.2f})"
    )

    panqueca_frango = Dish(panqueca_frango_data["name"], 15)
    panqueca_frango2 = Dish(panqueca_frango_data["name"], 15)
    file_salmao = Dish("Filé de Salmão", 60)
    frango = Ingredient("frango")
    ovo = Ingredient("ovo")

    panqueca_frango.add_ingredient_dependency(frango, 1)
    panqueca_frango.add_ingredient_dependency(ovo, 2)

    assert panqueca_frango.name == panqueca_frango_data["name"]

    assert hash(panqueca_frango) == hash(panqueca_frango2)
    assert hash(panqueca_frango) != hash(file_salmao)

    assert panqueca_frango == panqueca_frango2

    assert repr(panqueca_frango) == panqueca_frango_str

    with raises(TypeError, match="Dish price must be float."):
        Dish(panqueca_frango_data["name"], "15")
    with raises(ValueError, match="Dish price must be greater then zero."):
        Dish(panqueca_frango_data["name"], 0)

    assert panqueca_frango.recipe.get(frango) == 1
    assert panqueca_frango.recipe.get(ovo) == 2

    assert panqueca_frango.get_restrictions() == {
        Restriction.ANIMAL_MEAT,
        Restriction.ANIMAL_DERIVED,
    }

    assert panqueca_frango.get_ingredients() == {frango, ovo}
