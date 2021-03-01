from setuptools import setup
excluded = ['manage.py, tests/settings.py']

setup(name="django-paranoid",
      version="0.9",
      description="this library adds 'created_at', 'updated_at' and 'delete_at'  fields like a rail apps in django,"
                  " also added soft delete method",
      long_description=open('README.md', 'r').read(),
      long_description_content_type='text/markdown',
      author="Carlos Ganoza Plasencia",
      author_email="cganozap@gmail.com",
      url="https://github.com/drneox/django-paranoid",
      license="GPL",
      packages=["django_paranoid"],
      keywords="django created_at updated_at deleted_at fields models django-admin soft delete softdelete",
      )
