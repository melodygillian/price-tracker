{\rtf1\ansi\ansicpg1252\cocoartf2822
\cocoatextscaling0\cocoaplatform0{\fonttbl\f0\fswiss\fcharset0 Helvetica;}
{\colortbl;\red255\green255\blue255;}
{\*\expandedcolortbl;;}
\margl1440\margr1440\vieww11520\viewh8400\viewkind0
\pard\tx720\tx1440\tx2160\tx2880\tx3600\tx4320\tx5040\tx5760\tx6480\tx7200\tx7920\tx8640\pardirnatural\partightenfactor0

\f0\fs24 \cf0 # Minimal Price Tracker\
\
A black\uc0\u8209 and\u8209 white minimalist web app to track product prices. Frontend is static (GitHub Pages) and backend handles scraping and price alerts (Render).\
\
## Setup\
\
1. **Clone repo and edit** `frontend/script.js`:\
   Replace `YOUR_RENDER_BACKEND_URL` with the actual Render backend URL after deployment.\
\
2. **Deploy backend first:**\
   - Make a free account at [Render.com](https://render.com)\
   - New \uc0\u8594  Web Service\
   - Connect your GitHub repo\
   - Use `/backend` as your root directory\
   - Build command: `pip install -r requirements.txt`\
   - Start command: `gunicorn app:app`\
   - Click \'93Create Web Service\'94\
\
3. **Deploy frontend to GitHub Pages:**\
   - Go to repository \uc0\u8594  Settings \u8594  Pages\
   - Choose branch: `main`, folder: `/frontend`\
   - Wait until `https://yourname.github.io/price-tracker/` is live\
\
4. **Test it:**\
   Add a product (any URL). It will display mock prices until you connect a real scraping API.\
}