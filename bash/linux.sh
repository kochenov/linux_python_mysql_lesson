#!/bin/bash

####
## ЗАДАНИЕ 1
#################

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


####
## ЗАДАНИЕ 2
#################

# Создаем директорию
mkdir Питомник

# Перемещаем файл
mv Друзья_человека.txt Питомник


####
## ЗАДАНИЕ 3
#################

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