import requests
from behave import *

import Configurations


@given(u': API Endpoint where we need to post resource')
def step_impl(context):
    Ip = Configurations.Configparser()gi
    context.Posts_create = requests.post(url=Ip['API']['end_point'] + '/comments', json=Configurations.payload_post(),
                                         auth=None)
    context.Posts_create_json = context.Posts_create.json()


@when(u': payload is created by user')
def step_impl(context):
    assert "userId" in context.Posts_create.text


@then(u': status message "{status:d}" to be given back as response')
def step_impl(context, status):
    assert context.Posts_create.status_code == status


@given(u': API Endpoint where we need to PUT resource')
def step_impl(context):
    Ip = Configurations.Configparser()
    context.Put_create = requests.put(url=Ip['API']['end_point'] + '/posts/1', json=Configurations.payload_put(),
                                      auth=None)
    context.Put_create_json = context.Put_create.json()


@when(u': payload is changed by the user')
def step_impl(context):
    assert "ashish" in context.Put_create_json['title']


@then(u': status message "{200:d}" to be given back as response after updation')
def step_impl(context, status):
    assert context.Put_create.status_code == status


@given(u': API Endpoint where we need to Patch resource')
def step_impl(context):
    Ip = Configurations.Configparser()
    context.Patch_create = requests.patch(url=Ip['API']['end_point'] + '/posts/1', json=Configurations.payload_patch(),
                                          auth=None)
    context.Patch_create_json = context.Patch_create.json()


@when(u': payload only where patch needs to be applied is changed by the user')
def step_impl(context):
    assert "ashwin" in context.Patch_create_json['title']


@then(u': status message "{200:d}" to be given back as response after Patch updation')
def step_impl(context, status):
    assert context.Patch_create.status_code == status


@given(u': API Endpoint where we need to Delete resource')
def step_impl(context):
    Ip = Configurations.Configparser()
    context.Delete_response = requests.delete(url=Ip['API']['end_point'] + '/posts/1',
                                              json=Configurations.payload_patch(),
                                              auth=None)
    context.Delete_response_json = context.Delete_response.json()


@when(u': Result body should have blank data')
def step_impl(context):
    assert str(context.Delete_response_json) == "{}"


@then(u': status message "{200:d}" to be given back as response after Delete updation')
def step_impl(context, status):
    assert context.Delete_response.status_code == status
