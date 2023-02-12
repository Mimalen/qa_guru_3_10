import os
import time

from allure import severity, story, link, feature, label, tag, step
from allure_commons.types import Severity
from selene.support.conditions import be, have
from decorator import setup_browser


def fill_form(browser, data):
    ids = list(data.keys())
    values = list(data.values())
    for i in range(len(ids)):
        browser.element(ids[i]).should(be.blank).type(values[i])
    browser.element('label[for=gender-radio-2]').click()
    browser.element('#dateOfBirthInput').click()
    browser.element('.react-datepicker__month-select').type('June')
    browser.element('.react-datepicker__year-select').type('1999')
    browser.element('.react-datepicker__day--015').click()
    browser.element('label[for=hobbies-checkbox-1]').click()
    browser.element('label[for=hobbies-checkbox-2]').click()
    browser.element('#uploadPicture') \
        .set_value(
        os.path.abspath(
            os.path.join(
                os.path.dirname(__file__),
                'merry.jpg'
            )
        )
    )
    browser.element('')
    browser.element('#react-select-3-input').type('NCR').press_enter()
    browser.element('#react-select-4-input').type('Noida').press_enter()
    browser.element('#submit').press_enter()

def validate_form(browser, *args):
    browser.element('.table').all('td').even.should(have.texts(args))

@tag('web')
@label('owner', 'Mimalen')
@severity(Severity.NORMAL)
@feature('Filling the form')
@story('Selene')
@link('https://demoqa.com/automation-practice-form', name='test')
def test_submitting_form(setup_browser):
    datum = {
        '#firstName': 'Jul',
        '#lastName': 'Krv',
        '#userEmail': 'julkrv@test.co',
        '#userNumber': '1234567890',
        '#subjectsInput': 'qwerty',
        '#currentAddress': 'Pushkin street, Kolotushkin building, 123 apt'
    }

    with step("Заполнение формы регистрации"):
        fill_form(setup_browser, datum)


    with step('Валидация заполнения'):
        validate_form(
            setup_browser,
            full_name(datum),
            datum['#userEmail'],
            'Female',
            '1234567890',
            '15 June,1999',
            '',
            'Sports, Reading',
            'merry.jpg',
            'Pushkin street, Kolotushkin building, 123 apt',
            'NCR Noida'
        )

    setup_browser.quit()


def full_name(data):
    return f"{data['#firstName']} {data['#lastName']}"