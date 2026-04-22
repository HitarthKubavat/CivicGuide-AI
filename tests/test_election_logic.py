import unittest
from services.election_logic import ElectionLogic

class TestElectionLogic(unittest.TestCase):
    def setUp(self):
        self.logic = ElectionLogic()

    def test_get_voter_journey_english(self):
        journey = self.logic.get_voter_journey("en")
        self.assertIn("steps", journey)
        self.assertEqual(len(journey["steps"]), 6)
        self.assertEqual(journey["steps"][0]["title"], "Application Submission")

    def test_get_voter_journey_gujarati(self):
        journey = self.logic.get_voter_journey("gu")
        self.assertIn("steps", journey)
        self.assertEqual(len(journey["steps"]), 6)
        self.assertEqual(journey["steps"][0]["title"], "અરજી સબમિશન")
        
    def test_get_voter_journey_fallback(self):
        journey = self.logic.get_voter_journey("es")
        self.assertEqual(journey["steps"][0]["title"], "Application Submission")

    def test_get_timeline_dates_exist(self):
        timeline = self.logic.get_timeline("Ahmedabad")
        self.assertEqual(timeline["location"], "Ahmedabad")
        self.assertIn("notification_date", timeline)
        self.assertIn("nomination_deadline", timeline)
        self.assertIn("polling_date", timeline)
        self.assertIn("counting_date", timeline)

if __name__ == '__main__':
    unittest.main()
