import os
from allure import severity, story, link, feature, label, tag
from allure_commons.types import Severity
import pytest
from selene.support.conditions import be, have
from decorator import handle_test_with_allure, open_demo

@handle_test_with_allure
def test_name(open_demo):
    open_demo.element('#firstName').should(be.blank).type('Jul')
    open_demo.element('#firstName').should(have.value('Jul'))
    open_demo.element('#lastName').should(be.blank).type('Krv')
    open_demo.element('#lastName').should(have.value('Krv'))

@handle_test_with_allure
def test_email(open_demo):
    open_demo.element('#userEmail').should(be.blank).type('julkrv@test.co')
    open_demo.element('#userEmail').should(have.value('julkrv@test.co'))

@handle_test_with_allure
def test_gender(open_demo):
    open_demo.element('label[for=gender-radio-2]').click()
    open_demo.element('label[for=gender-radio-2]').should(be.enabled)

@handle_test_with_allure
def test_mobile(open_demo):
    open_demo.element('#userNumber').should(be.blank).type('1234567890')
    open_demo.element('#userNumber').should(have.value('1234567890'))

@handle_test_with_allure
def test_birth_date(open_demo):
    open_demo.element('#dateOfBirthInput').click()
    open_demo.element('.react-datepicker__month-select').type('June')
    open_demo.element('.react-datepicker__year-select').type('1999')
    open_demo.element('.react-datepicker__day--015').click()
    open_demo.element('#dateOfBirthInput').should(have.value('15 Jun 1999'))

@tag('web')
@label('owner', 'Mimalen')
@severity(Severity.NORMAL)
@feature('Fill the form')
@story('Selene')
@link('https://demoqa.com/automation-practice-form', name='test')
@handle_test_with_allure
def test_subjects(open_demo):
    open_demo.element('#subjectsInput').should(be.blank).type('qwerty')
    open_demo.element('#subjectsInput').should(have.value('qwerty'))