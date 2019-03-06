from pycbrf import ExchangeRates, Banks
import time


def money_status(status):
    current_data = str(str(time.localtime()[0]) + "-0" + str(time.localtime()[1]) + "-" + str(time.localtime()[2]))
    yesterday = str(str(time.localtime()[0]) + "-0" + str(time.localtime()[1] - 1) + "-" + str(time.localtime()[2]))
    rates = ExchangeRates(current_data, locale_en=False)
    rates_yesterday = ExchangeRates(yesterday, locale_en=False)
    flag_list = ("🇦🇺", "🇦🇿", "🇬🇧", "🇬🇪", "🇧🇾", "🇧🇬", "🇧🇷", "🇭🇺", "🇭🇰",
                 "🇩🇰",  "🇺🇸", "💶", "🇮🇳", "🇰🇿", "🇨🇦", "🇰🇬", "🇨🇳", "🇲🇩",
                 "🇳🇴", "🇵🇱", "🇷🇴", "", "🇸🇬", "🇹🇯", "🇹🇷", "🇹🇲", "🇺🇿",
                 "🇺🇦", "🇨🇿", "🇸🇪", "🇸🇪", "🇿🇦", "🇰🇷", "🇯🇵")
    flag = 0

    msg_text_money = ""
    if status == 'ALL':
        for rate in rates.rates:
            value_money = float((rates[rate.code].value - rates_yesterday[rate.code].value))
            if value_money < 0:
                msg_text_money = msg_text_money + (flag_list[flag]+(str(rates[rate.code].name) + " " +
                                                        ("%.2f" % rates[rate.code].value) + " руб." + " 🔻" + str(value_money)) + "\n")
            elif value_money >= 0:
                msg_text_money = msg_text_money + (flag_list[flag]+str(rates[rate.code].name) + " " +
                                    ("%.2f" % rates[rate.code].value) + " руб." + " 🔺+" + str(value_money)+ "\n")
            flag += 1
    else:
        if status == 'USD':
            flag = 10
        elif status == 'EUR':
            flag = 11
        value_money = float((rates[status].value - rates_yesterday[status].value))
        if value_money < 0:
            msg_text_money = msg_text_money + (flag_list[flag] + (str(rates[status].name) + " " +
                                                                  ("%.2f" % rates
                                                                      [status].value) + " руб." + " 🔻" + str(
                value_money)) + "\n")
        elif value_money >= 0:
            msg_text_money = msg_text_money + (flag_list[flag] + str(rates[status].name) + " " +
                                               ("%.2f" % rates[status].value) + " руб." + " 🔺+" + str(
                value_money) + "\n")

    return msg_text_money

"""
current_data = str(str(time.localtime()[0]) + "-0" + str(time.localtime()[1]) + "-" + str(time.localtime()[2]))
rates = ExchangeRates(current_data, locale_en=False)
for i in rates.rates:
    print(rates[i.code].code)
"""