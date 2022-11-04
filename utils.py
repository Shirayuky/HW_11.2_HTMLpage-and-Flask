# Все функции

# "id": 1,
#     "name": "Adela Hendricks",
#     "picture": "https://picsum.photos/200",
#     "position": "Go разработчик",
#     "gender": "female",
#     "age": 40,
#     "skills": "go, python"
from __future__ import annotations
from typing import List
import json


# Загрузка
def load_data() -> List[dict]:
    """Загружает список данных(как dict) из json файла"""
    with open('candidates.json', 'r', encoding='utf-8') as file:
        return list(json.load(file))


# print(f"База: {load_data()}")


# Поиск/вывод данных по ключу
def get_candidate_id(candidate_id: int) -> dict:
    for candidate in load_data():
        if candidate['id'] == candidate_id:
            return candidate


# print(f"Поиск по id: {get_candidate_id(4)}")


# Поиск/вывод данных по значению=имя
def get_candidate_by_name(candidate_name: str) -> List[dict]:
    result = []
    for candidate in load_data():
        if candidate['name'] == candidate_name:
            result.append(candidate)
    return result


# print(f"Поиск по имени: {get_candidate_by_name('Day')}")


# Поиск/вывод данных по значению=навык
def get_candidate_by_skills(candidate_skill: str) -> List[dict]:
    result = []
    for candidate in load_data():
        if candidate_skill.lower() in candidate['skills'].lower().split(', '):
            result.append(candidate)
    return result

# print(f"Поиск по навыку: {get_candidate_by_skills('python')}")
