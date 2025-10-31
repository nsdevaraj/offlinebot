# AIML Chatbot - React Edition

A modern, React-based chatbot application powered by AIML (Artificial Intelligence Markup Language) with a beautiful, responsive UI.

## 🚀 Tech Stack

### Backend
- **FastAPI** - Modern Python web framework
- **AIML** - Artificial Intelligence Markup Language for conversational patterns
- **Autocorrect** - Spell correction for user input
- **Uvicorn** - ASGI server

### Frontend
- **React** - Modern UI library
- **Tailwind CSS** - Utility-first CSS framework
- **Axios** - HTTP client for API calls
- **Modern animations & transitions**

## 📁 Project Structure

```
/app/
├── backend/                 # FastAPI backend
│   ├── server.py           # Main API server
│   ├── requirements.txt    # Python dependencies
│   └── .env               # Environment variables
├── frontend/               # React frontend
│   ├── src/
│   │   ├── App.js         # Main React component
│   │   ├── App.css        # Component styles
│   │   ├── index.js       # Entry point
│   │   └── index.css      # Global styles with Tailwind
│   ├── public/
│   │   └── index.html     # HTML template
│   ├── package.json       # Node dependencies
│   ├── tailwind.config.js # Tailwind configuration
│   └── .env              # Frontend environment variables
├── data/                  # AIML conversation patterns (100+ files)
├── pretrained_model/      # AIML brain file for fast loading
└── README.md             # This file
```

## 🎨 Features

### UI/UX
- ✨ Modern, minimalist design with gradients
- 💬 Real-time chat interface with message bubbles
- ⏱️ Message timestamps
- 🔄 Typing indicator animation
- 📱 Fully responsive design
- 🧹 Clear chat functionality
- 🎭 Smooth animations and transitions
- 📜 Auto-scroll to latest messages

### Backend
- 🤖 AI-powered responses using AIML
- ✍️ Automatic spell correction
- 🧠 Brain file caching for faster startup
- 🔌 RESTful API with FastAPI
- 🌐 CORS enabled for cross-origin requests
- ✅ Health check endpoint

## 🔧 API Endpoints

### GET `/api/health`
Health check endpoint
```bash
curl http://localhost:8001/api/health
```

### POST `/api/chat`
Send a message to the chatbot
```bash
curl -X POST http://localhost:8001/api/chat \
  -H "Content-Type: application/json" \
  -d '{"message": "Hello"}'
```

**Response:**
```json
{
  "response": "Hello! How can I help you today?",
  "status": "success"
}
```

```bash
# install dependencies
cd backend
python3 -m venv path/to/venv
source path/to/venv/bin/activate
pip install -r  requirements.txt
python server.py

cd frontend
yarn install
yarn start
```

## 🚀 Running the Application

### Using Supervisor (Recommended)
Both services are managed by supervisor and run automatically:

```bash
# Check status
sudo supervisorctl status

# Restart services
sudo supervisorctl restart backend
sudo supervisorctl restart frontend
sudo supervisorctl restart all
```

### Manual Startup

**Backend:**
```bash
cd backend
python server.py
# Runs on http://0.0.0.0:8001
```

**Frontend:**
```bash
cd frontend
yarn start
# Runs on http://localhost:3000
```

## 🛠️ Development

### Installing Dependencies

**Backend:**
```bash
cd /app/backend
pip install -r requirements.txt
```

**Frontend:**
```bash
cd /app/frontend
yarn install
```

### Environment Variables

**Backend (.env)**
```
MONGO_URL=mongodb://localhost:27017/chatbot
```

**Frontend (.env)**
```
REACT_APP_BACKEND_URL=http://localhost:8001
PORT=3000
```

## 📝 AIML Data

The chatbot uses 100+ AIML files covering various topics:
- General conversation
- Knowledge & facts
- Science & technology
- Entertainment (movies, music)
- Sports
- Geography & history
- And much more!

AIML files are located in `/app/data/` and loaded through `/app/pretrained_model/learningFileList.aiml`.

## 🎯 Key Improvements Over Original

1. **Modern UI**: Beautiful React interface vs basic HTML/jQuery
2. **Better UX**: Animations, typing indicators, timestamps
3. **FastAPI**: Modern async Python framework vs Flask
4. **Responsive**: Works great on all screen sizes
5. **Maintainable**: Component-based React architecture
6. **Type Safety**: Pydantic models for API validation
7. **Production Ready**: Supervisor for process management

## 🐛 Troubleshooting

### Backend not starting
Check logs:
```bash
tail -f /var/log/supervisor/backend.err.log
```

### Frontend compilation errors
```bash
cd /app/frontend
yarn install
sudo supervisorctl restart frontend
```

### AIML brain file issues
Delete and regenerate:
```bash
rm /app/pretrained_model/aiml_pretrained_model.dump
sudo supervisorctl restart backend
```

## 📚 Resources

- [FastAPI Documentation](https://fastapi.tiangolo.com/)
- [React Documentation](https://react.dev/)
- [Tailwind CSS](https://tailwindcss.com/)
- [AIML Tutorial](http://www.alicebot.org/documentation/)

## 📄 License

This project is open source and available for educational purposes.

---

**Built with ❤️ using React + FastAPI + AIML**
