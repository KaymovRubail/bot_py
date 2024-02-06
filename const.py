FirstCaption=('Hello {name}!\n'
              'I am your bot')
Userinfo=('Nickname: {name}\n'
          'Bio: {bio}\n'
          'Age: {age}\n'
          'Zodiac: {z}\n'
          'Gender: {gender}\n'
          'Best color: {bestcolor}\n'
          )from aiogram import executor

from config import dp
from database import ddbb
from handlers import start, qustions, group_filter, for_admin, registration, feedback_offers, profile, complaints, \
    reference, check


async def on_startup(_):
    data=ddbb.Database()
    data.create_table()
start.register_start_handler(dp=dp)
qustions.register_ask(dp=dp)
profile.registr_edit_profile(dp=dp)
complaints.register_complaints(dp=dp)
feedback_offers.register_fo(dp=dp)
registration.registr_reg_handler(dp=dp)
reference.register_referrence(dp=dp)
check.register_check_system(dp=dp)
# scrap.register_scrap(dp=dp)
# openaiii.register_openai(dp=dp)
for_admin.register_admin(dp=dp)
group_filter.register_group_filter(dp=dp)
if __name__ == '__main__':
    executor.start_polling(
        dp, skip_updates=True,
        on_startup=on_startup
    )