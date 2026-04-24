from datetime import datetime, timedelta

class ElectionLogic:
    def __init__(self):
        # Multi-language dictionary for voter journey (6 actual ECI steps)
        self.journey_data = {
            "en": {
                "first_time_steps": [
                    {"title": "Application Submission", "desc": "Submit Form 6 online or offline with age/address proof.", "details": "<p class='mb-2'><b>Required Documents:</b></p><ul class='list-disc pl-5 space-y-1 mb-2'><li><b>Age Proof:</b> Birth certificate, PAN card, Aadhaar, or 10th mark sheet.</li><li><b>Address Proof:</b> Aadhaar, Passport, Utility bill (water/electricity), or Bank passbook.</li><li><b>Photograph:</b> Recent passport-size colored photo.</li></ul><p class='mb-2'>Choose the correct form for your need:</p><ul class='list-disc pl-5 space-y-1'><li><b>Form 6:</b> For new voters.</li><li><b>Form 8:</b> For corrections.</li><li><b>Form 6A:</b> For NRIs.</li></ul><p class='mt-2 text-xs text-slate-500'>Note: Accepted file formats are JPG/PDF (Max 2MB).</p>"},
                    {"title": "BLO Assignment", "desc": "Application is assigned to a Booth Level Officer (BLO).", "details": "<p>A <b>Booth Level Officer (BLO)</b> is a local government official. They will physically visit your home to verify your identity and residence details.</p><p class='mt-2'><b>Official Procedure:</b></p><ul class='list-disc pl-5 space-y-1'><li>The application is printed and handed over to the respective BLO.</li><li>The BLO schedules a visit within 7-14 days.</li><li>Keep your original documents ready for inspection.</li></ul>"},
                    {"title": "Field Verification", "desc": "BLO conducts field verification of the submitted details.", "details": "<p class='mb-2'>The BLO will perform a rigorous 3-point check:</p><ul class='list-disc pl-5 space-y-1'><li><b>Physical address verification:</b> Ensuring you live there.</li><li><b>Document original checking:</b> Verifying uploaded proofs.</li><li><b>Signature matching:</b> Confirming your identity.</li></ul><p class='mt-2'><b>Required from you:</b> Present original ID and address proofs to the BLO and sign the verification report.</p>"},
                    {"title": "ERO Review", "desc": "Electoral Registration Officer reviews verification report and makes a decision.", "details": "<p>The <b>Electoral Registration Officer (ERO)</b> reviews the BLO's report. The ERO makes the final legal decision to officially add your name to the <b>Electoral Roll</b>.</p><p class='mt-2'><b>Official Procedure:</b></p><ul class='list-disc pl-5 space-y-1'><li>ERO conducts a final background check of the BLO report.</li><li>If approved, your name is published in the draft electoral roll.</li><li>After a statutory 7-day objection period, the final inclusion is processed.</li></ul>"},
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
                    {"title": "आवेदन जमा करना", "desc": "आयु/पता प्रमाण के साथ फॉर्म 6 ऑनलाइन या ऑफलाइन जमा करें।", "details": "<p class='mb-2'><b>आवश्यक दस्तावेज:</b></p><ul class='list-disc pl-5 space-y-1 mb-2'><li><b>आयु प्रमाण:</b> जन्म प्रमाण पत्र, पैन कार्ड, आधार, या 10वीं की मार्कशीट।</li><li><b>पता प्रमाण:</b> आधार, पासपोर्ट, उपयोगिता बिल (पानी/बिजली), या बैंक पासबुक।</li><li><b>तस्वीर:</b> हालिया पासपोर्ट आकार की रंगीन तस्वीर।</li></ul><p class='mb-2'>अपनी आवश्यकता के अनुसार सही फॉर्म चुनें:</p><ul class='list-disc pl-5 space-y-1'><li><b>फॉर्म 6:</b> नए मतदाताओं के लिए।</li><li><b>फॉर्म 8:</b> सुधार के लिए।</li><li><b>फॉर्म 6A:</b> अनिवासी भारतीयों (NRI) के लिए।</li></ul><p class='mt-2 text-xs text-slate-500'>नोट: स्वीकृत फ़ाइल स्वरूप JPG/PDF (अधिकतम 2MB) हैं।</p>"},
                    {"title": "BLO असाइनमेंट", "desc": "आवेदन बूथ लेवल ऑफिसर (BLO) को सौंपा जाता है।", "details": "<p><b>बूथ लेवल ऑफिसर (BLO)</b> एक स्थानीय सरकारी अधिकारी होता है। वे आपकी पहचान और निवास विवरण को सत्यापित करने के लिए आपके घर का भौतिक रूप से दौरा करेंगे।</p><p class='mt-2'><b>आधिकारिक प्रक्रिया:</b></p><ul class='list-disc pl-5 space-y-1'><li>आवेदन प्रिंट किया जाता है और संबंधित BLO को सौंपा जाता है।</li><li>BLO 7-14 दिनों के भीतर एक यात्रा निर्धारित करता है।</li><li>निरीक्षण के लिए अपने मूल दस्तावेज तैयार रखें।</li></ul>"},
                    {"title": "क्षेत्र सत्यापन", "desc": "BLO जमा किए गए विवरणों का क्षेत्र सत्यापन करता है।", "details": "<p class='mb-2'>BLO एक अनिवार्य 3-बिंदु जांच करेगा:</p><ul class='list-disc pl-5 space-y-1'><li><b>भौतिक पता सत्यापन:</b> यह सुनिश्चित करना कि आप वहां रहते हैं।</li><li><b>मूल दस्तावेज़ की जांच:</b> अपलोड किए गए प्रमाणों का सत्यापन।</li><li><b>हस्ताक्षर मिलान:</b> आपकी पहचान की पुष्टि।</li></ul><p class='mt-2'><b>आपसे आवश्यक:</b> BLO को मूल आईडी और पता प्रमाण प्रस्तुत करें और सत्यापन रिपोर्ट पर हस्ताक्षर करें।</p>"},
                    {"title": "ERO समीक्षा", "desc": "निर्वाचक पंजीकरण अधिकारी सत्यापन रिपोर्ट की समीक्षा करता है और निर्णय लेता है।", "details": "<p><b>निर्वाचक पंजीकरण अधिकारी (ERO)</b> BLO की रिपोर्ट की समीक्षा करता है। ERO आधिकारिक तौर पर आपका नाम <b>मतदाता सूची (Electoral Roll)</b> में जोड़ने का अंतिम कानूनी निर्णय लेता है।</p><p class='mt-2'><b>आधिकारिक प्रक्रिया:</b></p><ul class='list-disc pl-5 space-y-1'><li>ERO BLO रिपोर्ट की अंतिम पृष्ठभूमि जांच करता है।</li><li>यदि स्वीकृत हो जाता है, तो आपका नाम ड्राफ्ट मतदाता सूची में प्रकाशित किया जाता है।</li><li>7-दिवसीय वैधानिक आपत्ति अवधि के बाद, अंतिम प्रविष्टि संसाधित की जाती है।</li></ul>"},
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
            "gu": {
                "first_time_steps": [
                    {"title": "અરજી સબમિશન", "desc": "વય/સરનામાના પુરાવા સાથે ફોર્મ 6 ઓનલાઇન અથવા ઑફલાઇન સબમિટ કરો.", "details": "<p class='mb-2'><b>જરૂરી દસ્તાવેજો:</b></p><ul class='list-disc pl-5 space-y-1 mb-2'><li><b>ઉંમરનો પુરાવો:</b> જન્મ પ્રમાણપત્ર, પાન કાર્ડ, આધાર, અથવા 10માની માર્કશીટ.</li><li><b>સરનામાનો પુરાવો:</b> આધાર, પાસપોર્ટ, યુટિલિટી બિલ (પાણી/વીજળી), અથવા બેંક પાસબુક.</li><li><b>ફોટોગ્રાફ:</b> તાજેતરનો પાસપોર્ટ સાઇઝનો રંગીન ફોટો.</li></ul><p class='mb-2'>તમારી જરૂરિયાત મુજબ યોગ્ય ફોર્મ પસંદ કરો:</p><ul class='list-disc pl-5 space-y-1'><li><b>ફોર્મ 6:</b> નવા મતદારો માટે.</li><li><b>ફોર્મ 8:</b> સુધારા માટે.</li><li><b>ફોર્મ 6A:</b> બિન-નિવાસી ભારતીયો (NRI) માટે.</li></ul><p class='mt-2 text-xs text-slate-500'>નોંધ: સ્વીકૃત ફાઇલ ફોર્મેટ્સ JPG/PDF (મહત્તમ 2MB) છે.</p>"},
                    {"title": "BLO સોંપણી", "desc": "અરજી બૂથ લેવલ ઓફિસર (BLO) ને સોંપવામાં આવે છે.", "details": "<p><b>બૂથ લેવલ ઓફિસર (BLO)</b> એ સ્થાનિક સરકારી અધિકારી છે. તેઓ તમારી ઓળખ અને રહેઠાણની વિગતો ચકાસવા માટે રૂબરૂ તમારા ઘરની મુલાકાત લેશે.</p><p class='mt-2'><b>સત્તાવાર પ્રક્રિયા:</b></p><ul class='list-disc pl-5 space-y-1'><li>અરજી પ્રિન્ટ કરવામાં આવે છે અને સંબંધિત BLO ને સોંપવામાં આવે છે.</li><li>BLO 7-14 દિવસમાં મુલાકાતનું શેડ્યૂલ કરે છે.</li><li>નિરીક્ષણ માટે તમારા મૂળ દસ્તાવેજો તૈયાર રાખો.</li></ul>"},
                    {"title": "ક્ષેત્ર ચકાસણી", "desc": "BLO સબમિટ કરેલી વિગતોની ક્ષેત્ર ચકાસણી કરે છે.", "details": "<p class='mb-2'>BLO ફરજિયાત 3-પોઇન્ટ ચેક કરશે:</p><ul class='list-disc pl-5 space-y-1'><li><b>ભૌતિક સરનામાંની ચકાસણી:</b> ખાતરી કરવી કે તમે ત્યાં રહો છો.</li><li><b>મૂળ દસ્તાવેજ ચકાસણી:</b> અપલોડ કરેલા પુરાવાઓની ચકાસણી.</li><li><b>સહી મેચિંગ:</b> તમારી ઓળખની પુષ્ટિ.</li></ul><p class='mt-2'><b>તમારા તરફથી જરૂરી:</b> BLO ને મૂળ ID અને સરનામાના પુરાવા રજૂ કરો અને ચકાસણી રિપોર્ટ પર સહી કરો.</p>"},
                    {"title": "ERO સમીક્ષા", "desc": "ચૂંટણી નોંધણી અધિકારી ચકાસણી રિપોર્ટની સમીક્ષા કરે છે અને નિર્ણય લે છે.", "details": "<p><b>ચૂંટણી નોંધણી અધિકારી (ERO)</b> BLO ના રિપોર્ટની સમીક્ષા કરે છે. તમારું નામ સત્તાવાર રીતે <b>મતદાર યાદી (Electoral Roll)</b> માં ઉમેરવાનો અંતિમ કાનૂની નિર્ણય ERO લે છે.</p><p class='mt-2'><b>સત્તાવાર પ્રક્રિયા:</b></p><ul class='list-disc pl-5 space-y-1'><li>ERO BLO રિપોર્ટની અંતિમ પૃષ્ઠભૂમિ તપાસ કરે છે.</li><li>જો મંજૂર થાય, તો તમારું નામ ડ્રાફ્ટ મતદાર યાદીમાં પ્રકાશિત થાય છે.</li><li>7-દિવસની વૈધાનિક વાંધા અવધિ પછી, અંતિમ સમાવેશની પ્રક્રિયા થાય છે.</li></ul>"},
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
        city_lower = city.strip().lower()
        valid_gujarat_cities = {
            "ahmedabad", "surat", "vadodara", "rajkot", "bhavnagar",
            "jamnagar", "gandhinagar", "junagadh", "gandhidham", "anand",
            "navsari", "morbi", "nadiad", "surendranagar", "bharuch",
            "mehsana", "bhuj", "porbandar", "palanpur", "valsad",
            "vapi", "gondal", "veraval", "godhra", "patan",
            "dahod", "botad", "amreli", "deesa", "jetpur"
        }
        
        if city_lower not in valid_gujarat_cities:
            raise ValueError("CivicGuide AI currently provides detailed electoral data for Gujarat only. Please enter a city within Gujarat (e.g., Rajkot, Ahmedabad, Surat).")

        city_title = city.title()
        now = datetime.now()
        
        # Generating dummy dates - keeping it realistic intervals
        notification_date = now + timedelta(days=15)
        nomination_deadline = notification_date + timedelta(days=10)
        polling_date = nomination_deadline + timedelta(days=20)
        counting_date = polling_date + timedelta(days=5)
        
        return {
            "location": city_title,
            "notification_date": notification_date.strftime("%d-%m-%Y"),
            "nomination_deadline": nomination_deadline.strftime("%d-%m-%Y"),
            "polling_date": polling_date.strftime("%d-%m-%Y"),
            "counting_date": counting_date.strftime("%d-%m-%Y")
        }

