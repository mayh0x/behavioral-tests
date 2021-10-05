Feature: Login

    Scenario: Login successfully (1a)
        Given a user accesses a login page (1a)
        When the user submits their data with correct username and password (1a)
        Then it must be redirected to a logged area (1a)

    Scenario: Login attempt with incorrect username and/or password (1b)
        Given a user accesses a login page (1b)
        When the user fills in the fields with incorrect username and/or password (1b)
        Then it should see “Invalid username and/or password. Please check your username and password and try again.” (1b)
