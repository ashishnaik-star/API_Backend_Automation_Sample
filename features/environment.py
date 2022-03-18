from behave import *


def before_all(context):
    print("*******************Before ALL******************")


def before_feature(context,feature):
    print("*****************Before Feature****************")


def before_scenario(context,scenario):
    print("********************Before Scenario******************")


def After_all(context):
    print("*******************Before ALL******************")

