import time
from NCtestVSrepo.wp_tests.website import TestWebsite

with TestWebsite(teardown=True) as bot:
    bot.navigate_to_registration_page()
    bot.fill_registration_form()
    bot.verify_user_registration_is_successfull()
    time.sleep(5)
    bot.quit()