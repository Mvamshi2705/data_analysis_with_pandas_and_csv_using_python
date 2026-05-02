import csv

data=[
["Taj Mahal", "White marble mausoleum built by Shah Jahan", "Uttar Pradesh", "Agra", 27.1751, 78.0421, 1632, "Mughal Empire"],
    ["Red Fort", "Historic Mughal fort in Delhi", "Delhi", "Delhi", 28.6562, 77.2410, 1648, "Mughal Empire"],
    ["Qutub Minar", "Tall brick minaret and UNESCO site", "Delhi", "Delhi", 28.5244, 77.1855, 1193, "Delhi Sultanate"],
    ["Hampi", "Ancient ruins of Vijayanagara Empire", "Karnataka", "Hampi", 15.3350, 76.4600, 1336, "Vijayanagara Empire"],
    ["Konark Sun Temple", "13th century architectural Sun temple", "Odisha", "Konark", 19.8876, 86.0945, 1250, "Eastern Ganga Dynasty"],
    ["Ajanta Caves", "Buddhist cave monuments", "Maharashtra", "Aurangabad", 20.5519, 75.7033, -200, "Satavahana Dynasty"],
    ["Ellora Caves", "Rock cut cave temples", "Maharashtra", "Aurangabad", 20.0268, 75.1790, 600, "Rashtrakuta Dynasty"],
    ["Mysore Palace", "Royal palace of Mysore kingdom", "Karnataka", "Mysore", 12.3052, 76.6552, 1912, "Wadiyar Dynasty"],
    ["Gateway of India", "Monument from British period", "Maharashtra", "Mumbai", 18.9220, 72.8347, 1924, "British Raj"],
    ["Charminar", "Historic mosque and monument", "Telangana", "Hyderabad", 17.3616, 78.4747, 1591, "Qutb Shahi Dynasty"],
    ["India Gate", "War memorial in New Delhi", "Delhi", "Delhi", 28.6129, 77.2295, 1931, "British Raj"],
    ["Sanchi Stupa", "Ancient Buddhist stupa", "Madhya Pradesh", "Sanchi", 23.4793, 77.7397, -300, "Maurya Dynasty"],
    ["Fatehpur Sikri", "Former Mughal capital city", "Uttar Pradesh", "Agra", 27.0945, 77.6678, 1571, "Mughal Empire"],
    ["Gol Gumbaz", "Mausoleum of Mohammed Adil Shah", "Karnataka", "Vijayapura", 16.8302, 75.7100, 1656, "Adil Shahi Dynasty"],
    ["Victoria Memorial", "British era memorial building", "West Bengal", "Kolkata", 22.5448, 88.3426, 1921, "British Raj"],
    ["Meenakshi Temple", "Famous Dravidian temple", "Tamil Nadu", "Madurai", 9.9195, 78.1193, 1623, "Nayak Dynasty"],
    ["Amer Fort", "Magnificent Rajput fort", "Rajasthan", "Jaipur", 26.9855, 75.8513, 1592, "Rajput Dynasty"],
    ["Jaisalmer Fort", "Golden sandstone fort", "Rajasthan", "Jaisalmer", 26.9124, 70.9120, 1156, "Rajput Dynasty"],
    ["Nalanda University", "Ancient center of learning", "Bihar", "Nalanda", 25.1367, 85.4449, 427, "Gupta Empire"],
    ["Mahabalipuram", "Stone carved shore temples", "Tamil Nadu", "Chennai", 12.6208, 80.1945, 700, "Pallava Dynasty"],
    ["Khajuraho Temples", "Temples with sculptures", "Madhya Pradesh", "Khajuraho", 24.8318, 79.9199, 950, "Chandela Dynasty"],
    ["Rani ki Vav", "Historic stepwell", "Gujarat", "Patan", 23.8587, 72.1018, 1063, "Solanki Dynasty"],
    ["Brihadeeswara Temple", "UNESCO Chola temple", "Tamil Nadu", "Thanjavur", 10.7828, 79.1318, 1010, "Chola Dynasty"],
    ["Sun Temple Modhera", "Temple dedicated to Sun God", "Gujarat", "Modhera", 23.6000, 72.1333, 1026, "Solanki Dynasty"],
    ["Humayun Tomb", "Mughal garden tomb", "Delhi", "Delhi", 28.5933, 77.2507, 1570, "Mughal Empire"]
]

with open("india_historical_places.csv", "w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerow(["Place","Description","State","City","Latitude","Longitude","YearBuilt","Dynasty"])
    writer.writerows(data)

print("CSV file created sucessfully")