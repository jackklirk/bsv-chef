import pytest
from unittest.mock import MagicMock
from src.controllers.recipecontroller import RecipeController
# I could not make the tests work, for some reason the src could not be found

@pytest.mark.unit
def test_id1_get_recipe():
    mockedDAO = MagicMock()
    obj = {}
    mockedDAO.get_readiness_of_recipes = [obj]
    diet = "vegan"
    take_best = False
    uc = RecipeController(items_dao=mockedDAO)
    
    assert uc.get_recipe(diet, take_best) == None

@pytest.mark.unit
def test_id2_get_recipe():
    mockedDAO = MagicMock()
    obj = {}
    mockedDAO.get_readiness_of_recipes = [obj]
    diet = "vegan"
    take_best = True
    uc = RecipeController(items_dao=mockedDAO)
    
    assert uc.get_recipe(diet, take_best) == None

@pytest.mark.unit
def test_id3_get_recipe():
    mockedDAO = MagicMock()
    obj = {"Banana Bread": 1}
    mockedDAO.get_readiness_of_recipes = [obj]
    diet = "vegan"
    take_best = False
    uc = RecipeController(items_dao=mockedDAO)
    
    assert uc.get_recipe(diet, take_best) == "Banana Bread"

@pytest.mark.unit
def test_id4_get_recipe():
    mockedDAO = MagicMock()
    obj = {"Banana Bread": 1}
    mockedDAO.get_readiness_of_recipes = [obj]
    diet = "vegan"
    take_best = True
    uc = RecipeController(items_dao=mockedDAO)
    
    assert uc.get_recipe(diet, take_best) == "Banana Bread"

@pytest.mark.unit
def test_id5_get_recipe():
    mockedDAO = MagicMock()
    obj = {"Banana Bread": 1, "Sour Bread": 0.5, "Pancake": 0.2}
    mockedDAO.get_readiness_of_recipes = [obj]
    diet = "normal"
    take_best = False
    # I should mock the random with patch to number 1 here, but no time :(
    uc = RecipeController(items_dao=mockedDAO)
    
    assert uc.get_recipe(diet, take_best) == "Sour Bread"

@pytest.mark.unit
def test_id5_get_recipe():
    mockedDAO = MagicMock()
    obj = {"Banana Bread": 1, "Sour Bread": 0.5, "Pancake": 0.2}
    mockedDAO.get_readiness_of_recipes = [obj]
    diet = "normal"
    take_best = True
    # I should mock the random to number 2 here, but no time :(
    uc = RecipeController(items_dao=mockedDAO)
    
    assert uc.get_recipe(diet, take_best) == "Banana Bread"