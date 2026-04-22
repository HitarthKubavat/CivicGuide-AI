from datetime import datetime, timedelta

class ElectionLogic:
    def __init__(self):
        # Multi-language dictionary for voter journey (6 actual ECI steps)
        self.journey_data = {
            "en": {
                "steps": [
                    {"title": "Application Submission", "desc": "Submit Form 6 online or offline with age/address proof."},
                    {"title": "BLO Assignment", "desc": "Application is assigned to a Booth Level Officer (BLO)."},
                    {"title": "Field Verification", "desc": "BLO conducts field verification of the submitted details."},
                    {"title": "ERO Review", "desc": "Electoral Registration Officer reviews verification report and makes a decision."},
                    {"title": "EPIC Generation", "desc": "Electoral Photo Identity Card (EPIC) number is generated."},
                    {"title": "ID Card Delivery", "desc": "Physical EPIC is delivered via speed post."}
                ]
            },
            "gu": {
                "steps": [
                    {"title": "અરજી સબમિશન", "desc": "વય/સરનામાના પુરાવા સાથે ફોર્મ 6 ઓનલાઇન અથવા ઑફલાઇન સબમિટ કરો."},
                    {"title": "BLO સોંપણી", "desc": "અરજી બૂથ લેવલ ઓફિસર (BLO) ને સોંપવામાં આવે છે."},
                    {"title": "ક્ષેત્ર ચકાસણી", "desc": "BLO સબમિટ કરેલી વિગતોની ક્ષેત્ર ચકાસણી કરે છે."},
                    {"title": "ERO સમીક્ષા", "desc": "ચૂંટણી નોંધણી અધિકારી ચકાસણી રિપોર્ટની સમીક્ષા કરે છે અને નિર્ણય લે છે."},
                    {"title": "EPIC જનરેશન", "desc": "ઈલેક્ટોરલ ફોટો આઈડેન્ટિટી કાર્ડ (EPIC) નંબર જનરેટ થાય છે."},
                    {"title": "ID કાર્ડ વિતરણ", "desc": "ભૌતિક EPIC સ્પીડ પોસ્ટ દ્વારા વિતરિત કરવામાં આવે છે."}
                ]
            }
        }
        
    def get_voter_journey(self, language: str = "en") -> dict:
        """Returns the voter journey steps in the specified language."""
        lang = language.lower()
        if lang not in self.journey_data:
            lang = "en" # fallback to English
            
        return self.journey_data[lang]

    def get_timeline(self, city: str) -> dict:
        """Returns a dummy timeline for the specified city."""
        city = city.title()
        now = datetime.now()
        
        # Generating dummy dates - keeping it realistic intervals
        notification_date = now + timedelta(days=15)
        nomination_deadline = notification_date + timedelta(days=10)
        polling_date = nomination_deadline + timedelta(days=20)
        counting_date = polling_date + timedelta(days=5)
        
        return {
            "location": city,
            "notification_date": notification_date.strftime("%Y-%m-%d"),
            "nomination_deadline": nomination_deadline.strftime("%Y-%m-%d"),
            "polling_date": polling_date.strftime("%Y-%m-%d"),
            "counting_date": counting_date.strftime("%Y-%m-%d")
        }
