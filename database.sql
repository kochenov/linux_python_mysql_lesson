
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