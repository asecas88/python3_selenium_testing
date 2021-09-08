@wip
Feature: Search box

Scenario Outline: The user search a word

    Given The user is in main page
    When The user search '<item>'
    Then The user is in '<item>' page

Examples:

    | item           |
    | PS4            |
    | zapatillas     |
    | pelota tennis  |


