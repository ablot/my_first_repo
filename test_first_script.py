"""
Unit tests for the simple first_script function
"""

import pytest
import first_script

def test_give_answer():
    assert first_script.give_answer() == "The answer is 42"

def test_increament():
    assert first_script.increment(12) == 13

def test_subtract_the_answer():
    assert first_script.sub_answ(12) == 30

