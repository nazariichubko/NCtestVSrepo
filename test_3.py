import time
from NCtestVSrepo.wp_tests.website import TestWebsite

with TestWebsite(teardown=True) as bot:
    bot.navigate_to_users_login_page()
    bot.enter_registered_user_credentials()
    bot.verify_user_is_logged_in_successfully()
    time.sleep(5)
#  bot.log_out_from_account()
#  time.sleep((5))
    bot.quit()