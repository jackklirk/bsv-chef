import pytest
from unittest.mock import MagicMock, patch
from src.controllers.recipecontroller import RecipeController
from src.static.diets import Diet

@pytest.mark.unit
def test_id1_get_recipe():
    mockedDAO = MagicMock()
    with patch('src.controllers.recipecontroller.RecipeController.get_readiness_of_recipes', autospec=True) as mocked_get_readiness_of_recipes:
        mocked_get_readiness_of_recipes.return_value = {}
        diet = Diet.VEGAN
        take_best = False
        rc = RecipeController(items_dao=mockedDAO)
        
        assert rc.get_recipe(diet, take_best) == None

@pytest.mark.unit
def test_id2_get_recipe():
    mockedDAO = MagicMock()
    with patch('src.controllers.recipecontroller.RecipeController.get_readiness_of_recipes', autospec=True) as mocked_get_readiness_of_recipes:
        mocked_get_readiness_of_recipes.return_value = {}
        diet = Diet.VEGAN
        take_best = True
        rc = RecipeController(items_dao=mockedDAO)
        
        assert rc.get_recipe(diet, take_best) == None

@pytest.mark.unit
def test_id3_get_recipe():
    mockedDAO = MagicMock()
    get_readiness_of_recipes_return = {"Banana Bread": 1}
    expected_result = "Banana Bread"
    with patch('src.controllers.recipecontroller.RecipeController.get_readiness_of_recipes', autospec=True) as mocked_get_readiness_of_recipes:
        mocked_get_readiness_of_recipes.return_value = get_readiness_of_recipes_return
        diet = Diet.VEGAN
        take_best = False
        rc = RecipeController(items_dao=mockedDAO)
        
        assert rc.get_recipe(diet, take_best) == expected_result

@pytest.mark.unit
def test_id4_get_recipe():
    mockedDAO = MagicMock()
    get_readiness_of_recipes_return = {"Banana Bread": 1}
    expected_result = "Banana Bread"
    with patch('src.controllers.recipecontroller.RecipeController.get_readiness_of_recipes', autospec=True) as mocked_get_readiness_of_recipes:
        mocked_get_readiness_of_recipes.return_value = get_readiness_of_recipes_return
        diet = Diet.VEGAN
        take_best = True
        rc = RecipeController(items_dao=mockedDAO)
        
        assert rc.get_recipe(diet, take_best) == expected_result

# The sorting function is not working as intended
@pytest.mark.unit
def test_id5_get_recipe():
    mockedDAO = MagicMock()
    get_readiness_of_recipes_return = {"Banana Bread": 1, "Pancake": 0.2, "Sour Bread": 0.5}
    expected_result = "Sour Bread"
    with patch('src.controllers.recipecontroller.RecipeController.get_readiness_of_recipes', autospec=True) as mocked_get_readiness_of_recipes:
        mocked_get_readiness_of_recipes.return_value = get_readiness_of_recipes_return
        with patch('random.randint', autospec=True) as random_recipe:
            random_recipe.return_value = 1
            diet = Diet.NORMAL
            take_best = False
            rc = RecipeController(items_dao=mockedDAO)
            
            assert rc.get_recipe(diet, take_best) == expected_result

# If the take_best is true if should return the recipe with highest readiness
# but it is returning randomly
@pytest.mark.unit
def test_id6_get_recipe():
    mockedDAO = MagicMock()
    get_readiness_of_recipes_return = {"Pancake": 0.2, "Sour Bread": 0.5, "Banana Bread": 1}
    expected_result = "Banana Bread"
    with patch('src.controllers.recipecontroller.RecipeController.get_readiness_of_recipes', autospec=True) as mocked_get_readiness_of_recipes:
        mocked_get_readiness_of_recipes.return_value = get_readiness_of_recipes_return
        diet = Diet.NORMAL
        take_best = True
        rc = RecipeController(items_dao=mockedDAO)
        assert rc.get_recipe(diet, take_best) == expected_result
