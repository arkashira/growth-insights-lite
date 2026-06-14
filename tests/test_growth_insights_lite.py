import sys
import os
from growth_insights_lite import GrowthInsightsLite, Feature, main
import pytest

def test_get_pitch_line():
    growth_insights_lite = GrowthInsightsLite()
    assert growth_insights_lite.get_pitch_line() == "Growth Insights Lite: Your partner in growth"

def test_get_description():
    growth_insights_lite = GrowthInsightsLite()
    assert growth_insights_lite.get_description() == "Growth Insights Lite is a tool designed to provide actionable insights for growth"

def test_get_feature_overview():
    growth_insights_lite = GrowthInsightsLite()
    feature_overview = growth_insights_lite.get_feature_overview()
    assert len(feature_overview) == 2
    assert feature_overview[0]["Name"] == "Feature 1"
    assert feature_overview[0]["Description"] == "Description of Feature 1"
    assert feature_overview[1]["Name"] == "Feature 2"
    assert feature_overview[1]["Description"] == "Description of Feature 2"

def test_generate_readme():
    growth_insights_lite = GrowthInsightsLite()
    readme = growth_insights_lite.generate_readme()
    assert "# Growth Insights Lite" in readme
    assert "Growth Insights Lite: Your partner in growth" in readme
    assert "Growth Insights Lite is a tool designed to provide actionable insights for growth" in readme
    assert "| Name | Description |" in readme
    assert "| --- | --- |" in readme
    assert "| Feature 1 | Description of Feature 1 |" in readme
    assert "| Feature 2 | Description of Feature 2 |" in readme

def test_main():
    original_argv = sys.argv
    try:
        sys.argv = ["growth_insights_lite.py", "--generate-readme"]
        main()
    finally:
        sys.argv = original_argv
    
    assert os.path.exists("README.md")
    
    with open("README.md", "r") as f:
        readme = f.read()
    
    assert "# Growth Insights Lite" in readme
    assert "Growth Insights Lite: Your partner in growth" in readme
    assert "Growth Insights Lite is a tool designed to provide actionable insights for growth" in readme
    assert "| Name | Description |" in readme
    assert "| --- | --- |" in readme
    assert "| Feature 1 | Description of Feature 1 |" in readme
    assert "| Feature 2 | Description of Feature 2 |" in readme
    
    # Clean up the generated file after test
    os.remove("README.md")
