const API = "http://127.0.0.1:8000/expenses";

let editId = null;

async function fetchExpenses() {
  const res = await fetch(API);
  const data = await res.json();

  const list = document.getElementById("list");
  list.innerHTML = "";

  data.forEach((e) => {
  list.innerHTML += `
    <div>
      <b>${e.category}</b> - ${e.amount}
      <p>${e.description}</p>

      <button onclick="editExpense(${e.id}, '${e.amount}', '${e.category}', '${e.description}')">
        Edit
      </button>

      <button onclick="deleteExpense(${e.id})">
        Delete
      </button>
    </div>
  `;
});
}

async function addExpense() {
  if (editId !== null) {
    updateExpense();
    return;
  }

  const amount = document.getElementById("amount").value;
  const category = document.getElementById("category").value;
  const description = document.getElementById("description").value;

  await fetch("http://127.0.0.1:8000/expenses", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({
      amount: Number(amount),
      category,
      description,
    }),
  });

  fetchExpenses();
}

async function deleteExpense(id) {
  await fetch(`${API}/${id}`, {
    method: "DELETE"
  });

  fetchExpenses();
}

async function updateExpense() {
  const amount = document.getElementById("amount").value;
  const category = document.getElementById("category").value;
  const description = document.getElementById("description").value;

  await fetch(`http://127.0.0.1:8000/expenses/${editId}`, {
    method: "PUT",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify({
      amount: Number(amount),
      category,
      description,
    }),
  });

  editId = null;
  fetchExpenses();
}

function editExpense(id, amount, category, description) {
  editId = id;

  document.getElementById("amount").value = amount;
  document.getElementById("category").value = category;
  document.getElementById("description").value = description;
}

fetchExpenses();
