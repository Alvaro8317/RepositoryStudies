class TestFixtures:

    def test_name(self, fix_name):
        assert fix_name == "Alvaro"

    def test_lastname(self, fix_lastname):
        assert fix_lastname == "Garzon"

    def test_datatype_dni(self, fix_dni):
        assert isinstance(fix_dni, int)