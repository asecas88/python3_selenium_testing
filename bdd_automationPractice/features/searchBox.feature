Feature: Search box

Scenario Outline: The user search a word

    Given the user is in main page
    When the user search '<item>'
    Then the user should see '<item>' title

Examples:

    | item     |
    | dresses  |
    | t-shirts |
    | shoes    |
    | blouses  |
