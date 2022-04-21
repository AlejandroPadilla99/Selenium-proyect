from booking.booking import Booking
try:
    with Booking() as bot:
        bot.land_first_page()
        #bot.change_currency(currency='GBP')
        bot.select_place_to_go('New York')
        bot.select_dates(check_in_date='2022-05-16', check_out_date='2022-05-23')
        bot.select_adults(10)
        bot.click_search()
        bot.apply_filtrations()
        bot.report_results()
        #print(len(bot.report_results()))

except Exception as e:
    if  'in PATH' in str(e):
        print("There is a problem running this program form command line interface")
    else:
        raise
