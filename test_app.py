import pandas as pd
from app import df, update_chart

def test_data_loaded():
    """Test that the CSV data loads and is not empty"""
    assert not df.empty

def test_region_filter_all():
    """Test that 'all' region returns data"""
    fig = update_chart("all")
    assert fig is not None

def test_region_filter_north():
    """Test that filtering by north does not crash"""
    fig = update_chart("north")
    assert fig is not None
