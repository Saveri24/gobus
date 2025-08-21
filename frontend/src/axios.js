import axios from 'axios';

// Set the backend base URL
const api = axios.create({
  baseURL: 'http://127.0.0.1:5000', // your Flask backend
  headers: {
    'Content-Type': 'application/json',
  },
});

export default api;
