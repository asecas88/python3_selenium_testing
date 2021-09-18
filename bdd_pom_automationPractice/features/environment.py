import behave


def after_scenario(context,scenario):

    context.browser.close()
    context.browser.quit()
