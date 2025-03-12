import pytest
from app import run, run2

def test_run():
    assert run() == "works"

def test_run2_num():
    """Test that run2 function correctly adds two numbers"""
    assert run2(2, 3) == 5
    assert run2(-1, 1) == 0
    assert run2(0, 0) == 0

def test_run2_string():
    """Test that run2 function correctly concatenates strings"""
    assert run2("hello ", "world") == "hello world"