const express = require('express');
const fetch = require('node-fetch');
const path = require('path');
const app = express();
const PORT = 3000;

// Serve frontend files
app.use(express.static(path.join(__dirname, 'public')));

// Allow CORS + CSP for dev
app.use((req, res, next) => {
  res.setHeader("Content-Security-Policy", "default-src 'self'; connect-src *");
  next();
});

app.use(express.json());

// Proxy POST to Ollama server (running on Windows via Tailscale)
app.post('/v1/chat/completions', async (req, res) => {
  try {
    const ollamaResponse = await fetch('http://localhost:3000/v1/chat/completions', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify(req.body)
    });
    const data = await ollamaResponse.json();
    res.json(data);
  } catch (err) {
    console.error('Proxy error to Ollama:', err);
    res.status(500).json({ error: 'Failed to reach Ollama backend.' });
  }
});

// Emotion logging
app.post('/log/emotion', async (req, res) => {
  try {
    const ollamaLog = await fetch('http://localhost:3000/log/emotion', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify(req.body)
    });
    const result = await ollamaLog.json();
    res.json(result);
  } catch (err) {
    console.error('Emotion log proxy error:', err);
    res.status(500).json({ error: 'Emotion log failed.' });
  }
});

app.listen(PORT, () => {
  console.log(`Compa proxy server running at http://localhost:${PORT}`);
});
