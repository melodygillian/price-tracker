const API_URL = "https://YOUR_RENDER_BACKEND_URL.onrender.com";

async function fetchProducts() {
  const res = await fetch(`${API_URL}/products`);
  const data = await res.json();
  const table = document.getElementById("product-table");
  table.innerHTML = "";
  data.forEach(p => {
    const row = document.createElement("tr");
    if (p.is_discounted) row.classList.add("highlight");
    row.innerHTML = `
      <td>
        <img src="${p.image}" alt="${p.name}" width="50" height="50" style="border-radius:7px;background:#000;">
      </td>
      <td>${p.name}</td>
      <td>${p.brand}</td>
      <td>$${p.official_price}</td>
      <td>$${p.lowest_price}</td>
      <td>${p.target_price ? "$" + p.target_price : "-"}</td>
      <td>${p.is_discounted ? "Below target" : "OK"}</td>
      <td><button onclick="removeProduct('${p.id}')">Delete</button></td>
    `;
    table.appendChild(row);
  });
}

document.getElementById("product-form").addEventListener("submit", async e => {
  e.preventDefault();
  const desc = document.getElementById("product-desc").value;
  const brand = document.getElementById("product-brand").value;
  const target_price = document.getElementById("target-price").value;
  await fetch(`${API_URL}/add`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ desc, brand, target_price }),
  });
  fetchProducts();
});

async function removeProduct(id) {
  await fetch(`${API_URL}/delete/${id}`, { method: "DELETE" });
  fetchProducts();
}

fetchProducts();
