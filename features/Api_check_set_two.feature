# Created by Ashish at 16-03-2022
Feature: Testing sample Api from https://jsonplaceholder.typicode.com/ with GET

  Scenario: Validate List of Posts with keywords
    Given : API Endpoint which contains single post resource
    When : Post contains id and user id as one
    Then : Check if the keyword "sunt aut" is present in Post

 Scenario Outline: Validate List of Posts with comment ID
    Given : API Endpoint which contains comments with ID <val>
    When : Post contains postid as one
    Then : Check if the postid has value in it
    Examples:
   |val |
   |2   |

