class Login:
    def __init__(self,name, surname, login):
        self.name = name
        self.surname = surname
        self.login = login
    def info(self):
        return self.name, self.surname, self.login
    def is_employee(self):
        return True


class Authorization(Login):
    def __init__(self,name, surname, login, password, hash_algorithm, is_hashed = False):
        super().__init__(name, surname, login)
        self.password = password
        self.hash_algorithm = hash_algorithm
        self.is_hashed = is_hashed
    def hashing_pass(self):
        import hashlib
        if self.hash_algorithm == 'sha256':
            self.password = hashlib.sha256(self.password.encode('utf-8')).hexdigest()
        elif self.hash_algorithm == 'md5':
            self.password = hashlib.md5(self.password.encode('utf-8')).hexdigest()
        else:
            self.password = hashlib.sha256(self.password.encode('utf-8')).hexdigest()
        self.is_hashed = True
        return self.password
    def info(self):
        if self.is_hashed != True:
            self.hashing_pass(self)
        return self.password, self.hash_algorithm, self.is_hashed
