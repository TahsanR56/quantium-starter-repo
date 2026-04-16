import pytest
from app import app
import chromedriver_autoinstaller

chromedriver_autoinstaller.install()

def test_header_exists(dash_duo):
    dash_duo.start_server(app)
    header = dash_duo.wait_for_element("h1", timeout=10)
    assert header is not None
    assert "Pink Morsel" in header.text

def test_chart_exists(dash_duo):
    dash_duo.start_server(app)
    chart = dash_duo.wait_for_element("#sales-chart", timeout=10)
    assert chart is not None

def test_region_picker_exists(dash_duo):
    dash_duo.start_server(app)
    radio = dash_duo.wait_for_element("#region-filter", timeout=10)
    assert radio is not None
