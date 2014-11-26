Feature: Rent CD web application to be able to checkout cd
		As a clerk I wish to be able to checkout cd's
		for customers

Scenario: To be able to checkout cd
		Given I visit the checkout page
                When I enter the customer id "001" and cd id "1"
                Then I see a rental contract "Air (001) rented Twila Paris Hits (1) Rental Due: 11/26/2014" 