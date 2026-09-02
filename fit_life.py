"""Проект FitLife - MVP версия 1.0"""

# Константы для расчетов
WATER_PER_KG = 30 # миллилитров на КГ веса
MLITTERS_TO_LITERS = 1000


# 1. Знакомство
user_name = input('Как тебя зовут? ')
user_age = int(input('Сколько тебе лет? '))

# 2. Сбор данных
user_weight = float(input('Введи свой вес в кг через точку (например 75.5): '))
user_height = float(input('Введи свой рост в метрах (например, 1.75): '))

# 3. Логика расчетов
bmi = round(user_weight / (user_height ** 2), 1)

# Подсчет воды: вес * 30 мл
water_needed = round((user_weight * WATER_PER_KG) / MLITTERS_TO_LITERS, 1)

# 4. Вывод красивого результата
print(f'''Привет, {user_name}!
Отчет для пользователя: {user_name} ({user_age} г.)
Твой Индекс Массы Тела: {bmi}
Рекомендуемая норма воды: {water_needed} л. в день
Расчет окончен. Будьте здоровы!''')
