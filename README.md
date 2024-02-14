# Шаблон для разработки микросервиса в контейнере

Зачастую после разработки приложения возникает необходимость
в его развертывании в OS Linux.
Чтобы избежать промежуточных действий по доставке зависимостей
в целевую операционную систему можно вести разработку
непосредственно в ней, используя контейнер Docker или Podman.

Разработанный шаблон позволяет создать контейнер,
в котором можно запускать исходный код на Python разрабатываемого приложения.
Для обновления пакетов использована библиотека poetry,
которая адаптирована для сборки образа в двух режимах: 
* разработки (используется по умолчанию);
* развертывания.

## Структура файлов
```bash
Project
├── app
│    ├── main.py
│    └── src
│        └── example.py
│    ├── poetry.lock
│    ├── pyproject.toml
│    └── Dockerfile
└── docker-compose.yaml    
```

## Конфигурация по умолчанию (docker-compose.yaml):
* Название образа: `my_img`.
* Название контейнера: `MyCont`.
* Установка зависимостей для разработки: `development=1`;
* Прослушивание порта `5000` на аналогичном порту в localhost.
* Непрерывный цикл работы запущенного контейнера: `command: tail -F anything`).
* Перезагрузка контейнера при перезагрузке основной системы: `restart: always`.

## Содержание сборки
Базовым образом является Python.
В качестве рабочих зависимостей используются uvicorn и fastapi,
для разработки - pytest.
Любая доступная зависимость [устанавливается](https://python-poetry.org/docs/cli/#add)
и [удаляется](https://python-poetry.org/docs/cli/#remove) через методы poetry (указаны ниже).

## Команды для работы

### Сборка образа и запуск контейнера
```bash
cd ./Project
docker compose up -d --build
```

### Подключение к контейнеру:
```bash
docker exec -it MyCont bash
```

### Добавление обычных зависимостей:
```bash
poetry add <PACKAGE>
```

### Добавление зависимостей для разработки:
```bash
poetry add --dev <PACKAGE>
```

### Удаление зависимостей:
```bash
poetry remove <PACKAGE>
```

### Остановка контейнера и удаление образа
Для удаления контейнера(ов) следует использовать команду:
```bash
cd ./Project
docker compose down --rmi all
```

### Порядок работы в PyCharm
#### Настройка проекта
1. Клонирование и переименование шаблона проекта
1. Переход в каталог с проектом, сборка образа и запуск контейнера
1. Открытие существующего проекта в PyCharm
1. Добавление интерпретатора ([отличаются в разных ОС](https://www.jetbrains.com/help/pycharm/settings-docker.html))
1. Определение конфигурации запуска (требуется сопоставление путей локальной машины и контейнера)

#### Обновление зависимостей
1. Запуск терминала
1. Добавление (удаление) зависимости
1. Удаление старого образа и сборка нового
> Для обновления зависимостей на уровне системы требуется обновление Dockerfile.

#### Запуск и отладка скриптов
> Успешная настройка проекта и актуализация зависимостей
> позволяет использовать стандартные инструменты PyCharm.

## Источники
1. [Running Docker Containers Indefinitely](https://www.baeldung.com/ops/running-docker-containers-indefinitely)
1. [Ubuntu: Docker Official Image](https://hub.docker.com/_/ubuntu/tags)
1. [Connecting to an existing docker container](https://docs.docker.com/engine/reference/commandline/container_exec/)
1. [Templates for Docker Development Environments (Fast API)](https://github.com/docker/awesome-compose/tree/master/fastapi)
1. [Containerized Python Development (3 parts)](https://www.docker.com/blog/tag/python-env-series/)
1. [Docker Best Practices for Python Developers](https://testdriven.io/blog/docker-best-practices/)
1. [Docker connection settings](https://www.jetbrains.com/help/pycharm/settings-docker.html)
1. [Test-Driven Development Steps](https://github.com/jonnyg23/obsidian_devlog/blob/master/Test-Driven%20Development%20with%20FastAPI%20and%20Docker.md)
1. [Poetry — прекрасная альтернатива pip (шпаргалка)](https://habr.com/ru/articles/593529/)
1. [Blazing fast Python Docker builds with Poetry](https://medium.com/@albertazzir/blazing-fast-python-docker-builds-with-poetry-a78a66f5aed0)
