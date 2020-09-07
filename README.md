# emenu



Kroki instalacji
```bash
1. git clone https://github.com/kuzxnia/emenu.git && cd emenu
2. pipenv install
3. pipenv shell
4. modyfikacja konfiguracji bazy danych w config/settings/base.py zmienna 'DATABASES'
5. python manage.py migrate
6. python manage.py loaddata initial_data
7. python manage.py runserver
```
