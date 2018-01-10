# Messages are preset in this file

class Messages:
    # Greetings:
    # AfternoonBegin is time to switch from Morning to Afternoon greeting
    # AfternoonEnd is time to switch from Afternoon to Night greeting
    Morning = "Bom dia."
    Afternoon = "Boa tarde."
    Night = "Boa noite."
    AfternoonBegin = 12
    AfternoonEnd = 12

    # Hours:
    # Array that goes from beginning of day till end
    # intro_hour is format of how to say the hour. Hour goes in between
    intro_hour = ("São ", " horas")
    hours = ("10", "11", "12", "13", "14", "15", "16", "17", "18")

    # Meals:
    # Array includes hour of meal and reminder to be spoken
    Lunch = (11, "")
    Dinner = (17, "")

    # Days:
    # Array with all weekdays. day[0] = Monday ... day[6] = Sunday
    # intro_day is format of how to say day. Day goes in between
    intro_day = ("Hoje é ", ".")
    days = ("Segunda-Feira", "Terça-Feira", "Quarta-Feira", "Quinta-Feira", "Sexta-Feira", "Sábado", "Domingo")
