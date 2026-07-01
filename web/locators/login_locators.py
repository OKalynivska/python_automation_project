from enum import Enum


class LoginLocators(Enum):
    EMAIL="[data-qa='login-email']"
    PASSWORD="[name='password']"
    LOGIN_BUTTON="[data-qa='login-button']"
    LOGIN_FORM=".login-form"
