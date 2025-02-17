import pytest
from app.candidates.dао.Candidates import Candidates
from app.config.development.load_env import candidates_patch

class TestCandidates:

    assert candidates_patch == r'C:\Users\asabl\PycharmProjects\HM_13?\app\data\candidates.json'

    def