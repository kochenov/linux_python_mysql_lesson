
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



--------------------------------

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




  --------------------- 10 задание

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

-------------------- Задание 11

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



------------ 12 задание
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

