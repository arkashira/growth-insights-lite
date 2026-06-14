import json
from dataclasses import dataclass
from argparse import ArgumentParser

@dataclass
class Feature:
    name: str
    description: str

class GrowthInsightsLite:
    def __init__(self):
        self.features = [
            Feature("Feature 1", "Description of Feature 1"),
            Feature("Feature 2", "Description of Feature 2"),
        ]

    def get_pitch_line(self):
        return "Growth Insights Lite: Your partner in growth"

    def get_description(self):
        return "Growth Insights Lite is a tool designed to provide actionable insights for growth"

    def get_feature_overview(self):
        feature_overview = []
        for feature in self.features:
            feature_overview.append({
                "Name": feature.name,
                "Description": feature.description,
            })
        return feature_overview

    def generate_readme(self):
        readme = "# Growth Insights Lite\n"
        readme += "## Pitch Line\n"
        readme += self.get_pitch_line() + "\n"
        readme += "## Description\n"
        readme += self.get_description() + "\n"
        readme += "## Feature Overview\n"
        readme += "| Name | Description |\n"
        readme += "| --- | --- |\n"
        for feature in self.features:
            readme += f"| {feature.name} | {feature.description} |\n"
        return readme

def main():
    parser = ArgumentParser(description="Growth Insights Lite")
    parser.add_argument("--generate-readme", action="store_true", help="Generate README.md")
    args = parser.parse_args()
    if args.generate_readme:
        growth_insights_lite = GrowthInsightsLite()
        with open("README.md", "w") as f:
            f.write(growth_insights_lite.generate_readme())

if __name__ == "__main__":
    main()
