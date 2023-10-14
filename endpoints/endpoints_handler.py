class Endpoint:
    status = None

    def check_response_status_is_ok(self):
        assert self.status == 200
