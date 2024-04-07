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
Для решения заданий связанных с базой данных дальше, я буду использовать `postgres` (как аналог MySql), так как я использую Windows на своём ПК, принял решение делать разработку в докер контейнере и использовать `docker-compose.yml `

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

### Задание 9

Заполнить низкоуровневые таблицы именами(животных), командами
которые они выполняют и датами рождения

### Решение задания 9
код находится в файле `database.sql`

```
-- Вставка данных в таблицу "Команда"
INSERT INTO command (name) VALUES
  ('Сидеть'),
  ('Лежать'),
  ('Дай лапу'),
  ('Принеси');

-- Вставка данных в таблицу "Животное"
INSERT INTO animal (type) VALUES
  ('Домашнее животное'),
  ('Вьючное животное');

-- Вставка данных в таблицу "Домашнее животное"
INSERT INTO pet (animal_id, species) VALUES
  (1, 'Собака'),
  (1, 'Кошка'),
  (1, 'Хомяк');

-- Вставка данных в таблицу "Вьючное животное"
INSERT INTO pack_animal (animal_id, species, carrying_capacity) VALUES
  (2, 'Лошадь', 1000),
  (2, 'Верблюд', 800),
  (2, 'Осёл', 500);

-- Вставка данных в таблицу "Выполнение команды"
INSERT INTO command_execution (pet_id, command_id, date_of_birth) VALUES
  (1, 1, '2023-01-01'),
  (1, 2, '2023-02-02'),
  (2, 3, '2023-03-03'),
  (3, 4, '2023-04-04'),
  (1, 3, '2023-05-05'), -- Собака умеет давать лапу
  (2, 4, '2023-06-06'); -- Кошка умеет приносить

```

### Задание 10 
Удалив из таблицы верблюдов, т.к. верблюдов решили перевезти в другой
питомник на зимовку. Объединить таблицы лошади, и ослы в одну таблицу.

#### Решение задания 10

```

-- Создание новой таблицы "Вьючное животное объединенное"
CREATE TABLE pack_animal_combined (
  id SERIAL PRIMARY KEY,
  species VARCHAR(255) NOT NULL,
  carrying_capacity INT NOT NULL
);

-- Перенос данных из таблицы "Лошадь"
INSERT INTO pack_animal_combined (species, carrying_capacity)
SELECT species, carrying_capacity
FROM pack_animal
WHERE species = 'Лошадь';

-- Перенос данных из таблицы "Осёл"
INSERT INTO pack_animal_combined (species, carrying_capacity)
SELECT species, carrying_capacity
FROM pack_animal
WHERE species = 'Осёл';

-- Удаление таблиц "Лошадь" и "Осёл"
DROP TABLE pack_animal;

-- Переименование "Вьючное животное объединенное" в "Вьючное животное"
ALTER TABLE pack_animal_combined RENAME TO pack_animal;

```

### Задание 11
Создать новую таблицу “молодые животные” в которую попадут все
животные старше 1 года, но младше 3 лет и в отдельном столбце с точностью
до месяца подсчитать возраст животных в новой таблице

#### Решение задания 11

```

-- Создание новой таблицы "Молодые животные"
CREATE TABLE young_animals (
  -- Идентификатор животного (autoincrement)
  id SERIAL PRIMARY KEY,
  -- Внешний ключ к таблице "Животное" (id животного, не null)
  animal_id INT NOT NULL,
  -- Вид животного (строка длиной 255 символов, не null)
  species VARCHAR(255) NOT NULL,
  -- Возраст в месяцах (целое число, не null)
  age_in_months INT NOT NULL,
  -- Ограничение внешнего ключа (ссылка на таблицу "Животное" по полю id)
  FOREIGN KEY (animal_id) REFERENCES animal (id)
);

-- Заполнение таблицы "Молодые животные"
INSERT INTO young_animals (animal_id, species, age_in_months)
SELECT
  -- id животного из таблицы "Выполнение команды"
  animal_id,
  -- Вид животного из таблицы "Выполнение команды"
  species,
  -- Вычисление возраста в месяцах
  (EXTRACT(YEAR FROM CURRENT_DATE) - EXTRACT(YEAR FROM date_of_birth)) * 12 + EXTRACT(MONTH FROM CURRENT_DATE) - EXTRACT(MONTH FROM date_of_birth)
FROM command_execution
JOIN pet ON pet.id = command_execution.pet_id
WHERE 
  -- Животные старше 1 года 
  (EXTRACT(YEAR FROM CURRENT_DATE) - EXTRACT(YEAR FROM date_of_birth)) * 12 + EXTRACT(MONTH FROM CURRENT_DATE) - EXTRACT(MONTH FROM date_of_birth) > 12
  -- И младше 3 лет
AND (EXTRACT(YEAR FROM CURRENT_DATE) - EXTRACT(YEAR FROM date_of_birth)) * 12 + EXTRACT(MONTH FROM CURRENT_DATE) - EXTRACT(MONTH FROM date_of_birth) < 36;

```

### Задание 12

 Объединить все таблицы в одну, при этом сохраняя поля, указывающие на
прошлую принадлежность к старым таблицам.


### Решение задания 12

```

SELECT
  a.id,
  a.type,
  p.species,
  pa.carrying_capacity,
  ce.command_id,
  ce.date_of_birth
FROM animal a
LEFT JOIN pet p ON a.id = p.animal_id
LEFT JOIN pack_animal pa ON a.id = p.animal_id
LEFT JOIN command_execution ce ON p.id = ce.pet_id;

```

### Задание 13/14

`main.py` и `classes.py`

Весь код прокомментирован и понятен интуитивно.