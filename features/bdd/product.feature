Feature: Check tools product

    Scenario: Retrieve product inventory
        Given the product inventory endpoint
        When sending a request to get product inventory
        Then the inventory retrieval is successful
        And the response contains the expected product data