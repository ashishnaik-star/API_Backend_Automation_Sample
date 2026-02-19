import os
import sys
from behave import *


def before_all(context):
    # Ensure repository root is on PYTHONPATH so `import Configurations` works
    repo_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
    if repo_root not in sys.path:
        sys.path.insert(0, repo_root)
    print("*******************Before ALL******************")


def before_feature(context, feature):
    print("*****************Before Feature****************")


def before_scenario(context, scenario):
    print("********************Before Scenario******************")


def after_all(context):
    print("*******************After ALL******************")
