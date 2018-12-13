import unittest
import get_launch

class TestGetLaunchInfo(unittest.TestCase):
	# Test the get_launch_info function from get_launch.py

	def test_get_wrong_launch_info(self):
		result = get_launch.get_launch_info('next2')
		self.assertIsNone(result)
	def test_get_right_launch_info(self):
		result = get_launch.get_launch_info('next')
		self.assertIsNotNone(result)

class TestPrintLaunchInformation(unittest.TestCase):
	# Test the print_launch_information function from get_launch.py

	def test_get_wrong_launch_information(self):
		# Test with wrong url
		launch = get_launch.get_launch_info('next2')
		result = get_launch.print_launch_information(launch)
		self.assertIsNone(result)

	def test_get_right_launch_information(self):
		# Test with right url
		launch = get_launch.get_launch_info('next')
		result = get_launch.print_launch_information(launch)
		self.assertIsNotNone(result)

class TestPrintLaunchesInformation(unittest.TestCase):
	# Test the print_launches_information function from get_launch.py

	def test_get_wrong_launch_information(self):
		# Test with wrong url
		launch = get_launch.get_launch_info('upcoming2')
		result = get_launch.print_launches_information(launch)
		self.assertIsNone(result)

	def test_get_right_launch_information(self):
		# Test with right url
		launch = get_launch.get_launch_info('upcoming')
		result = get_launch.print_launches_information(launch)
		self.assertIsNotNone(result)

class TestPrintInformation(unittest.TestCase):
	# Test the print_information function from get_launch.py
	def test_print_with_1(self):
		# Test with input 1
		original_input = __builtins__.input
		__builtins__.input = lambda _: '1'
		result = get_launch.print_information()
		__builtins__.input = original_input
		self.assertEqual(result, 1)

	def test_print_with_2(self):
		# Test with input 2
		original_input = __builtins__.input
		__builtins__.input = lambda _: '2'
		result = get_launch.print_information()
		__builtins__.input = original_input
		self.assertEqual(result, 2)

	def test_print_with_3(self):
		# Test with input 3
		original_input = __builtins__.input
		__builtins__.input = lambda _: '3'
		result = get_launch.print_information()
		__builtins__.input = original_input
		self.assertEqual(result, 3)

	def test_print_with_4(self):
		# Test with input 4
		original_input = __builtins__.input
		__builtins__.input = lambda _: '4'
		result = get_launch.print_information()
		__builtins__.input = original_input
		self.assertEqual(result, 4)

	def test_print_with_5(self):
		# Test with input 5 (invalid)
		original_input = __builtins__.input
		__builtins__.input = lambda _: '5'
		result = get_launch.print_information()
		__builtins__.input = original_input
		self.assertEqual(result, -1)

if __name__ == '__main__':
	unittest.main()