from rest_framework.test import APIClient
from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse
from decimal import Decimal
from rest_framework import status
from recipe.models import Recipe
from recipe.serializers import RecipeSerializer

RECIPES_URL = reverse('recipe:recipe-list')


def create_recipe(user, **params):
    """ helper function for creating recipe """
    defaults = {
        'title': 'Sample Title',
        'time_minutes': 4,
        'price': Decimal('4.75'),
        'description': 'sample description',
        'link': 'http://example.com/sample_recipe.pdf'
    }
    defaults.update(params)
    recipe = Recipe.objects.create(user=user, **defaults)
    return recipe


class TestPublicRecipeAPI(TestCase):
    def setUp(self):  # noqa
        self.client = APIClient()

    def test_auth_is_required(self):
        res = self.client.get(RECIPES_URL)
        self.assertEqual(res.status_code, status.HTTP_401_UNAUTHORIZED)


class TestPrivateRecipeAPI(TestCase):
    def setUp(self): # noqa
        self.client = APIClient()
        self.user = get_user_model().objects.create_user(
            email='test@example.com',
            password='test1234'
        )
        self.client.force_authenticate(self.user)

    def test_retrieve_recipes(self):
        create_recipe(self.user)
        create_recipe(self.user)

        res = self.client.get(RECIPES_URL)
        recipes = Recipe.objects.all().order_by('-id')
        serializer = RecipeSerializer(recipes, many=True)

        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(res.data, serializer.data)


def test_retrieve_recipes_limited_to_user(self):
    other_user = get_user_model().objects.create_user(
        email='other@example.com',
        password='other_password123'
    )

    create_recipe(other_user)
    create_recipe(self.user)

    res = self.client.get(RECIPES_URL)
    recipes = Recipe.objects.all().filter(user=self.user)
    serializer = RecipeSerializer(recipes, many=True)

    self.assertEqual(res.status_code, status.HTTP_200_OK)
    self.assertEqual(res.data, serializer.data)
