from django.contrib.auth import get_user_model

from django_webtest import WebTest


class TaskTest(WebTest):

    def test_login(self):
        # WHEN anonymous user try to access
        index = self.app.get('/',)

        # THEN sites redirects to login page
        self.assertEqual(index.status_code, 302)

        # GIVEN a registed user
        user = get_user_model().objects.create_user(
                username='testuser',
                password='12345')

        # WHEN users logged tries to open the site
        index = self.app.get('/', user=user)

        # THEN access granted
        self.assertEqual(index.status_code, 200)
