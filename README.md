# Backend cho bài tập lớn CÔNG NGHỆ PHẦN MỀM
## 1.How to install
### 1a.Backend
> [!WARNING]
> Sử dụng lệnh **virtualenv env** để tạo virtual environment

> [!WARNING]
> Kích hoạt virtual environment **env\Scripts\activate** trước khi cài đặt các thư viện
```
    pip install djangorestframework djangorestframework-simplejwt django-cors-headers djoser
```
```
    python manage.py makemigrations
```
```
    python manage.py migrate
```
> [!WARNING]
> Change directory vào backend folder trước khi runserver
```
    python manage.py runserver
```


