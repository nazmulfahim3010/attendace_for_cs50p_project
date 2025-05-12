import pyfiglet  # type:ignore
import cowsay  # type:ignore

class Wellcome:
    def __init__(self):
        self._email_pass_error = Wellcome.tux_msg("user email and password is wrong")
        self._check_csv_existing_error = Wellcome.tux_msg("you already have an account please login\nyour email exist in our data")
        self._new_ac_welcome = Wellcome.figlet_msg("welcome \n your account has been created")
        self._verification_data_error_email = Wellcome.cow_msg("your email is not valid")
        self._verification_data_error_password = Wellcome.tux_msg("your password is not valid")
    
    @classmethod
    def tux_msg(cls, msg):
        return cowsay.tux(msg)
    
    @classmethod
    def figlet_msg(cls, msg):
        return pyfiglet.figlet_format(msg)

    @classmethod
    def cow_msg(cls, msg):
        return cowsay.cow(msg)


msg=Wellcome()
print(msg._check_csv_existing_error)

