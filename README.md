# MediDoc
your health, your schedule, one click away

# MediDoc

MediDoc is a medical appointment scheduling and management system designed to facilitate seamless interactions between patients and healthcare professionals. It enables users to book, manage, and track their medical appointments with ease.

## Features
- **User Authentication**: Secure login and signup system.
- **Google Calendar Integration**: Sync appointments with Google Calendar.
- **Appointment Scheduling**: Users can book and manage appointments with doctors.
- **Profile Management**: Users can update their profile and personal details.
- **Real-Time Notifications**: Get alerts for upcoming appointments.
- **Role-Based Access**: Different functionalities for patients and doctors.

## Tech Stack
- **Backend**: Django (Python)
- **Frontend**: HTML, CSS, Bootstrap
- **Database**: PostgreSQL
- **APIs**: Google Calendar API, Google OAuth
- **Version Control**: Git & GitHub

## Installation & Setup
1. **Clone the repository**
   ```bash
   git clone https://github.com/Cavista-Hackathon-2025/MediDoc.git
   cd MediDoc
   ```
2. **Create a virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use: venv\Scripts\activate
   ```
3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```
4. **Setup environment variables**
   - Create a `.env` file and add the necessary credentials (Google OAuth keys, database credentials, etc.)
   
5. **Run migrations**
   ```bash
   python manage.py migrate
   ```
6. **Start the development server**
   ```bash
   python manage.py runserver
   ```

## Google OAuth & Calendar Integration
To enable Google authentication and calendar integration:
1. **Obtain OAuth credentials** from [Google Developer Console](https://console.cloud.google.com/)
2. **Enable Google Calendar API**
3. **Update `settings.py` with OAuth credentials**
4. **Ensure the correct scopes are set**:
   ```python
   SCOPES = [
       "https://www.googleapis.com/auth/calendar.events",
       "https://www.googleapis.com/auth/userinfo.email",
       "https://www.googleapis.com/auth/userinfo.profile",
       "openid",
       "https://www.googleapis.com/auth/calendar"
   ]
   ```

## Troubleshooting
### Merge Conflicts
If you get a merge conflict when pulling changes:
```bash
git status
git merge origin/main
# Resolve conflicts manually
git add .
git commit -m "Resolved merge conflicts"
git push origin main
```

### Common Errors & Fixes
- **SIP must be disabled for installation**: Boot into Recovery Mode and run:
  ```bash
  csrutil disable
  ```
- **OAuth Callback Issues**: Ensure the redirect URI matches your settings in Google Developer Console.
- **Database Errors**: Run migrations and check `.env` configurations.

## Contributors
- **Köded** - Full Stack Developer
- **Ibukunoluwa - Front End Developer**
- **Vivian - Front End Developer**
- **Anuoluwapo - Front End Developer**



## License
This project is licensed under the MIT License.
