# 📬 Email Notification Microservice

Микросервис для отправки email-уведомлений о найденных утечках данных, построенный на базе:
- 🔁 **Celery** для асинхронных фоновых задач
- 🧠 **Redis** как брокер очередей
- 🌐 **FastAPI** для REST API интерфейса

---

## 🚀 Возможности

- Приём запросов на отправку email через HTTP (`/send-email`)
- Асинхронная отправка писем через Celery (не блокирует основной поток)
- Подключение к SMTP (Gmail или любой другой)
- Расширяемость под Telegram/SMS/Slack и др.
- Готово для использования как микросервис

---

## 🛠️ Установка

### 1. Клонируй репозиторий

```bash
git clone https://github.com/yourname/leak-email-service.git
cd leak-email-service
```
### 2. Установи зависимости

```pip install -r requirements.txt```

Или вручную:

```pip install fastapi uvicorn celery redis```

### 3. Настрой config.py

```EMAIL_HOST = "smtp.gmail.com"
EMAIL_PORT = 587
EMAIL_USER = "your_email@gmail.com"          # Твой email
EMAIL_PASSWORD = "your_app_password"         # Пароль приложения (не обычный!)
REDIS_BROKER_URL = "redis://localhost:6379/0"
```

## 📦 Структура проекта
```
email_service/
├── config.py            # Настройки SMTP и Redis
├── email_utils.py       # Функция отправки email
├── tasks.py             # Celery задачи
├── worker.py            # Запуск Celery воркера
├── main.py              # REST API на FastAPI
├── example_producer.py  # Пример прямого вызова задачи
```

## 🧪 Запуск

## 1. Запуск Redis (если локально)
```
docker run -p 6379:6379 redis

```
## 2. Запуск Celery worker (в отдельном окне терминала)
```
python worker.py

```
## 3. Запуск REST API
```
uvicorn main:app --reload

```
Теперь API доступен по адресу: 
```
http://localhost:8000

```

## 🌐 Использование API

## 🔹 POST /send-email

Описание: Отправляет письмо с уведомлением (в фоне)

## 📤 Пример запроса
```
POST http://localhost:8000/send-email
Content-Type: application/json

{
  "to": "user@example.com",
  "subject": "Утечка обнаружена!",
  "body": "Ваши данные были найдены в открытых источниках."
}
```

## ✅ Пример ответа
```
{
  "status": "ok",
  "message": "Email task added to queue"
}
```

## 🧩 Возможности для расширения
	•	Добавить поддержку Telegram-бота
	•	Добавить логирование в базу данных (PostgreSQL, SQLite)
	•	Добавить /send-notification с выбором канала (email, telegram, sms)
	•	Поддержка очередей с приоритетами

# 💡 Полезные команды
## Проверка очереди в Redis
```
redis-cli monitor

```
## Проверка задач Celery
```
celery -A tasks inspect active

```

