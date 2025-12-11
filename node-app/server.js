const express = require('express');
const app = express();
const port = process.env.PORT || 8080;

app.get('/', (req, res) => {
  const deployType = process.env.DEPLOY_TYPE || 'Local/Unknown';
  res.send(`
    <html>
      <body style="background-color: #2D5A27; color: white; font-family: sans-serif; display: flex; justify-content: center; align-items: center; height: 100vh;">
        <div style="background: rgba(255,255,255,0.1); padding: 40px; border-radius: 20px;">
          <h1>Hello from Node.js! ⬢</h1>
          <p>Deployed via: ${deployType}</p>
        </div>
      </body>
    </html>
  `);
});

app.listen(port, () => {
  console.log(`App listening on port ${port}`);
});