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
        missing_fields = []
        if not data.get('surname'):
            missing_fields.append('surname')
        if not data.get('name'):
            missing_fields.append('name')
        if not data.get('patronymic'):
            missing_fields.append('patronymic')
        if not data.get('birth_date'):
            missing_fields.append('birth_date')
        if not data.get('passport_number'):
            missing_fields.append('passport_number')
        if not data.get('birth_place'):
            missing_fields.append('birth_place')
        if not data.get('phone'):
            missing_fields.append('phone')
        if not data.get('registration_address'):
            missing_fields.append('registration_address')

        raise ValidationError(f"The following fields are required: {', '.join(missing_fields)}")