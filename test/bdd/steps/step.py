from lettuce import *
from nose.tools import assert_equal, assert_in
from webtest import TestApp

from checkout_app import app

@step(u'Given I visit the checkout page')
def given_i_visit_the_checkout_page(step):
    world.browser = TestApp(app)
    world.response = world.browser.get('http://localhost:5000/')
    assert_equal(world.response.status_code, 200)
    #assert_equal(world.response.text, u'Hello World!')

@step(u'When I enter the customer id "([^"]*)" and cd id "([^"]*)"')
def when_i_enter_the_customer_id_group1_cd_id_group2(step, customer_id, cd_id):
    form = world.response.forms['account-form']
    form['customer_id'] = customer_id
    form['cd_id'] = cd_id
    world.form_response = form.submit()
    assert_equal(world.form_response.status_code, 200)

@step(u'Then I see a rental contract "([^"]*)"')
def then_i_see_a_rental_contract(step, rental_contract):
    assert_in ("Rental Contract: {}".format(rental_contract),
    world.form_response.text)