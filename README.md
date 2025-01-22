# 🏔️ Pereval API

**REST API для учёта и модерации горных перевалов**  
Серверная часть системы, позволяющая туристам добавлять данные о перевалах, а модераторам — проверять их.

---

## 📌 Задача проекта

Разработать API для мобильного приложения, которое:
1. Позволяет пользователям добавлять информацию о перевалах (координаты, фото, уровень сложности).
2. Обеспечивает модерацию данных через изменение статуса записей.
3. Запрещает редактирование данных после прохождения модерации.

---

## 🚀 Возможности API

### Основные методы:
| Метод | Эндпоинт | Описание |
|-------|----------|----------|
| `POST` | `/submitData/` | Добавление нового перевала |
| `GET` | `/submitData/<id>/` | Получение данных по ID |
| `PATCH` | `/submitData/<id>/update/` | Редактирование (только статус `new`) |
| `GET` | `/submitData/list/?user__email=<email>` | Фильтрация по email пользователя |

### Ключевые особенности:
✅ Работа с изображениями в Base64  
✅ Валидация координат и уровней сложности  
✅ Автоматический статус `new` для новых записей  
✅ Защита от изменения персональных данных  
✅ Поддержка Docker + PostgreSQL

---

## 🛠 Технологии

![Django](https://img.shields.io/badge/Django-092E20?logo=django&logoColor=white)
![DRF](https://img.shields.io/badge/DRF-red?logo=django&logoColor=white)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-316192?logo=postgresql&logoColor=white)
![Docker](https://img.shields.io/badge/Docker-2CA5E0?logo=docker&logoColor=white)

---

## 🚀 Быстрый старт

### 1. Установка
```bash
git clone https://github.com/Levushka46/pavel.git
cd pereval
cp .env.example .env  # Заполните настройки БД
