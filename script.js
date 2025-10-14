{\rtf1\ansi\ansicpg1252\cocoartf2822
\cocoatextscaling0\cocoaplatform0{\fonttbl\f0\fswiss\fcharset0 Helvetica;}
{\colortbl;\red255\green255\blue255;}
{\*\expandedcolortbl;;}
\margl1440\margr1440\vieww11520\viewh8400\viewkind0
\pard\tx720\tx1440\tx2160\tx2880\tx3600\tx4320\tx5040\tx5760\tx6480\tx7200\tx7920\tx8640\pardirnatural\partightenfactor0

\f0\fs24 \cf0 const API_URL = "https://price-tracker-dolh.onrender.com";\
\
async function fetchProducts() \{\
  const res = await fetch(`$\{API_URL\}/products`);\
  const data = await res.json();\
  const table = document.getElementById("product-table");\
  table.innerHTML = "";\
  data.forEach(p => \{\
    const row = document.createElement("tr");\
    if (p.is_discounted) row.classList.add("highlight");\
    row.innerHTML = `\
      <td><a href="$\{p.url\}" target="_blank">$\{p.name\}</a></td>\
      <td>$$\{p.official_price\}</td>\
      <td>$$\{p.lowest_price\}</td>\
      <td>$\{p.target_price ? "$" + p.target_price : "-"\}</td>\
      <td>$\{p.is_discounted ? "Below target" : "OK"\}</td>\
      <td><button onclick="removeProduct('$\{p.id\}')">Delete</button></td>\
    `;\
    table.appendChild(row);\
  \});\
\}\
\
document.getElementById("product-form").addEventListener("submit", async e => \{\
  e.preventDefault();\
  const name = document.getElementById("product-name").value;\
  const url = document.getElementById("product-url").value;\
  const target_price = document.getElementById("target-price").value;\
  await fetch(`$\{API_URL\}/add`, \{\
    method: "POST",\
    headers: \{ "Content-Type": "application/json" \},\
    body: JSON.stringify(\{ name, url, target_price \}),\
  \});\
  fetchProducts();\
\});\
\
async function removeProduct(id) \{\
  await fetch(`$\{API_URL\}/delete/$\{id\}`, \{ method: "DELETE" \});\
  fetchProducts();\
\}\
\
fetchProducts();\
}
