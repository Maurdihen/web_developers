import json


def load_candidates(path):
    with open(path, 'r') as candidates:
        return json.load(candidates)


def get_candidate(id):
    return [candidate for candidate in load_candidates('candidates.json') if candidate['id'] == id][0]

def get_candidates_by_name(name):
    return [candidate for candidate in load_candidates('candidates.json') if name.lower() in candidate['name'].lower()]


def get_candidates_by_skill(skill):
    return [candidate for candidate in load_candidates('candidates.json') if skill.lower() in candidate['skills'].lower().split(', ')]