# MapShops
API поиска магазинов по городам и улицам 


Создайте виртуальное окружение:
```bash
python -m venv env
```

Войдите в виртуальное окружение:
```bash
source env/bin/activate
```

Установите зависимости:
```bash
pip install -r requirements.txt
```

Скопируйте файл с переменными окружения:
```bash
cp .env.example .env
```

### Сборка образов и запуск контейнеров

В корне репозитория выполните команду:

```bash
docker-compose up --build
```

### Инициализация проекта

Команды выполняются внутри контейнера приложения:

```bash
docker-compose exec web bash
```

#### Применение миграций:

```bash
python manage.py migrate
```

#### Добавление фикстур

```bash
python manage.py loaddata city street shop shop-building
```

Проект доступен по адресу http://127.0.0.1:8000