Feature: Internal Mail

    Scenario: Success sending message in internal mail (1a)
        Given a user accesses the internal mail page (1a)
        When the user submits a message with a valid receiver, subject and message body (1a)
        Then it should see "Email sent successfully!" (1a)

    Scenario: Attempting to submit without a mandatory field in internal mail (1b)
        Given a user accesses the internal mail page (1b)
        When the user sends a message with at least one mandatory field unfilled (1b)
        Then it should see "Required Field" next to the fields that have not been filled in (1b)