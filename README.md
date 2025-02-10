# HRGenie - AI-Powered HR Assistant

HRGenie is an intelligent HR assistant that helps with employee onboarding and scheduling using advanced language models. Built with Django and integrated with state-of-the-art AI models.

## Features

- 🤖 AI-powered chat interface using DialoGPT and OpenAI
- 🔐 Secure user authentication system
- 📊 Interactive dashboard interface
- 💼 Context-aware responses for HR-related queries
- 🎯 Specialized in onboarding and scheduling assistance

## Tech Stack

- Django 
- Python
- Hugging Face Transformers (DialoGPT)
- OpenAI API
- Bootstrap 4
- JavaScript/jQuery

## Installation

1. Clone the repository
```bash
git clone <repository-url>
cd hrgenie
```

2. Create and activate virtual environment
```bash
python -m venv env
source env/bin/activate  # On Windows use: env\Scripts\activate
```

3. Install dependencies
```bash
pip install -r requirements.txt
```

4. Set up environment variables
```bash
# Create .env file and add:
OPENAI_API_KEY=your_openai_api_key
```

5. Run migrations
```bash
python manage.py makemigrations
python manage.py migrate
```

6. Start the development server
```bash
python manage.py runserver
```

## Usage

1. Register a new user account or login with existing credentials
2. Navigate to the chat interface at `/chat/`
3. Start interacting with HRGenie by typing your HR-related queries
4. The AI will provide context-aware responses based on your company's HR needs

## Project Structure

```
hrgenie/
├── apps/
│   ├── authentication/    # User authentication
│   ├── home/             # Main application views
│   └── static/           # Static files (CSS, JS)
├── core/                 # Project settings
└── templates/           # HTML templates
```

## Features in Detail

### AI Chat Interface
- Powered by Microsoft's DialoGPT-large model
- Enhanced with OpenAI integration
- Contextual understanding of HR processes
- Real-time response generation

### Authentication System
- Secure user registration and login
- Session-based authentication
- Password protection and validation

### Dashboard
- Modern, responsive design
- Interactive charts and metrics
- User-friendly interface

## Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## Security Note

⚠️ Remember to keep your API keys secure and never commit them to version control.

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments

- Built with [Black Dashboard Django](https://www.creative-tim.com/product/black-dashboard-django)
- Uses Microsoft's DialoGPT model
- Powered by OpenAI's API

## Support

For support, email [support@hrgenie.com](mailto:support@hrgenie.com) or open an issue in the repository.
