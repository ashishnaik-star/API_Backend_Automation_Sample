import requests
from behave import *

import Configurations


@given(u': API Endpoint which contains single post resource')
def step_impl(context):
    Ip = Configurations.Configparser()
    context.Posts_get_req = requests.get(url=Ip['API']['end_point'] + '/posts', auth=None)
    context.Json_val = context.Posts_get_req.json()


@when(u': Post contains id and user id as one')
def step_impl(context):
    assert context.Json_val[0]['userId'] == 1
    assert context.Json_val[0]['id'] == 1


@then(u': Check if the keyword "sunt aut" is present in Post')
def step_impl(context):
    assert context.Posts_get_req.status_code == 200


@given(u': API Endpoint which contains comments with ID {val:d}')
def step_impl(context, val):
    Ip = Configurations.Configparser()
    context.Posts_get_req_comment = requests.get(url=Ip['API']['end_point'] + '/comments', params={'postId': val},
                                                 auth=None)
    context.Json_val_comment = context.Posts_get_req_comment.json()

@when(u': Post contains postid as one')
def step_impl(context):
    assert "@" in context.Json_val_comment[0]['email']


@then(u': Check if the postid has value in it')
def step_impl(context):
   assert context.Posts_get_req_comment.status_code == 200





