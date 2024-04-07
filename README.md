## Система учета для питомника в котором живут домашние и вьючные животные.

## OS Linux (Ubuntu)

### Задание 1

Используя команду cat в терминале операционной системы Linux, создать два файла Домашние животные (заполнив файл собаками, кошками,
хомяками) и Вьючные животными заполнив файл Лошадьми, верблюдами и
ослы), а затем объединить их. Просмотреть содержимое созданного файла.
Переименовать файл, дав ему новое имя (Друзья человека).

### Решение задания 1

```
    # Создаем два текстовых файла: "Домашние_животные" и "Вьючные_животные"
    # с перечислением животных в каждом.

    cat > Домашние_животные <<EOF
    Собака
    Кошка
    Хомяк
    EOF

    cat > Вьючные_животные <<EOF
    Лошадь
    Верблюд
    Осёл
    EOF

    # Объединяем два файла в один под названием "Друзья_человека".

    cat Домашние_животные Вьючные_животные > Друзья_человека

    # Просматриваем содержимое объединенного файла.

    cat Друзья_человека

    # Переименовываем файл "Друзья_человека" в "Друзья_человека.txt",
    # добавляя расширение .txt для ясности.

    mv Друзья_человека Друзья_человека.txt

```


### Задание 2

| Создать директорию, переместить файл туда.

### Решение задания 2

```

# Создаем директорию
mkdir Питомник

# Перемещаем файл
mv Друзья_человека.txt Питомник

```


### Задание 3

| Подключить дополнительный репозиторий MySQL. Установить любой пакет
из этого репозитория.

### Решение задания 3

```
# Добавляем репозиторий
# Загружаю репозиторий
wget https://dev.mysql.com/get/mysql-apt-config_0.8.22-1_all.deb
# Запуск настройки
sudo dpkg -i mysql-apt-config_0.8.22-1_all.deb

# Обновляем список пакетов
sudo apt update

# проверяю кэш пакетов
apt-cache policy mysql-server

# Устанавливаю пакет
sudo apt install mysql-client mysql-server

```

### Задание 4

| Установить и удалить deb-пакет с помощью dpkg.

### Решение задания 4
```

# Устанавливаю
sudo dpkg -i mysql-apt-config_0.8.22-1_all.deb

# Удаляю

sudo dpkg -r mysql-apt-config
```

### Задание 5

| Выложить историю команд в терминале ubuntu

### Решение задания 5

```

# Просмотр истории команд
history

# Сохранение истории команд
history > history.txt

# Очистка истории команд
history -c

```

### Задание 6

Нарисовать диаграмму, в которой есть класс родительский класс, домашние
животные и вьючные животные, в составы которых в случае домашних
животных войдут классы: собаки, кошки, хомяки, а в класс вьючные животные
войдут: Лошади, верблюды и ослы)

### Решение задания 6

![uml](uml.png "UML")

### Задание 7

 В подключенном MySQL репозитории создать базу данных “Друзья
человека”

### Решение задания 7

``` 
# Подключение к MySQL
mysql -u root -p
# ввод пароля

# Создание базы данных, друзья человека
CREATE DATABASE human_friends;

```
Для решения заданий связанных с базой данных дальше, я буду использовать Python и Postgres (как аналог MySql), так как я использую Windows на своём ПК, принял решение делать разработку в докер контейнере и использовать `docker-compose.yml `

```
# docker-compose.yml

# Определяет версию формата файла docker-compose.yml
version: '3'  

services:
  # Название сервиса - база данных PostgreSQL
  postgres:  
    # Образ для сервиса, используем последнюю версию postgres
    image: "postgres:latest"  
    # Окружающие переменные для сервиса
    environment:  
      # Пароль для пользователя postgres (не рекомендуется использовать в production)
      - POSTGRES_PASSWORD=password  
      # Название создаваемой базы данных
      - POSTGRES_DB=human_friends  

    ports:
      # Маппирование портов - внешний:внутренний. 5432 - стандартный порт postgres
      - "5432:5432"  

    volumes:
      # Тома - монтирование локальной директории data в контейнер, 
      # где будут храниться данные базы данных
      - ./data:/var/lib/postgresql/data  

```

Для запуска контейнера использую команду:

```docker compose -f "docker-compose.yml" up -d --build ```

При создании контейнера `postgres` база данных `human_friends` создаётся автоматически, так как в контейнере указанна переменная окружения:

```- POSTGRES_DB=human_friends  ```

### Задание 8

Создать таблицы с иерархией из диаграммы в БД


### Решение задания 8

В файле `database.sql` находится код для создания таблиц.

```
-- Создание таблицы "Животное"
CREATE TABLE animal (
  id SERIAL PRIMARY KEY,
  type VARCHAR(255) NOT NULL
);

-- Создание таблицы "Домашнее животное"
CREATE TABLE pet (
  id SERIAL PRIMARY KEY,
  animal_id INT NOT NULL,
  species VARCHAR(255) NOT NULL,
  FOREIGN KEY (animal_id) REFERENCES animal (id)
);

-- Создание таблицы "Вьючное животное"
CREATE TABLE pack_animal (
  id SERIAL PRIMARY KEY,
  animal_id INT NOT NULL,
  species VARCHAR(255) NOT NULL,
  carrying_capacity INT NOT NULL,
  FOREIGN KEY (animal_id) REFERENCES animal (id)
);

-- Создание таблицы "Команда"
CREATE TABLE command (
  id SERIAL PRIMARY KEY,
  name VARCHAR(255) NOT NULL
);

-- Создание таблицы "Выполнение команды"
CREATE TABLE command_execution (
  id SERIAL PRIMARY KEY,
  pet_id INT NOT NULL,
  command_id INT NOT NULL,
  date_of_birth DATE NOT NULL,
  FOREIGN KEY (pet_id) REFERENCES pet (id),
  FOREIGN KEY (command_id) REFERENCES command (id)
);


```