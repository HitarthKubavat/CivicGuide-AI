# CivicGuide-AI

**Vertical:** Civic Tech & Governance

CivicGuide-AI is a high-performance, Interactive Election Assistant designed to bridge the gap between citizens and the electoral process. By offering a dynamic and localized platform, the app empowers voters with personalized ECI (Election Commission of India) guidelines, local election timelines, and accessible multi-language support.

---

## 🧠 Approach and Logic

The architecture is designed for performance, modularity, and rapid prototyping capabilities:

- **Agentic Workflow**: Developed using an advanced agentic workflow within **Antigravity**. The AI assistant autonomously reasoned through the requirements, updated backend Python modules, integrated new logical decision making flows (e.g., distinguishing between First-Time and Existing voters), and leveraged the **Browser Agent** for automated end-to-end UI testing without manual intervention.
- **FastAPI Core**: The core logic is powered by FastAPI, ensuring lightning-fast execution, type safety, and a highly modular router-based structure for managing timelines and voter journey datasets.

## ⚙️ How it Works

1. **The Stepper UI**: The application features a dynamic Stepper UI that visually breaks down complex ECI registration processes into bite-sized, sequential steps. 
2. **Logical Decision Making**: The Stepper adapts intelligently. Users can toggle "Are you a First-time Voter?", which triggers a state change in the backend logic, instantly swapping the default Form 6 journey for an existing voter journey (Form 8, Form 6B, etc.).
3. **Localized Search**: Users can input their specific city (e.g., Ahmedabad) into the central search bar. The backend processes the string and returns simulated local election timeline dates, which are seamlessly injected into the UI via an asynchronous fetch call.

## 🌐 Google Services Integration

The platform is designed to hook into powerful external services:
- **Google Maps API**: A dedicated placeholder for Google Maps is included on the UI to eventually fetch and display exact Polling Booth locations based on the searched city.
- **Google Translate API**: A foundational implementation structure is present to scale up the hardcoded translations (English & Gujarati) by integrating the Google Translate API for dynamic, on-the-fly accessibility across dozens of Indian regional languages.

## 🔒 Security & Accessibility

- **Input Sanitization**: To mitigate Cross-Site Scripting (XSS) attacks, a custom `escapeHTML` logic is implemented on the frontend, ensuring all JSON inputs from the backend are strictly sanitized before injecting into the DOM.
- **Localization**: Built from the ground up for Gujarat, the application features a seamless toggle between English and Gujarati, making the critical voter information highly accessible and user-friendly for local citizens.

## 📋 Assumptions

- Data generated for the timelines is simulated and acts as a placeholder for a real-time ECI datastore.
- The workflow data represents the current ECI registration cycle.
- The end-user possesses basic digital literacy and access to a modern web browser.

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