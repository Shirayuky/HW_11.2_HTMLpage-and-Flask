# Все функции

# "id": 1,
#     "name": "Adela Hendricks",
#     "picture": "https://picsum.photos/200",
#     "position": "Go разработчик",
#     "gender": "female",
#     "age": 40,
#     "skills": "go, python"
from __future__ import annotations
import requests
import json
from typing import List

# Включение загрузки
def get_all_candidates() -> List[dict]:
    """Включает загрузку данных"""
    return load_data()

# Загрузка
def load_data() -> List[dict]:
    """Загружает список данных(как dict) из json файла"""
    path = requests.get("https://jsonkeeper.com/b/A8VV", verify=False)

    with open(path) as file:
        candidates = list(json.load(file))
        return candidates


# Поиск/вывод данных по ключу
def get_candidate_id (candidate_id: int) -> dict:
    for candidate in get_all_candidates():
        if candidate['id'] == candidate_id:
            return candidate


# Поиск/вывод данных по значению=имя
def get_candidate_by_name(candidate_name: str) -> List[dict]:
    result = []
    for candidate in get_all_candidates():
        if candidate['name'].title() == candidate_name:
            result.append(candidate)
    return result


# Поиск/вывод данных по значению=навык
def get_candidate_by_skills(candidate_skill: str) -> List[dict]:
    result = []
    for candidate in get_all_candidates():
        if candidate_skill in candidate['skill'].lower().split(', '):
            result.append(candidate)
    return result

