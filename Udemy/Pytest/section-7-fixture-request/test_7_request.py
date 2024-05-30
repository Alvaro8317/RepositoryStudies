import sqlite3


def test_request_setup_teardown(request, fixture_function):
    print(request)  # Debug para saber que tiene request
    db = sqlite3.connect("../section-3-tests-anatomy/test.db")

    def finalize_connection():
        db.close()

    request.addfinalizer(finalize_connection)
    return db
# Pytest recomienda más hacer el setup y teardown con yield
