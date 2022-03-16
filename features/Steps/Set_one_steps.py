import behave
from behave import *
import requests

import Configurations


@given(': API Endpoint which contains list of resources for Posts')
def step_impl_post(context):
    Ip = Configurations.Configparser()
    context.Posts_get_req = requests.get(url=Ip['API']['end_point'] + '/posts', auth=None)
    context.Json_val = context.Posts_get_req.json()


@when(': Posts contain set of 100 posts')
def step_impl_when_post(context):
    for i in range(0, 100):
        assert context.Json_val[i]['id'] == i + 1


@then(': Check if the keyword "{val}" is present in Posts')
def step_impl_then_post(context, val):
    assert context.Posts_get_req.status_code == 200
    assert val in context.Posts_get_req.text


@given(u': API Endpoint which contains list of resources for comments')
def step_impl_comment(context):
    Ip = Configurations.Configparser()
    context.Posts_get_comment = requests.get(url=Ip['API']['end_point'] + '/comments', auth=None)
    context.Posts_get_comment_json = context.Posts_get_comment.json()


@when(u': Comments contain set of 500 Comments')
def step_impl_when_comment(context):
    for i in range(0, 500):
        assert context.Posts_get_comment_json[i]['id'] == i + 1


@then(u': Check if the keyword "{val}" is present in Comments')
def step_impl_then_comment(context, val):
    assert context.Posts_get_comment.status_code == 200
    assert val in context.Posts_get_comment.text


@given(u': API Endpoint which contains list of resources for Albums')
def step_impl_given_album(context):
    Ip = Configurations.Configparser()
    context.Posts_get_albums = requests.get(url=Ip['API']['end_point'] + '/albums', auth=None)
    context.Posts_get_albums_json = context.Posts_get_albums.json()


@when(u': Comments contain set of 100 Albums with user id between 1 and 10')
def step_impl_when_album(context):
    Range_list = list(range(1, 11))
    for i in range(0, 100):
        assert context.Posts_get_albums_json[i]['userId'] in Range_list


@then(u': Check if the keyword {val} is present in Albums')
def step_impl_then_album(context, val):
    assert context.Posts_get_albums.status_code == 200
    assert val in context.Posts_get_albums.text


@given(u': API Endpoint which contains list of resources for photos')
def step_impl_given_photos(context):
    Ip = Configurations.Configparser()
    context.Posts_get_photos = requests.get(url=Ip['API']['end_point'] + '/photos', auth=None)
    context.Posts_get_photos_json = context.Posts_get_photos.json()


@when(u': Comments contain set of 5000 photos')
def step_impl_when_photos(context):
    for i in range(0, 500):
        assert context.Posts_get_photos_json[i]['id'] == i + 1


@then(u': Check if the keyword "{val}" is present in photos')
def step_impl_then_photos(context, val):
    assert context.Posts_get_photos.status_code == 200
    assert val in context.Posts_get_photos.text
