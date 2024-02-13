from selene import browser, be, have


def test_search_selen():
    browser.open('/')
    browser.element('[name="q"]').should(be.blank).type('yashaka/selene').press_enter()
    browser.element('[id="search"]').should(have.text('Selene - User-oriented Web UI browser tests in Python'))


def test_search_no_results_google():
    browser.open('/')
    browser.element('[name="q"]').should(be.blank).type('vtuikej9').press_enter()
    browser.element('[class="card-section"]').should(have.text('Your search - vtuikej9 - did not match any documents.'))