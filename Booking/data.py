headers_create_booking = {
    "Content-Type": "application/json",
}

user_body = {
    "firstname" : "",
    "lastname" : "",
    "totalprice" : 1,
    "depositpaid" : True,
    "bookingdates" : {
        "checkin" : "2018-01-01",
        "checkout" : "2019-01-01"
    },
    "additionalneeds" : "Breakfast"
}

# VALORES PRUEBA
# Firstname - Valor de prueba 1
first_name_0_letter = ""

# Firstname - Valor de prueba 2
first_name_special_symbol = "!$%&?%#"

# Firstname - Valor de prueba 3
first_name_numbers = "123"

# Firstname - Valor de prueba 4
first_name_number_type = 12

# Lastname - Valor de prueba 5
last_name_0_letter = ""

# Lastname - Valor de prueba 6
last_name_special_symbol = "!$%&?%#"

# Lastname - Valor de prueba 7
last_name_numbers = "123"

# Lastname - Valor de prueba 8
last_name_number_type = 12

# Total Price - Valor de prueba 9
total_price_empty = ""

# Total Price - Valor de prueba 10
total_price_string = "cien"

# Checkin - Valor de prueba 11
check_in_different_format = "2018/01/01"

# Checkout - Valor de prueba 12
check_out_different_format = "2019/01/01"