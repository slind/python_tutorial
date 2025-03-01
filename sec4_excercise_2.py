savings = 918

hourly_cost = 0.51
daily_cost = hourly_cost * 24
monthly_cost = 24*30

server_count = 20

print("Operating costs of one server per day ${0}".format(str(daily_cost)))
print("Operating costs of one server per month ${0}".format(str(monthly_cost)))

print("Operating costs of {0} server per day ${1}".format(str(server_count), str(daily_cost*server_count)))
print("Operating costs of {0} server per month ${1}".format(str(server_count), str(monthly_cost*20)))

print("My savings of ${0} will pay for {1} days of operation on af single server".format(str(savings), str(savings/daily_cost)))