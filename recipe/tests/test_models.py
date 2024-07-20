from decimal import Decimal
from django.test import TestCase
from django.contrib.auth import get_user_model
from recipe.models import Recipe, Tag


def create_user(email='user@example.com', password='test123'):
    return get_user_model().objects.create_user(
        email,
        password
    )


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

    def test_create_tag(self):
        user = create_user()
        tag = Tag.objects.create(user=user, name='Tag1')
        self.assertEqual(str(tag), tag.name)
