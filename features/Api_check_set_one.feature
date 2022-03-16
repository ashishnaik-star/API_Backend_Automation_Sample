# Created by Ashish at 15-03-2022
Feature: Testing sample Api from https://jsonplaceholder.typicode.com/ with get request

  Scenario: Validate List of Posts with keywords
    Given : API Endpoint which contains list of resources for Posts
    When : Posts contain set of 100 posts
    Then : Check if the keyword "qui est esse" is present in Posts

  Scenario: Validate List of Resources with keywords for Comments
    Given : API Endpoint which contains list of resources for comments
    When : Comments contain set of 500 Comments
    Then : Check if the keyword "Eliseo@gardner.biz" is present in Comments

  Scenario Outline: Check list of keywords from the API Response in Albums
     Given : API Endpoint which contains list of resources for Albums
      When : Comments contain set of 100 Albums with user id between 1 and 10
      Then : Check if the keyword <val> is present in Albums
    Examples:
      | val |
      | omnis laborum odio |
      | sunt qui excepturi placeat culpa |

  @smoke
  Scenario: Validate List of Resources with keywords for photos
    Given : API Endpoint which contains list of resources for photos
    When : Comments contain set of 5000 photos
    Then : Check if the keyword "https://via.placeholder.com/600/f9ab8f" is present in photos



