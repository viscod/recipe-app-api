from decimal import Decimal
from django.test import TestCase
from django.contrib.auth import get_user_model
from recipe.models import Recipe


class TestRecipe(TestCase):

    def test_create_recipe(self):
        user = get_user_model().objects.create_user(
            email='test@example.com',
            password='test1234'
        )

        recipe = Recipe.objects.create(
            user=user,
            title='Sample Recipe',
            time_minutes=5,
            price=Decimal('5.50'),
            description='Sample Recipe Description'
        )
        self.assertEqual(str(recipe), recipe.title)
