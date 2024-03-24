import unittest
from app import app

class TestApp(unittest.TestCase):

    # Test if the home page loads successfully
    def test_home_page_loads(self):
        tester = app.test_client(self)
        response = tester.get('/')
        self.assertEqual(response.status_code, 200)

    # Test if the body type page loads successfully
    def test_body_type_page_loads(self):
        tester = app.test_client(self)
        response = tester.get('/body-type')
        self.assertEqual(response.status_code, 200)

    # Test if the suggestion page loads successfully
    def test_suggest_page_loads(self):
        tester = app.test_client(self)
        response = tester.get('/suggest')
        self.assertEqual(response.status_code, 200)

    # Test if the test route for form submission loads successfully
    def test_test_route_loads(self):
        tester = app.test_client(self)
        response = tester.get('/testfile', data=dict(gender='male', skinColor='fair', occasion='casual', bodyType='medium', size='M'))
        self.assertEqual(response.status_code, 200)

    # Test if the form submission returns correct data
    def test_form_submission(self):
        tester = app.test_client(self)
        response = tester.post('/testfile', data=dict(gender='male', skinColor='fair', occasion='casual', bodyType='medium', size='M'))
        self.assertIn(b'male', response.data)
        self.assertIn(b'fair', response.data)
        self.assertIn(b'casual', response.data)
        self.assertIn(b'medium', response.data)
        self.assertIn(b'M', response.data)

    # Test if the index page calculates BSA correctly
    def test_bsa_calculation(self):
        tester = app.test_client(self)
        response = tester.post('/', data=dict(height='180', weight='70', gender='male'))
        self.assertIn(b'Large(L)', response.data)

    # Test if the index page handles wrong inputs correctly
    def test_wrong_inputs_handling(self):
        tester = app.test_client(self)
        response = tester.post('/', data=dict(height='abc', weight='def', gender='male'))
        self.assertIn(b'Wrong inputs', response.data)

    # Test if the predict Blueprint loads successfully
    def test_predict_blueprint_loads(self):
        tester = app.test_client(self)
        response = tester.get('/predict')
        self.assertEqual(response.status_code, 200)

    # Test if the blueprint route handles data correctly
    def test_predict_blueprint_data(self):
        tester = app.test_client(self)
        response = tester.post('/predict', data=dict(data='Some data'))
        self.assertIn(b'Some data', response.data)

    

if __name__ == '__main__':
    unittest.main()
