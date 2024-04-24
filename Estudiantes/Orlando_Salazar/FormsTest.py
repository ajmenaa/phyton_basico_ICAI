import pyform
from pyform.controls import ControlText, ControlButton

class SimpleExample1(pyform.BaseWidget):
    def __init__(self):
        super().__init__('Simple Example 1')
        self._firstname = ControlText('First name', 'Default value')
        self._middlename = ControlText('Middle name')
        self._lastname = ControlText('Last name')
        self._fullname = ControlText('Full name')
        self._button = ControlButton('Press this button')
        self._button.value = self.__button_action

    def __button_action(self):
        self._fullname.value = f"{self._firstname.value} {self._middlename.value} {self._lastname.value}"

if __name__ == "__main__":
    pyform.start_app(SimpleExample1)