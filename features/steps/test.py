from behave import *

use_step_matcher("re")


@when("Go to https://www\.a1\.digital")
def open_index(context):
    context.web.open("https://www.a1.digital")

@when("accept all cookies")
def accept_cookies(context):
    context.web.find_element_by_id("onetrust-accept-btn-handler").click()


@when('go to "Lösungen" page')
def next_page(context):
    context.find_element_by_link_text("Lösungen").click()

@then('go to "Exoscale" page')
def last_page(context):
    context.find_element_by_link_text("Exoscale: Die Europäische Cloud Infrastruktur").click()



