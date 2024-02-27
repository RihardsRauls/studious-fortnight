from .main import remover

def test_remover():
    assert remover("I miss my wife") == " mss my wf"
    assert remover("Why my dementia hasnt affected me as a person!") == "Why my dmnt hsnt ffctd m s  prsn"
    assert remover("digger") == "dggr"
    assert remover("AAAAAAAAAAAAAAAAAAAAAAAAA") == ""
    assert remover("QQQQQQQQQQQQQQQQ") == "QQQQQQQQQQQQQQQQ"
    assert remover("") == ""
    assert remover("This is a funny test") == "Ths s  fnny tst"
    assert remover("123123 AAA123") == "123123 123"
    assert remover("This is poggers") == "Ths s pggrs"
    assert remover("What are your thoughts on the geopolitical situation in kyrgyzstan") == "Wht r yr thghts n th gpltcl sttn n kyrgyzstn"
