Feature: Internal Mail

    Scenario: Success sending message in internal mail (2a)
        Given a user accesses the internal mail page (2a)
        When the user submits a message with a valid receiver, subject and message body (2a)
        Then it should see "Email sent successfully!" (2a)

    Scenario: Attempting to submit without a mandatory field in internal mail (2b)
        Given a user accesses the internal mail page (2b)
        When the user sends a message with at least one mandatory field unfilled (2b)
        Then it should see "Campo Obrigatório" next to the fields that have not been filled in (2b)
