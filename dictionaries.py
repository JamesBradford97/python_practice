#A key-value pair system
#Seems like JSON

month_Conversions={
    "Jan": "January",
    "Feb": "Febraury",
    "Mar": "March",
    "Apr":"April",
    "May":"May",
    "Jun":"June",
    "Jul":"July",
    "Aug":"August",
    "Sep":"September",
    "Oct":"October",
    "Nov":"November",
    "Dec":"December",
}

print(month_Conversions["Apr"])

print(month_Conversions.get("Jan"))

print(month_Conversions.get("Kay", "Not a valid key")) #Specifying a fall back output in case key doesn't exist