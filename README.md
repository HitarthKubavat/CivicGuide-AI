# Matdaar-Mitra (CivicGuide AI)

A high-performance, Interactive Election Assistant designed to bridge the gap between citizens and the electoral process.

## 🏛️ Chosen Vertical
**Civic Tech & Governance**: Focused on empowering citizens through digital literacy and simplified access to electoral processes.

## 💡 Approach and Logic
- **Hyper-Localization**: The assistant is specifically geofenced and optimized for Gujarat, providing a specialized experience for local voters.
- **Progressive Disclosure**: Uses an interactive accordion system to deliver complex ECI registration and voting-day information without overwhelming the user.
- **Inclusion First**: Built-in support for Gujarati, Hindi, and English to ensure no citizen is left behind due to language barriers.
- **Voter Journey Mapping**: Detailed walkthroughs from Form 6 submission to the final VVPAT slip verification inside the polling booth.

## 🚀 How the Solution Works
- **Dynamic Regional Search**: Users enter a Gujarat city (e.g., Rajkot, Ahmedabad) to instantly fetch relevant election timelines and localized polling booth maps.
- **Interactive Education**: Features a 'How to Vote' module that demystifies the EVM-VVPAT process and a 'Voter IQ Quiz' to correct common misconceptions.
- **Document Checklists**: Provides specific, actionable lists of the 12 acceptable ID proofs and required registration documents.

## 🌐 Google Services Integration
- **Google Antigravity**: The core development and orchestration environment.
- **Gemini 1.5 Flash**: Powers the intelligent dialogue, multilingual dictionary, and logical decision-making.
- **Google Maps Embed API**: Provides dynamic, real-time geographic context for constituencies without requiring API key management.
- **Google Search (Agentic)**: Utilized during the build phase to verify official ECI guidelines and ensure data accuracy.

## 📌 Assumptions
- Data is simulated based on the 2026 Gujarat electoral cycle.
- Users have access to a standard mobile or desktop web browser.
- The assistant serves as an educational bridge to official government portals.

## 🛡️ Security & Privacy
- **Stateless Architecture**: No personal voter data (PII) is stored, ensuring 100% privacy and security.
- **Regional Validation**: Custom logic prevents out-of-scope searches to maintain high data integrity for the target region.

---

## 🛠 Setup & Execution

### Prerequisites
- Python 3.9+

### Installation
1. Clone the repository and navigate to the project directory:
   ```bash
   cd CivicGuide-AI
   ```
2. Install the dependencies:
   ```bash
   pip install -r requirements.txt
   ```

### Running the Application
Start the FastAPI server via Uvicorn:
```bash
python -m uvicorn main:app --port 8000
```
Navigate your browser to `http://localhost:8000`.