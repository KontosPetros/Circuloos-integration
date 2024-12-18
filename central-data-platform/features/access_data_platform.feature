

Feature: Access Protected Resources

  Scenario: Authenticate and access resources
    Given the service is running
    When I authenticate as a partner
    Then I should have access to protected resources
    And the resource response should contain expected version information