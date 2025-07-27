// seon-proxy/server.js

const express = require('express');
const cors = require('cors');
const fetch = (...args) => import('node-fetch').then(({default: fetch}) => fetch(...args));
const app = express();

app.use(cors());
app.use(express.json());

const path = require('path');
app.use(express.static(path.join(__dirname, 'public')));


// Proxy chat completions manually using fetch
app.post('/v1/chat/completions', async (req, res) => {
  try {
    const ollamaRes = await fetch('http://100.127.238.120:11434/v1/chat/completions', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify(req.body)
    });

    const data = await ollamaRes.json();
    res.status(200).json(data);
  } catch (err) {
    console.error('[SEON PROXY] Failed to contact Ollama:', err.message);
    res.status(500).send('Ollama unreachable');
  }
});


// Log emotion
app.post('/log/emotion', (req, res) => {
  const emotion = req.body.emotion;
  console.log(`[COMPA] Emotion logged: ${emotion}`);
  res.sendStatus(200);
});

const PORT = 3000;
app.listen(PORT, () => {
  console.log(`[SEON PROXY] Listening on http://localhost:${PORT}`);
});
