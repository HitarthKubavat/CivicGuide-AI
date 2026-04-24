from datetime import datetime, timedelta

class ElectionLogic:
    def __init__(self):
        # Multi-language dictionary for voter journey (6 actual ECI steps)
        self.journey_data = {
            "en": {
                "first_time_steps": [
                    {"title": "Application Submission", "desc": "Submit Form 6 online or offline with age/address proof.", "details": "<p class='mb-2'>Choose the correct form for your need:</p><ul class='list-disc pl-5 space-y-1'><li><b>Form 6:</b> For new voters.</li><li><b>Form 8:</b> For corrections.</li><li><b>Form 6A:</b> For NRIs.</li></ul><p class='mt-2 text-xs text-slate-500'>Note: Accepted file formats are JPG/PDF (Max 2MB).</p>"},
                    {"title": "BLO Assignment", "desc": "Application is assigned to a Booth Level Officer (BLO).", "details": "<p>A <b>Booth Level Officer (BLO)</b> is a local government official. They will physically visit your home to verify your identity and residence details.</p>"},
                    {"title": "Field Verification", "desc": "BLO conducts field verification of the submitted details.", "details": "<p class='mb-2'>The BLO will perform a rigorous 3-point check:</p><ul class='list-disc pl-5 space-y-1'><li><b>Physical address verification:</b> Ensuring you live there.</li><li><b>Document original checking:</b> Verifying uploaded proofs.</li><li><b>Signature matching:</b> Confirming your identity.</li></ul>"},
                    {"title": "ERO Review", "desc": "Electoral Registration Officer reviews verification report and makes a decision.", "details": "<p>The <b>Electoral Registration Officer (ERO)</b> reviews the BLO's report. The ERO makes the final legal decision to officially add your name to the <b>Electoral Roll</b>.</p>"},
                    {"title": "EPIC Generation", "desc": "Electoral Photo Identity Card (EPIC) number is generated.", "details": "<p>You can download your e-EPIC immediately once the number is generated from the official voter portal.</p>"},
                    {"title": "ID Card Delivery", "desc": "Physical EPIC is delivered via speed post.", "details": "<p>It usually takes 2-4 weeks after EPIC generation to receive the physical card at your registered address.</p>"}
                ],
                "existing_voter_steps": [
                    {"title": "Check Name in Voter List", "desc": "Verify your name in the electoral roll using your EPIC number.", "details": "<p>Ensure your polling station details are correct before election day.</p>"},
                    {"title": "Update Details (Form 8)", "desc": "Submit Form 8 for any corrections, shifting of residence, or replacing EPIC.", "details": "<p>Form 8 also works if you are shifting within the same constituency.</p>"},
                    {"title": "Aadhaar Linking (Form 6B)", "desc": "Voluntarily link your Aadhaar card with your voter ID for authentication.", "details": "<p>This helps in removing duplicate entries in the electoral roll.</p>"},
                    {"title": "Download e-EPIC", "desc": "Download a digital copy of your Voter ID from the official portal.", "details": "<p>e-EPIC is equally valid as a physical card for voting purposes.</p>"}
                ]
            },
            "hi": {
                "first_time_steps": [
                    {"title": "आवेदन जमा करना", "desc": "आयु/पता प्रमाण के साथ फॉर्म 6 ऑनलाइन या ऑफलाइन जमा करें।", "details": "<p class='mb-2'>अपनी आवश्यकता के अनुसार सही फॉर्म चुनें:</p><ul class='list-disc pl-5 space-y-1'><li><b>फॉर्म 6:</b> नए मतदाताओं के लिए।</li><li><b>फॉर्म 8:</b> सुधार के लिए।</li><li><b>फॉर्म 6A:</b> अनिवासी भारतीयों (NRI) के लिए।</li></ul><p class='mt-2 text-xs text-slate-500'>नोट: स्वीकृत फ़ाइल स्वरूप JPG/PDF (अधिकतम 2MB) हैं।</p>"},
                    {"title": "BLO असाइनमेंट", "desc": "आवेदन बूथ लेवल ऑफिसर (BLO) को सौंपा जाता है।", "details": "<p><b>बूथ लेवल ऑफिसर (BLO)</b> एक स्थानीय सरकारी अधिकारी होता है। वे आपकी पहचान और निवास विवरण को सत्यापित करने के लिए आपके घर का भौतिक रूप से दौरा करेंगे।</p>"},
                    {"title": "क्षेत्र सत्यापन", "desc": "BLO जमा किए गए विवरणों का क्षेत्र सत्यापन करता है।", "details": "<p class='mb-2'>BLO एक अनिवार्य 3-बिंदु जांच करेगा:</p><ul class='list-disc pl-5 space-y-1'><li><b>भौतिक पता सत्यापन:</b> यह सुनिश्चित करना कि आप वहां रहते हैं।</li><li><b>मूल दस्तावेज़ की जांच:</b> अपलोड किए गए प्रमाणों का सत्यापन।</li><li><b>हस्ताक्षर मिलान:</b> आपकी पहचान की पुष्टि।</li></ul>"},
                    {"title": "ERO समीक्षा", "desc": "निर्वाचक पंजीकरण अधिकारी सत्यापन रिपोर्ट की समीक्षा करता है और निर्णय लेता है।", "details": "<p><b>निर्वाचक पंजीकरण अधिकारी (ERO)</b> BLO की रिपोर्ट की समीक्षा करता है। ERO आधिकारिक तौर पर आपका नाम <b>मतदाता सूची (Electoral Roll)</b> में जोड़ने का अंतिम कानूनी निर्णय लेता है।</p>"},
                    {"title": "EPIC जनरेशन", "desc": "इलेक्टोरल फोटो आइडेंटिटी कार्ड (EPIC) नंबर जनरेट होता है।", "details": "<p>नंबर जनरेट होते ही आप आधिकारिक मतदाता पोर्टल से तुरंत अपना e-EPIC डाउनलोड कर सकते हैं।</p>"},
                    {"title": "ID कार्ड डिलीवरी", "desc": "भौतिक EPIC स्पीड पोस्ट के माध्यम से वितरित किया जाता है।", "details": "<p>EPIC जनरेशन के बाद आपके पंजीकृत पते पर भौतिक कार्ड प्राप्त करने में आमतौर पर 2-4 सप्ताह लगते हैं।</p>"}
                ],
                "existing_voter_steps": [
                    {"title": "वोटर लिस्ट में नाम जांचें", "desc": "अपने EPIC नंबर का उपयोग करके मतदाता सूची में अपना नाम सत्यापित करें।", "details": "<p>सुनिश्चित करें कि चुनाव के दिन से पहले आपके मतदान केंद्र का विवरण सही है।</p>"},
                    {"title": "विवरण अपडेट करें (फॉर्म 8)", "desc": "किसी भी सुधार, निवास बदलने या EPIC बदलने के लिए फॉर्म 8 जमा करें।", "details": "<p>यदि आप उसी निर्वाचन क्षेत्र में शिफ्ट हो रहे हैं तो फॉर्म 8 भी काम करता है।</p>"},
                    {"title": "आधार लिंकिंग (फॉर्म 6B)", "desc": "प्रमाणीकरण के लिए स्वेच्छा से अपने आधार कार्ड को अपने वोटर आईडी से लिंक करें।", "details": "<p>यह मतदाता सूची में डुप्लिकेट प्रविष्टियों को हटाने में मदद करता है।</p>"},
                    {"title": "e-EPIC डाउनलोड करें", "desc": "आधिकारिक पोर्टल से अपने वोटर आईडी की एक डिजिटल प्रति डाउनलोड करें।", "details": "<p>e-EPIC मतदान उद्देश्यों के लिए भौतिक कार्ड के समान ही मान्य है।</p>"}
                ]
            },
            "mr": {
                "first_time_steps": [
                    {"title": "अर्ज सबमिशन", "desc": "वय/पत्त्याच्या पुराव्यासह फॉर्म 6 ऑनलाइन किंवा ऑफलाइन सबमिट करा.", "details": "<p class='mb-2'>तुमच्या गरजेनुसार योग्य फॉर्म निवडा:</p><ul class='list-disc pl-5 space-y-1'><li><b>फॉर्म 6:</b> नवीन मतदारांसाठी.</li><li><b>फॉर्म 8:</b> दुरुस्तीसाठी.</li><li><b>फॉर्म 6A:</b> अनिवासी भारतीयांसाठी (NRI).</li></ul><p class='mt-2 text-xs text-slate-500'>टीप: स्वीकारलेले फाइल फॉरमॅट JPG/PDF (कमाल 2MB) आहेत.</p>"},
                    {"title": "BLO असाइनमेंट", "desc": "अर्ज बूथ लेव्हल ऑफिसर (BLO) कडे सोपवला जातो.", "details": "<p><b>बूथ लेव्हल ऑफिसर (BLO)</b> हे स्थानिक सरकारी अधिकारी असतात. तुमची ओळख आणि निवासाचा तपशील पडताळण्यासाठी ते प्रत्यक्ष तुमच्या घरी भेट देतील.</p>"},
                    {"title": "क्षेत्र पडताळणी", "desc": "BLO सबमिट केलेल्या तपशीलांची क्षेत्र पडताळणी करते.", "details": "<p class='mb-2'>BLO अनिवार्य ३-बिंदू तपासणी करेल:</p><ul class='list-disc pl-5 space-y-1'><li><b>प्रत्यक्ष पत्ता पडताळणी:</b> तुम्ही तिथेच राहता याची खात्री करणे.</li><li><b>मूळ कागदपत्रांची तपासणी:</b> अपलोड केलेल्या पुराव्यांची पडताळणी.</li><li><b>स्वाक्षरी जुळवणे:</b> तुमच्या ओळखीची पुष्टी.</li></ul>"},
                    {"title": "ERO पुनरावलोकन", "desc": "निवडणूक नोंदणी अधिकारी पडताळणी अहवालाचे पुनरावलोकन करतात आणि निर्णय घेतात.", "details": "<p><b>निवडणूक नोंदणी अधिकारी (ERO)</b> BLO च्या अहवालाचे पुनरावलोकन करतात. तुमचे नाव अधिकृतपणे <b>मतदार यादीत (Electoral Roll)</b> समाविष्ट करण्याचा अंतिम कायदेशीर निर्णय ERO घेतात.</p>"},
                    {"title": "EPIC जनरेशन", "desc": "इलेक्टोरल फोटो आयडेंटिटी कार्ड (EPIC) क्रमांक तयार होतो.", "details": "<p>नंबर तयार झाल्यानंतर तुम्ही अधिकृत मतदार पोर्टलवरून तुमचे e-EPIC लगेच डाउनलोड करू शकता.</p>"},
                    {"title": "ID कार्ड वितरण", "desc": "भौतिक EPIC स्पीड पोस्टद्वारे वितरित केले जाते.", "details": "<p>EPIC जनरेशन नंतर तुमच्या नोंदणीकृत पत्त्यावर भौतिक कार्ड प्राप्त होण्यासाठी साधारणपणे 2-4 आठवडे लागतात.</p>"}
                ],
                "existing_voter_steps": [
                    {"title": "मतदार यादीत नाव तपासा", "desc": "तुमचा EPIC क्रमांक वापरून मतदार यादीतील तुमचे नाव सत्यापित करा.", "details": "<p>निवडणुकीच्या दिवसापूर्वी तुमच्या मतदान केंद्राचे तपशील योग्य असल्याची खात्री करा.</p>"},
                    {"title": "तपशील अपडेट करा (फॉर्म 8)", "desc": "कोणतीही सुधारणा, निवासस्थान बदलणे किंवा EPIC बदलण्यासाठी फॉर्म 8 सबमिट करा.", "details": "<p>तुम्ही त्याच मतदारसंघात स्थलांतर करत असल्यास फॉर्म 8 देखील काम करतो.</p>"},
                    {"title": "आधार लिंकिंग (फॉर्म 6B)", "desc": "प्रमाणीकरणासाठी तुमची आधार कार्ड तुमच्या मतदार ओळखपत्राशी स्वेच्छेने लिंक करा.", "details": "<p>यामुळे मतदार यादीतील डुप्लिकेट नोंदी काढण्यात मदत होते.</p>"},
                    {"title": "e-EPIC डाउनलोड करा", "desc": "अधिकृत पोर्टलवरून तुमच्या मतदार ओळखपत्राची डिजिटल प्रत डाउनलोड करा.", "details": "<p>e-EPIC मतदानासाठी भौतिक कार्डाइतकेच वैध आहे.</p>"}
                ]
            },
            "gu": {
                "first_time_steps": [
                    {"title": "અરજી સબમિશન", "desc": "વય/સરનામાના પુરાવા સાથે ફોર્મ 6 ઓનલાઇન અથવા ઑફલાઇન સબમિટ કરો.", "details": "<p class='mb-2'>તમારી જરૂરિયાત મુજબ યોગ્ય ફોર્મ પસંદ કરો:</p><ul class='list-disc pl-5 space-y-1'><li><b>ફોર્મ 6:</b> નવા મતદારો માટે.</li><li><b>ફોર્મ 8:</b> સુધારા માટે.</li><li><b>ફોર્મ 6A:</b> બિન-નિવાસી ભારતીયો (NRI) માટે.</li></ul><p class='mt-2 text-xs text-slate-500'>નોંધ: સ્વીકૃત ફાઇલ ફોર્મેટ્સ JPG/PDF (મહત્તમ 2MB) છે.</p>"},
                    {"title": "BLO સોંપણી", "desc": "અરજી બૂથ લેવલ ઓફિસર (BLO) ને સોંપવામાં આવે છે.", "details": "<p><b>બૂથ લેવલ ઓફિસર (BLO)</b> એ સ્થાનિક સરકારી અધિકારી છે. તેઓ તમારી ઓળખ અને રહેઠાણની વિગતો ચકાસવા માટે રૂબરૂ તમારા ઘરની મુલાકાત લેશે.</p>"},
                    {"title": "ક્ષેત્ર ચકાસણી", "desc": "BLO સબમિટ કરેલી વિગતોની ક્ષેત્ર ચકાસણી કરે છે.", "details": "<p class='mb-2'>BLO ફરજિયાત 3-પોઇન્ટ ચેક કરશે:</p><ul class='list-disc pl-5 space-y-1'><li><b>ભૌતિક સરનામાંની ચકાસણી:</b> ખાતરી કરવી કે તમે ત્યાં રહો છો.</li><li><b>મૂળ દસ્તાવેજ ચકાસણી:</b> અપલોડ કરેલા પુરાવાઓની ચકાસણી.</li><li><b>સહી મેચિંગ:</b> તમારી ઓળખની પુષ્ટિ.</li></ul>"},
                    {"title": "ERO સમીક્ષા", "desc": "ચૂંટણી નોંધણી અધિકારી ચકાસણી રિપોર્ટની સમીક્ષા કરે છે અને નિર્ણય લે છે.", "details": "<p><b>ચૂંટણી નોંધણી અધિકારી (ERO)</b> BLO ના રિપોર્ટની સમીક્ષા કરે છે. તમારું નામ સત્તાવાર રીતે <b>મતદાર યાદી (Electoral Roll)</b> માં ઉમેરવાનો અંતિમ કાનૂની નિર્ણય ERO લે છે.</p>"},
                    {"title": "EPIC જનરેશન", "desc": "ઈલેક્ટોરલ ફોટો આઈડેન્ટિટી કાર્ડ (EPIC) નંબર જનરેટ થાય છે.", "details": "<p>નંબર જનરેટ થયા પછી તરત જ તમે સત્તાવાર મતદાર પોર્ટલ પરથી તમારું e-EPIC ડાઉનલોડ કરી શકો છો.</p>"},
                    {"title": "ID કાર્ડ વિતરણ", "desc": "ભૌતિક EPIC સ્પીડ પોસ્ટ દ્વારા વિતરિત કરવામાં આવે છે.", "details": "<p>EPIC જનરેશન પછી તમારા નોંધાયેલા સરનામા પર ભૌતિક કાર્ડ મેળવવામાં સામાન્ય રીતે 2-4 અઠવાડિયા લાગે છે.</p>"}
                ],
                "existing_voter_steps": [
                    {"title": "મતદાર યાદીમાં નામ તપાસો", "desc": "તમારા EPIC નંબરનો ઉપયોગ કરીને મતદાર યાદીમાં તમારું નામ ચકાસો.", "details": "<p>ખાતરી કરો કે ચૂંટણીના દિવસ પહેલા તમારા મતદાન મથકની વિગતો સાચી છે.</p>"},
                    {"title": "વિગતો અપડેટ કરો (ફોર્મ 8)", "desc": "કોઈપણ સુધારા, રહેઠાણ બદલવા અથવા EPIC બદલવા માટે ફોર્મ 8 સબમિટ કરો.", "details": "<p>જો તમે તે જ મતવિસ્તારમાં સ્થળાંતર કરી રહ્યાં હોવ તો ફોર્મ 8 પણ કામ કરે છે.</p>"},
                    {"title": "આધાર લિંકિંગ (ફોર્મ 6B)", "desc": "પ્રમાણીકરણ માટે સ્વેચ્છાએ તમારા આધાર કાર્ડને તમારા મતદાર ID સાથે લિંક કરો.", "details": "<p>આ મતદાર યાદીમાં ડુપ્લિકેટ એન્ટ્રીઓને દૂર કરવામાં મદદ કરે છે.</p>"},
                    {"title": "e-EPIC ડાઉનલોડ કરો", "desc": "અધિકૃત પોર્ટલ પરથી તમારા મતદાર ID ની ડિજિટલ નકલ ડાઉનલોડ કરો.", "details": "<p>e-EPIC મતદાન હેતુઓ માટે ભૌતિક કાર્ડ જેટલું જ માન્ય છે.</p>"}
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

