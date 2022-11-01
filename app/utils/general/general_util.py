class Utils():
    def validate_string(self, value):
        """Valid empty string"""
        if not isinstance(value, str):
            return False

        if str.strip(value) == "":
            return False
