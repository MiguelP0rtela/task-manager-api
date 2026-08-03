def validate_password(value: str) -> str:
    errors = []

    if len(value) < 8:
        errors.append("at least 8 characters")

    if not any(char.isupper() for char in value):
        errors.append("one uppercase letter")

    if not any(char.islower() for char in value):
        errors.append("one lowercase letter")

    if not any(char.isdigit() for char in value):
        errors.append("one number")

    if not any(not char.isalnum() for char in value):
        errors.append("one special character")

    if errors:
        raise ValueError(
            "Password must contain: " + ", ".join(errors)
        )

    return value