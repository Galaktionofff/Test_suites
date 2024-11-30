import unittest
import suite_12_3

RunTS = unittest.TestSuite()
RunTS.addTest(unittest.TestLoader().loadTestsFromTestCase(suite_12_3.TestTournament))
RunTS.addTest(unittest.TestLoader().loadTestsFromTestCase(suite_12_3.RunnerTest))

runner = unittest.TextTestRunner(verbosity=2)
runner.run(RunTS)
