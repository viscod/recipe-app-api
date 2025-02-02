from unittest.mock import patch
from psycopg2 import OperationalError as Psycopg2Error
from django.core.management import call_command
from django.db.utils import OperationalError
from django.test import SimpleTestCase


@patch('core.management.commands.wait_for_db.Command.check')
class CommandTests(SimpleTestCase):
    """ test wait for db """
    def test_wait_for_db_ready(self, patched_check):
        patched_check.return_value = True

        call_command('wait_for_db')

        patched_check.assert_called_once_with(databases=['default'])

    @patch('time.sleep')
    def test_wait_for_db_delay(self, patched_sleep, patched_check):
        """
        we raise db adapter exception twice mocking state
        where the db started but the _app is not
        ready yet to connect
        then we raise _app exception three times mocking the
        state that the _app started but the testing db is not ready
        or has not been created
        or not ready accept connection from the _app
        then we mock the happy scenario by return True
        """
        patched_check.side_effect = [Psycopg2Error] * 2 \
            + [OperationalError] * 3 + [True]

        call_command('wait_for_db')

        self.assertEqual(patched_check.call_count, 6)

        patched_check.assert_called_with(databases=['default'])
