# Created by Ashish at 16-03-2022
Feature: Testing sample Api from https://jsonplaceholder.typicode.com/ with POST/PUT/PATCH/DELETE

  Scenario: Posting user defined post to API and fetching response
    Given : API Endpoint where we need to post resource
    When : payload is created by user
    Then : status message "201" to be given back as response

  Scenario: Posting user defined Put to API and fetching response
    Given : API Endpoint where we need to PUT resource
    When : payload is changed by the user
    Then : status message "200" to be given back as response after updation

  Scenario: Posting user defined Patch to API and fetching response
    Given : API Endpoint where we need to Patch resource
    When : payload only where patch needs to be applied is changed by the user
    Then : status message "200" to be given back as response after Patch updation

  Scenario: Deleting and entry whit API and fetching response
    Given : API Endpoint where we need to Delete resource
    When : Result body should have blank data
    Then : status message "200" to be given back as response after Delete updation
