import unittest
import metApp

print("This check is currently a work in process.")

class TestApp(unittest.TestCase):

    def test_get_form(self):
        #self.assertEqual()

        #Checks: that flask app produces table as expected unless the starting year is after the ending year.
        result=metApp.get_form('All', -500000, 0, '5')
        print(result)


if __name__=="__main__":
    unittest.main()
