from flask import Flask, render_template
from functions import *

app = Flask(__name__)


@app.route('/')
def main_page():
    candidates = load_candidates('candidates.json')
    name_candidate = load_candidates('candidates.json')[1]['name']
    return render_template('list.html', candidates=candidates, name_candidate=name_candidate)


@app.route('/candidate/<x>')
def page_candidate(x):
    list_candidate = get_candidate(int(x))
    return render_template('single.html', list_candidate=list_candidate)


@app.route('/search/<name>')
def search_by_name(name):
    len_ = len(get_candidates_by_name(name))
    return render_template('candidate_name.html', list_candidates=get_candidates_by_name(name), len_=len_)


@app.route('/skill/<skill_name>')
def search_by_skills(skill_name):
    len_ = len(get_candidates_by_skill(skill_name))
    return render_template('skill.html', list_candidates=get_candidates_by_skill(skill_name), len_=len_, skill_name=skill_name)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)