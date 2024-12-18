from behave import given, when, then
import logging


@given("the service is running")
def step_impl(context):
    logging.debug(f"Connecting to host: { context.online_config['HOST']}")





@when("I authenticate as a partner")
def step_impl(context):
    logging.debug(f"Authenticating with username: { context.online_config['PARTNER_USERNAME']} and password: { context.online_config['PARTNER_PASSWORD']}")

@then("I should have access to protected resources")
def step_impl(context):
    logging.debug(f"Using ORIONzxczczx secret: {context.online_config['ORION_PEP_SECRET']}")
    logging.debug(f"Using MIKTAKA secret: {  context.online_config['MIKTAKA_PEP_SECRET'] }")
