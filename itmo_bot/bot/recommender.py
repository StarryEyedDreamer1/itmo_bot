
def recommend_disciplines(user_input: str) -> str:
    user_input = user_input.lower()
    recommendations = []

    if "frontend" in user_input or "web" in user_input:
        recommendations += ["Продуктовая аналитика", "UX-дизайн", "ML в веб-продуктах"]

    if "ml" in user_input or "машинное обучение" in user_input or "data" in user_input:
        recommendations += ["Машинное обучение", "Глубокое обучение", "Компьютерное зрение"]

    if "стартап" in user_input or "предпринимательство" in user_input:
        recommendations += ["Управление продуктом", "Проектный практикум", "Стартап и бизнес-планирование"]

    if "математика" in user_input or "исследование" in user_input:
        recommendations += ["Теория вероятностей", "Оптимизация", "Научные семинары"]

    if not recommendations:
        recommendations.append("Основы программирования")
        recommendations.append("Введение в искусственный интеллект")

    result = "На основе твоих вводных я рекомендую тебе обратить внимание на дисциплины:\n"
    result += "\n".join(f"• {r}" for r in recommendations)
    return result
