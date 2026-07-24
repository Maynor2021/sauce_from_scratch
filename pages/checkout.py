from pages.base_pages import BasePage

class CheckoutPage(BasePage):
    FIRST_NAME_INPUT = "#first-name"
    LAST_NAME_INPUT = "#last-name"
    POSTAL_CODE_INPUT = "#postal-code"
    CONTINUE_BUTTON = "#continue"
    FINISH_BUTTON= "#finish"
    COMPLETE_MESSAGE = ".complete-header"
    
    def fill_checkout_info(self, first_name, last_name, postal_code):
        self.page.fill(self.FIRST_NAME_INPUT, first_name)
        self.page.fill(self.LAST_NAME_INPUT, last_name)
        self.page.fill(self.POSTAL_CODE_INPUT, postal_code)
        
    def click_continue(self):
        self.page.click(self.CONTINUE_BUTTON)
        
    def click_finish(self):
        self.page.click(self.FINISH_BUTTON)
        
        
    def get_confirmation_message(self):
        return self.page.text_content(self.COMPLETE_MESSAGE    )
    