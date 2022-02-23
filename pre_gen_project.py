import sys
import cookiecutter.prompt
'''
This pre_gen is to avoid to input tests variables if you don't want to create it
'''

if "{{ cookiecutter.db }}" == "mysql":
    cookiecutter.prompt.read_user_variable("database_name", "django")
    cookiecutter.prompt.read_user_variable("database_user", "django")
    cookiecutter.prompt.read_user_variable("database_password", "django")
    cookiecutter.prompt.read_user_variable("database_root_password", "django")

else:
    """{{ cookiecutter.update(
        {
            "database_name": "",
            "database_user": "",
            "database_password": "",
            "database_root_password": "",
        }
    )}}"""

sys.exit(0)