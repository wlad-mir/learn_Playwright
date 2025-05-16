from playwright.sync_api import Page, expect
import re


def test_one(page: Page):
    page.goto('https://google.pl/')
    search_field = page.get_by_role('combobox')
    search_field.fill('cat')
    search_field.press('Enter')
    expect(page).to_have_title(re.compile('^cat'))

def test_by_role(page: Page):
    page.goto('https://magento.softwaretestingboard.com/')
    page.get_by_role('menuitem',name='What`s New').click()
    page.get_by_role('link', name='Search Terms').click()

def test_by_text(page: Page):
    page.goto('https://qa-practice.com/')
    page.get_by_text('Single UI Element').click()

def test_by_label(page: Page):
    page.goto('https://qa-practice.com/elements/input/simple')
    page.get_by_label('Text string').fill('Margot')

def test_by_placeholder(page: Page):
    page.goto('https://qa-practice.com/elements/input/simple')
    page.get_by_placeholder('Submit me').fill('Fedorargot')

def test_by_alt_text(page: Page):
    page.goto('https://epam.com/')
    page.get_by_alt_text('The Next Evolution of Software Engineering').click()

def test_by_title(page: Page):
    page.goto('https://google.pl/')
    page.get_by_title('Szukaj').fill('cat')

def test_by_test_id(page: Page):
    page.goto('https://www.airbnb.com')
    page.get_by_test_id('header-tab-search-block-tab-EXPERIENCES').click()

def test_by_css_selector(page: Page):
    page.goto('https://magento.softwaretestingboard.com/')
    page.locator('.showcart').click()

def test_by_xpath(page: Page):
    page.goto('https://magento.softwaretestingboard.com/')
    page.locator('//*[@class="action showcart"]').click()

def test_by_label(page: Page):
    page.goto('https://qa-practice.com/elements/input/simple')
    field = page.get_by_label('Text string')
    field.press_sequentially('Szabzudin', delay=500)
    field.press('Control+a')
    field.press('Backspace')






