from django.test import TestCase
from django.urls import reverse

from .base import CategoryTestCaseMixin
from ..models import Category


class AdminTest(CategoryTestCaseMixin, TestCase):

    @classmethod
    def setUpClass(cls):
        from django.contrib import admin
        admin.autodiscover()
        cls.admin = admin
        return super().setUpClass()

    def setUp(self):
        self.user = self.create_user()
        self.user.is_superuser = True
        self.user.is_staff = True
        self.user.save()

    def get_request_with_user(self):
        request = self.get_request('en')
        request.user = self.user
        request.META['HTTP_HOST'] = 'example.com'
        return request

    def test_admin_owner_default(self):
        """
        Test that the ChangeForm contains Treebeard's MoveNodeForm
        """
        root = Category.add_root(name="test root")
        root.save()
        root = self.reload(root)
        root.add_child(name="test child 1")
        root.add_child(name="test child 2")

        admin_inst = self.admin.site._registry[Category]

        request = self.get_request_with_user()
        response = admin_inst.add_view(request)
        option = '<option value="first-child">First child of</option>'
        self.assertContains(response, option)

    def test_admin_list(self):
        root = Category.add_root(name="test root")
        root.attributes = {"class": "main", "id": "m42"}
        root.save()

        self.client.force_login(self.user)
        response = self.client.get(reverse("admin:aldryn_categories_category_changelist"))
        self.assertContains(response, 'test root')
        self.assertContains(response, ' class="main" id="m42"')
