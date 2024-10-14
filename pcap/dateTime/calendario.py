import calendar

class MyCalendar():
    def count_weekday_in_year(self, year, weekday):
        count = 0
        for month in range(1, 13):
            cal = calendar.monthcalendar(year, month)
            week = 0
            while week < len(cal):
                if cal[week][weekday] != 0:
                    count += 1
                week += 1
        return count

    def count_weekday_in_month(self, year, month, weekday):
        count = 0
        cal = calendar.monthcalendar(year, month)
        week = 0
        while week < len(cal):
            if cal[week][weekday] != 0:
                count += 1
            week += 1
        return count

    def count_weekday_in_month_range(self, year, month, weekday, start, end):
        count = 0
        cal = calendar.monthcalendar(year, month)
        week = 0
        while week < len(cal):
            if cal[week][weekday] != 0 and cal[week][weekday] >= start and cal[week][weekday] <= end:
                count += 1
            week += 1
        return count
    
    def count_weekday_in_year_range(self, year, weekday, start, end):
        count = 0
        for month in range(1, 13):
            cal = calendar.monthcalendar(year, month)
            week = 0
            while week < len(cal):
                if cal[week][weekday] != 0 and cal[week][weekday] >= start and cal[week][weekday] <= end:
                    count += 1
                week += 1
        return count
    
    def count_weekday_in_year_month(self, year, month, weekday, start, end):
        count = 0
        cal = calendar.monthcalendar(year, month)
        week = 0
        while week < len(cal):
            if cal[week][weekday] != 0 and cal[week][weekday] >= start and cal[week][weekday] <= end:
                count += 1
            week += 1
        return count

# Criação de uma instância da classe MyCalendar
my_cal = MyCalendar()

# Solicitar a entrada do usuário
year = int(input("Digite o ano: "))
month = int(input("Digite o mês (1-12): "))
weekday = int(input("Digite o dia da semana (0 = Segunda-feira, 6 = Domingo): "))
start = int(input("Digite o dia inicial do intervalo: "))
end = int(input("Digite o dia final do intervalo: "))

# Chamar os métodos com os valores fornecidos pelo usuário
count_year = my_cal.count_weekday_in_year(year, weekday)
count_month = my_cal.count_weekday_in_month(year, month, weekday)
count_month_range = my_cal.count_weekday_in_month_range(year, month, weekday, start, end)
count_year_range = my_cal.count_weekday_in_year_range(year, weekday, start, end)
count_year_month = my_cal.count_weekday_in_year_month(year, month, weekday, start, end)

# Imprimir os resultados
print(f"Número de vezes que o dia da semana {weekday} aparece no ano {year}: {count_year}")
print(f"Número de vezes que o dia da semana {weekday} aparece no mês {month} do ano {year}: {count_month}")
print(f"Número de vezes que o dia da semana {weekday} aparece no intervalo {start}-{end} do mês {month} do ano {year}: {count_month_range}")
print(f"Número de vezes que o dia da semana {weekday} aparece no intervalo {start}-{end} do ano {year}: {count_year_range}")
print(f"Número de vezes que o dia da semana {weekday} aparece no intervalo {start}-{end} do mês {month} do ano {year}: {count_year_month}")
