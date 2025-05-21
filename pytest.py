import csv
import pytest
from unittest.mock import patch
import builtins
from project_msg import cowsay_msg_tux  # assuming this exists
from student_data_input_sys import data_input  # replace with your actual Python filename

# Helper function to read CSV content
def read_csv_file():
    try:
        with open("student sheet.csv", "r") as file:
            reader = csv.reader(file)
            return list(reader)
    except FileNotFoundError:
        return None

# Test to check CSV file creation and content
def test_data_input_creates_csv_file():
    with patch.object(builtins, 'input', return_value='3'):
        data_input()

    content = read_csv_file()
    assert content is not None
    assert content[0] == ["id", "attendance"]
    assert len(content) == 4  # 3 students + 1 header
    assert content[1][0].startswith("242-234-")
    assert content[1][1] == "0"


def test_cowsay_msg_called(monkeypatch):
    called = []

    def fake_cowsay_msg(msg):
        called.append(msg)
        return "fake cowsay output"

    monkeypatch.setattr("project_msg.cowsay_msg_tux", fake_cowsay_msg)

    with patch.object(builtins, 'input', return_value='1'):
        data_input()

    assert "student file has created" in called
