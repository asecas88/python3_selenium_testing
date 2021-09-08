import behave

def after_scenario(context, scenario):

    context.browser.close()
    context.browser.quit()

def after_all(context):

    print("THIS PROGRAM IS FINISHED")
