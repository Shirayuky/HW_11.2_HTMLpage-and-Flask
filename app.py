# Приложение и все роуты
from typing import List

from flask import Flask, render_template
import utils


app = Flask(__name__)


@app.route("/")
def title_page():
    """Главная страница - вывод списком всех кандидатов"""
    candidates: List[dict] = utils.load_data()
    return render_template('list.html', candidates=candidates)


app.run()
