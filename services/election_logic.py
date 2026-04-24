from datetime import datetime, timedelta

class ElectionLogic:
    def __init__(self):
        # Multi-language dictionary for voter journey (6 actual ECI steps)
        self.journey_data = {
            "en": {
                "first_time_steps": [
                    {"title": "Application Submission", "desc": "Submit Form 6 online or offline with age/address proof.", "pro_tip": "Required documents: Aadhar, Age Proof (Birth Certificate/10th Marksheet)."},
                    {"title": "BLO Assignment", "desc": "Application is assigned to a Booth Level Officer (BLO).", "pro_tip": "Keep your phone handy, the BLO will contact you for verification."},
                    {"title": "Field Verification", "desc": "BLO conducts field verification of the submitted details.", "pro_tip": "Be present at the address with original documents during the visit."},
                    {"title": "ERO Review", "desc": "Electoral Registration Officer reviews verification report and makes a decision.", "pro_tip": "Track your application status on the Voter Helpline app using your reference ID."},
                    {"title": "EPIC Generation", "desc": "Electoral Photo Identity Card (EPIC) number is generated.", "pro_tip": "You can download your e-EPIC immediately once the number is generated."},
                    {"title": "ID Card Delivery", "desc": "Physical EPIC is delivered via speed post.", "pro_tip": "It usually takes 2-4 weeks after EPIC generation to receive the physical card."}
                ],
                "existing_voter_steps": [
                    {"title": "Check Name in Voter List", "desc": "Verify your name in the electoral roll using your EPIC number.", "pro_tip": "Ensure your polling station details are correct."},
                    {"title": "Update Details (Form 8)", "desc": "Submit Form 8 for any corrections, shifting of residence, or replacing EPIC.", "pro_tip": "Form 8 also works if you are shifting within the same constituency."},
                    {"title": "Aadhaar Linking (Form 6B)", "desc": "Voluntarily link your Aadhaar card with your voter ID for authentication.", "pro_tip": "This helps in removing duplicate entries in the electoral roll."},
                    {"title": "Download e-EPIC", "desc": "Download a digital copy of your Voter ID from the official portal.", "pro_tip": "e-EPIC is equally valid as a physical card for voting."}
                ]
            },
            "hi": {
                "first_time_steps": [
                    {"title": "आवेदन जमा करना", "desc": "आयु/पता प्रमाण के साथ फॉर्म 6 ऑनलाइन या ऑफलाइन जमा करें।", "pro_tip": "आवश्यक दस्तावेज़: आधार, आयु प्रमाण (जन्म प्रमाण पत्र/10वीं की मार्कशीट)।"},
                    {"title": "BLO असाइनमेंट", "desc": "आवेदन बूथ लेवल ऑफिसर (BLO) को सौंपा जाता है।", "pro_tip": "अपना फोन पास रखें, BLO सत्यापन के लिए आपसे संपर्क करेगा।"},
                    {"title": "क्षेत्र सत्यापन", "desc": "BLO जमा किए गए विवरणों का क्षेत्र सत्यापन करता है।", "pro_tip": "दौरे के दौरान मूल दस्तावेजों के साथ पते पर उपस्थित रहें।"},
                    {"title": "ERO समीक्षा", "desc": "निर्वाचक पंजीकरण अधिकारी सत्यापन रिपोर्ट की समीक्षा करता है और निर्णय लेता है।", "pro_tip": "अपने संदर्भ आईडी का उपयोग करके वोटर हेल्पलाइन ऐप पर अपनी आवेदन स्थिति ट्रैक करें।"},
                    {"title": "EPIC जनरेशन", "desc": "इलेक्टोरल फोटो आइडेंटिटी कार्ड (EPIC) नंबर जनरेट होता है।", "pro_tip": "नंबर जनरेट होते ही आप तुरंत अपना e-EPIC डाउनलोड कर सकते हैं।"},
                    {"title": "ID कार्ड डिलीवरी", "desc": "भौतिक EPIC स्पीड पोस्ट के माध्यम से वितरित किया जाता है।", "pro_tip": "EPIC जनरेशन के बाद भौतिक कार्ड प्राप्त करने में आमतौर पर 2-4 सप्ताह लगते हैं।"}
                ],
                "existing_voter_steps": [
                    {"title": "वोटर लिस्ट में नाम जांचें", "desc": "अपने EPIC नंबर का उपयोग करके मतदाता सूची में अपना नाम सत्यापित करें।", "pro_tip": "सुनिश्चित करें कि आपके मतदान केंद्र का विवरण सही है।"},
                    {"title": "विवरण अपडेट करें (फॉर्म 8)", "desc": "किसी भी सुधार, निवास बदलने या EPIC बदलने के लिए फॉर्म 8 जमा करें।", "pro_tip": "यदि आप उसी निर्वाचन क्षेत्र में शिफ्ट हो रहे हैं तो फॉर्म 8 भी काम करता है।"},
                    {"title": "आधार लिंकिंग (फॉर्म 6B)", "desc": "प्रमाणीकरण के लिए स्वेच्छा से अपने आधार कार्ड को अपने वोटर आईडी से लिंक करें।", "pro_tip": "यह मतदाता सूची में डुप्लिकेट प्रविष्टियों को हटाने में मदद करता है।"},
                    {"title": "e-EPIC डाउनलोड करें", "desc": "आधिकारिक पोर्टल से अपने वोटर आईडी की एक डिजिटल प्रति डाउनलोड करें।", "pro_tip": "e-EPIC मतदान के लिए भौतिक कार्ड के समान ही मान्य है।"}
                ]
            },
            "mr": {
                "first_time_steps": [
                    {"title": "अर्ज सबमिशन", "desc": "वय/पत्त्याच्या पुराव्यासह फॉर्म 6 ऑनलाइन किंवा ऑफलाइन सबमिट करा.", "pro_tip": "आवश्यक कागदपत्रे: आधार, वयाचा पुरावा (जन्म प्रमाणपत्र/10वीची मार्कशीट)."},
                    {"title": "BLO असाइनमेंट", "desc": "अर्ज बूथ लेव्हल ऑफिसर (BLO) कडे सोपवला जातो.", "pro_tip": "तुमचा फोन जवळ ठेवा, BLO पडताळणीसाठी तुमच्याशी संपर्क साधेल."},
                    {"title": "क्षेत्र पडताळणी", "desc": "BLO सबमिट केलेल्या तपशीलांची क्षेत्र पडताळणी करते.", "pro_tip": "भेटीदरम्यान मूळ कागदपत्रांसह पत्त्यावर उपस्थित रहा."},
                    {"title": "ERO पुनरावलोकन", "desc": "निवडणूक नोंदणी अधिकारी पडताळणी अहवालाचे पुनरावलोकन करतात आणि निर्णय घेतात.", "pro_tip": "तुमचा संदर्भ आयडी वापरून व्होटर हेल्पलाइन अॅपवर तुमच्या अर्जाची स्थिती ट्रॅक करा."},
                    {"title": "EPIC जनरेशन", "desc": "इलेक्टोरल फोटो आयडेंटिटी कार्ड (EPIC) क्रमांक तयार होतो.", "pro_tip": "नंबर तयार झाल्यानंतर तुम्ही तुमचे e-EPIC लगेच डाउनलोड करू शकता."},
                    {"title": "ID कार्ड वितरण", "desc": "भौतिक EPIC स्पीड पोस्टद्वारे वितरित केले जाते.", "pro_tip": "EPIC जनरेशन नंतर भौतिक कार्ड प्राप्त होण्यासाठी साधारणपणे 2-4 आठवडे लागतात."}
                ],
                "existing_voter_steps": [
                    {"title": "मतदार यादीत नाव तपासा", "desc": "तुमचा EPIC क्रमांक वापरून मतदार यादीतील तुमचे नाव सत्यापित करा.", "pro_tip": "तुमच्या मतदान केंद्राचे तपशील योग्य असल्याची खात्री करा."},
                    {"title": "तपशील अपडेट करा (फॉर्म 8)", "desc": "कोणतीही सुधारणा, निवासस्थान बदलणे किंवा EPIC बदलण्यासाठी फॉर्म 8 सबमिट करा.", "pro_tip": "तुम्ही त्याच मतदारसंघात स्थलांतर करत असल्यास फॉर्म 8 देखील काम करतो."},
                    {"title": "आधार लिंकिंग (फॉर्म 6B)", "desc": "प्रमाणीकरणासाठी तुमची आधार कार्ड तुमच्या मतदार ओळखपत्राशी स्वेच्छेने लिंक करा.", "pro_tip": "यामुळे मतदार यादीतील डुप्लिकेट नोंदी काढण्यात मदत होते."},
                    {"title": "e-EPIC डाउनलोड करा", "desc": "अधिकृत पोर्टलवरून तुमच्या मतदार ओळखपत्राची डिजिटल प्रत डाउनलोड करा.", "pro_tip": "e-EPIC मतदानासाठी भौतिक कार्डाइतकेच वैध आहे."}
                ]
            },
            "gu": {
                "first_time_steps": [
                    {"title": "અરજી સબમિશન", "desc": "વય/સરનામાના પુરાવા સાથે ફોર્મ 6 ઓનલાઇન અથવા ઑફલાઇન સબમિટ કરો.", "pro_tip": "જરૂરી દસ્તાવેજો: આધાર, વયનો પુરાવો (જન્મ પ્રમાણપત્ર/10માની માર્કશીટ)."},
                    {"title": "BLO સોંપણી", "desc": "અરજી બૂથ લેવલ ઓફિસર (BLO) ને સોંપવામાં આવે છે.", "pro_tip": "તમારો ફોન હાથવગો રાખો, BLO ચકાસણી માટે તમારો સંપર્ક કરશે."},
                    {"title": "ક્ષેત્ર ચકાસણી", "desc": "BLO સબમિટ કરેલી વિગતોની ક્ષેત્ર ચકાસણી કરે છે.", "pro_tip": "મુલાકાત દરમિયાન અસલ દસ્તાવેજો સાથે સરનામા પર હાજર રહો."},
                    {"title": "ERO સમીક્ષા", "desc": "ચૂંટણી નોંધણી અધિકારી ચકાસણી રિપોર્ટની સમીક્ષા કરે છે અને નિર્ણય લે છે.", "pro_tip": "તમારા રેફરન્સ આઈડીનો ઉપયોગ કરીને વોટર હેલ્પલાઈન એપ પર તમારી અરજીનું સ્ટેટસ ટ્રેક કરો."},
                    {"title": "EPIC જનરેશન", "desc": "ઈલેક્ટોરલ ફોટો આઈડેન્ટિટી કાર્ડ (EPIC) નંબર જનરેટ થાય છે.", "pro_tip": "નંબર જનરેટ થયા પછી તરત જ તમે તમારું e-EPIC ડાઉનલોડ કરી શકો છો."},
                    {"title": "ID કાર્ડ વિતરણ", "desc": "ભૌતિક EPIC સ્પીડ પોસ્ટ દ્વારા વિતરિત કરવામાં આવે છે.", "pro_tip": "EPIC જનરેશન પછી ભૌતિક કાર્ડ મેળવવામાં સામાન્ય રીતે 2-4 અઠવાડિયા લાગે છે."}
                ],
                "existing_voter_steps": [
                    {"title": "મતદાર યાદીમાં નામ તપાસો", "desc": "તમારા EPIC નંબરનો ઉપયોગ કરીને મતદાર યાદીમાં તમારું નામ ચકાસો.", "pro_tip": "ખાતરી કરો કે તમારા મતદાન મથકની વિગતો સાચી છે."},
                    {"title": "વિગતો અપડેટ કરો (ફોર્મ 8)", "desc": "કોઈપણ સુધારા, રહેઠાણ બદલવા અથવા EPIC બદલવા માટે ફોર્મ 8 સબમિટ કરો.", "pro_tip": "જો તમે તે જ મતવિસ્તારમાં સ્થળાંતર કરી રહ્યાં હોવ તો ફોર્મ 8 પણ કામ કરે છે."},
                    {"title": "આધાર લિંકિંગ (ફોર્મ 6B)", "desc": "પ્રમાણીકરણ માટે સ્વેચ્છાએ તમારા આધાર કાર્ડને તમારા મતદાર ID સાથે લિંક કરો.", "pro_tip": "આ મતદાર યાદીમાં ડુપ્લિકેટ એન્ટ્રીઓને દૂર કરવામાં મદદ કરે છે."},
                    {"title": "e-EPIC ડાઉનલોડ કરો", "desc": "અધિકૃત પોર્ટલ પરથી તમારા મતદાર ID ની ડિજિટલ નકલ ડાઉનલોડ કરો.", "pro_tip": "e-EPIC મતદાન માટે ભૌતિક કાર્ડ જેટલું જ માન્ય છે."}
                ]
            }
        }
        
    def get_voter_journey(self, language: str = "en", first_time: bool = True) -> dict:
        """Returns the voter journey steps in the specified language."""
        lang = language.lower()
        if lang not in self.journey_data:
            lang = "en" # fallback to English
            
        key = "first_time_steps" if first_time else "existing_voter_steps"
        return {"steps": self.journey_data[lang][key]}

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
