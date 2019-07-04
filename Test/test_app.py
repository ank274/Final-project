from app.Project import to_usd

def test_to_usd():
    result = to_usd(20)
    assert result == "${0:,.2f}".format(20)
