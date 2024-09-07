import configuration
import requests
import data

# Crear nueva reserva
def create_new_booking(body):
    return (requests.post(configuration.URL_SERVICE + configuration.CREATE_BOOKING_PATH,
                         json=body, headers=data.headers_create_booking))
    
response_create = create_new_booking(data.user_body)
print(response_create.status_code)

def get_name_user_body(first_name):
    current_body = data.user_body.copy()
    current_body["firstname"] = first_name
    return current_body

def get_lastname_user_body(last_name):
    current_body = data.user_body.copy()
    current_body["lastname"] = last_name
    return current_body

def get_total_price_user_body(total_price):
    current_body = data.user_body.copy()
    current_body["totalprice"] = total_price
    return current_body

def get_deposit_paid_price_user_body(deposit_paid):
    current_body = data.user_body.copy()
    current_body["depositpaid"] = deposit_paid
    return current_body

def get_check_in_price_user_body(check_in):
    current_body = data.user_body.copy()
    current_body["checkin"] = check_in
    return current_body

def get_check_out_price_user_body(check_out):
    current_body = data.user_body.copy()
    current_body["checkout"] = check_out
    return current_body

def get_additional_needs_price_user_body(additional_needs):
    current_body = data.user_body.copy()
    current_body["additionalneeds"] = additional_needs
    return current_body

# Firstname -> Función de prueba negativa para confirmar que hay errores por introducir valores incorrectos
def negative_assert_test_first_name(first_name):
    booking_response = create_new_booking(get_name_user_body(first_name))

    assert booking_response.status_code != 200
    print(booking_response.status_code)

# Lastname -> Función de prueba negativa para confirmar que hay errores por introducir valores incorrectos
def negative_assert_test_last_name(last_name):
    booking_response = create_new_booking(get_name_user_body(last_name))

    assert booking_response.status_code != 200

# Total price -> Función de prueba negativa para confirmar que hay errores por introducir valores incorrectos
def negative_assert_test_total_price(total_price):
    booking_response = create_new_booking(get_name_user_body(total_price))

    assert booking_response.status_code != 200

# Checkin -> Función de prueba negativa para confirmar que hay errores por introducir valores incorrectos
def negative_assert_test_check_in(check_in):
    booking_response = create_new_booking(get_name_user_body(check_in))

    assert booking_response.status_code != 200

# Checkout -> Función de prueba negativa para confirmar que hay errores por introducir valores incorrectos
def negative_assert_test_check_out(check_out):
    booking_response = create_new_booking(get_name_user_body(check_out))

    assert booking_response.status_code != 200

#  Prueba 1: campo firstname en blanco
def test_create_booking_first_name_0_letter_get_error_response():
    negative_assert_test_first_name(data.first_name_0_letter)

#  Prueba 2: campo firstname con símbolos
def test_create_booking_first_name_special_symbols_get_error_response():
    negative_assert_test_first_name(data.first_name_numbers)

#  Prueba 3: campo firstname con caracteres numéricos
def test_create_booking_first_name_numbers_get_error_response():
    negative_assert_test_first_name(data.first_name_numbers)

#  Prueba 4: campo firstname con valor tipo numérico
def test_create_booking_first_name_number_type_get_error_response():
    negative_assert_test_first_name(data.first_name_numbers)

#  Prueba 5: campo lastname en blanco
def test_create_booking_last_name_0_letter_get_error_response():
    negative_assert_test_last_name(data.last_name_0_letter)

#  Prueba 6: campo lastname con símbolos
def test_create_booking_last_name_special_symbols_get_error_response():
    negative_assert_test_last_name(data.last_name_numbers)

#  Prueba 7: campo lastname con caracteres numéricos
def test_create_booking_last_name_numbers_get_error_response():
    negative_assert_test_last_name(data.last_name_numbers)

#  Prueba 8: campo lastname con valor tipo numérico
def test_create_booking_last_name_number_type_get_error_response():
    negative_assert_test_last_name(data.first_name_numbers)

#  Prueba 9: campo totalprice en blanco
def test_create_booking_total_price_empty_get_error_response():
    negative_assert_test_total_price(data.total_price_empty)

#  Prueba 10: campo totalprice con cadena de texto
def test_create_booking_total_price_string_get_error_response():
    negative_assert_test_total_price(data.total_price_string)

#  Prueba 11: campo checkin con distinto formato
def test_create_booking_check_in_get_error_response():
    negative_assert_test_check_in(data.check_in_different_format)

#  Prueba 12: campo checkout con distinto formato
def test_create_booking_check_out_get_error_response():
    negative_assert_test_check_out(data.check_out_different_format)
