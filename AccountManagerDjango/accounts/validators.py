from rest_framework.exceptions import ValidationError

def validate_mail(data):
    if not data.get('name') or not data.get('email'):
        raise ValidationError("Username and email are required for mail device.")

def validate_mobile(data):
    if not data.get('phone'):
        raise ValidationError("Phone number is required for mobile device.")

def validate_web(data):
    if not data.get('surname') or not data.get('name') \
            or not data.get('patronymic') or not data.get('birth_date') \
            or not data.get('passport_number') or not data.get('birth_place') \
            or not data.get('phone') or not data.get('registration_address'):
        raise ValidationError("Phone number is required for mobile device.")