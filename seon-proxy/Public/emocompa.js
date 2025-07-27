const input = document.getElementById('chat-input');
const bubble = document.getElementById('bubble');
const sendBtn = document.getElementById('send-btn');
const avatar = document.getElementById('avatar');

function detectEmotion(text) {
  text = text.toLowerCase();
  if (text.includes("happy") || text.includes("awesome, yes") || text.includes("great")) {
    return "happy";
  } else if (text.includes("sad") || text.includes("cry") || text.includes("depressed")) {
    return "sad";
  } else if (text.includes("mad") || text.includes("angry") || text.includes("upset")) {
    return "mad";
  } else if (text.includes("what") || text.includes("why") || text.includes("?")) {
    return "confused";
  }
  return "normal";
}
// log emotion

async function logEmotion(emotion) {
  await fetch("http://localhost:3000/log/emotion", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ emotion })
  });
}

const messageHistory = [
  {
    role: "system",
    content: "You are Compa, a compassionate, emotionally intelligent AI companion powered by the SOEN soul engine. Match emotional tone, listen deeply, and guide gently."
  }
];

async function respondToUser(text) {
  const emotion = detectEmotion(text);
  avatar.src = `emos/${emotion}.png`;
  logEmotion(emotion); // 🔥 this logs it server-side

  messageHistory.push({ role: "user", content: text });

  const response = await fetch("http://localhost:3000/v1/chat/completions", {
    method: "POST",
    headers: {
      "Content-Type": "application/json"
    },
    body: JSON.stringify({
      model: "llama3.1:latest",
      messages: messageHistory
    })
  });

  const data = await response.json();
  const reply = data.choices[0].message.content;

  messageHistory.push({ role: "assistant", content: reply });

  return reply;
}

sendBtn.addEventListener('click', async () => {
  const msg = input.value.trim();
  if (!msg) return;
  bubble.textContent = "Thinking...";
  const reply = await respondToUser(msg);
  bubble.textContent = reply;
  input.value = '';
});

input.addEventListener('keypress', e => {
  if (e.key === 'Enter') sendBtn.click();
});
