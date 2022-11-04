# Приложение и все роуты
from typing import List

from flask import Flask, render_template
import utils

app = Flask(__name__)


@app.route("/")
def list_page():
    """Главная страница - вывод списком всех кандидатов"""
    candidates: List[dict] = utils.load_data()
    return render_template('list.html', candidates=candidates)


@app.route("/candidate/<int:idx>")
def card_page(idx):
    """Вывод кандидата по id"""
    candidate_id_card: dict = utils.get_candidate_id(idx)
    if not candidate_id_card:
        return "Кандидат не найден"
    return render_template('card.html', candidate=candidate_id_card)


@app.route("/search/<name>")
def search_candidates_page(name):
    """Вывод кандидата по id"""
    candidate_name: List[dict] = utils.get_candidate_by_name(name)
    return render_template('search.html', candidates=candidate_name)


@app.route("/skill/<skill>")
def search_skill_page(skill):
    """Вывод кандидата по id"""
    candidate_skill_card: List[dict] = utils.get_candidate_by_skills(skill)
    if not candidate_skill_card:
        return "У вас слишком завышенные ожидания!"
    return render_template('skill.html', candidates=candidate_skill_card, skill=skill)


app.run()
