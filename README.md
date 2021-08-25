# geekshop

Интернет магазин мебели 

### Устанавливаем нужные библиотеки
```
pip3 install django==2.2 Pillow
```

### Создаем базу данных
```
python3 manage.py makemigrations
python3 manage.py migrate
python3 manage.py createsuperuser
```
### Запускаем
```
python3 manage.py runserver
```

переходим в админку
/admin 
входим под созданным пользователем добавляем товары, фото кладем в папку `/geekshop/media/products_images`

