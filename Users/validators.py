from django.core.exceptions import ValidationError

class CustomPasswordValidator:
    def validate(self, password, user=None):
        if not any(c.isdigit() for c in password):
            raise ValidationError("Пароль должен содержать как минимум одну цифру")
    
    def get_help_text(self):
        return "Пароль должен содержать как минимум одну цифру"

