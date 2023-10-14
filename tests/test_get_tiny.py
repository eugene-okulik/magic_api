def test_get_existing_url(create_tiny, url_getter_endp):
    code, long_url = create_tiny
    url_getter_endp.get_long_using_short(code)
    url_getter_endp.check_response_status_is_ok()
    url_getter_endp.check_stored_url_same_as_sent_url(long_url)

