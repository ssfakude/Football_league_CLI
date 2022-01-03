import pytest
from league.svc_football import calculate_match_points
from re import findall



@pytest.fixture
def test_correct_inputs(input_file):
    lines=[]
    with open("testing_input.txt") as f:
        lines = f.readlines()
    for line in lines:
        match=  findall(r'(?<!\S)(?:[$]\S+|[^-?\d+\.?\d*]+)\b|-?\d+\.?\d*', line)
        assert len(match) == 4
        assert int(match[3]) >= 0
        assert int(match[1]) >= 0 
def test_points_results():
    assert calculate_match_points("teamA", "teamB", "6", "1") == {"teamA":3, "teamB":0}
    assert calculate_match_points("teamA", "teamB", "2", "2") == {"teamA":1, "teamB":1}

