from tasks import send_email_task

# Пример использования: имитация утечки
if __name__ == "__main__":
    email = "user@example.com"   # ← Куда отправлять
    subject = "🚨 Утечка обнаружена"
    body = "Ваши данные были найдены в открытых источниках. Проверьте аккаунты."

    send_email_task.delay(email, subject, body)
    print("📨 Задача на отправку email отправлена в очередь")