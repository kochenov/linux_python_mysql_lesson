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
