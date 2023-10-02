from BaseClass import BaseLoginClass


class TestLogin(BaseLoginClass):
    def test_loggin_con_log(self):
        log = self.get_logger()
        log.info("Prueba con Logger")
        print("Test")
