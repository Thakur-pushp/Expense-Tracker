document.addEventListener("DOMContentLoaded", fetchTransactions);

const form = document.getElementById("expense-form");
const transactionList = document.getElementById("transaction-list");

// Fetch and display transactions from SQLite/Flask backend
function fetchTransactions() {
    fetch('/api/transactions')
        .then(res => res.json())
        .then(data => {
            transactionList.innerHTML = "";
            data.forEach(trx => {
                const li = document.createElement("li");
                li.className = trx.type;
                li.innerHTML = `
                    <span><strong>${trx.title}</strong> (${trx.category}) - ₹${trx.amount} [${trx.date}]</span>
                    <button class="delete-btn" onclick="deleteTransaction(${trx.id})">Delete</button>
                `;
                transactionList.appendChild(li);
            });
        });
}

// Add transaction event
form.addEventListener("submit", function(e) {
    e.preventDefault();

    const newTrx = {
        title: document.getElementById("title").value,
        amount: parseFloat(document.getElementById("amount").value),
        type: document.getElementById("type").value,
        category: document.getElementById("category").value,
        date: new Date().toISOString().split('T')[0]
    };

    fetch('/api/transactions', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(newTrx)
    })
    .then(res => res.json())
    .then(data => {
        if(data.error) {
            alert(data.error);
        } else {
            form.reset();
            fetchTransactions();
        }
    });
});

// Delete transaction function
function deleteTransaction(id) {
    fetch(`/api/transactions/${id}`, {
        method: 'DELETE'
    })
    .then(res => res.json())
    .then(() => {
        fetchTransactions();
    });
}

// Categories ki list jo type ke hisaab se change hogi
const categories = {
    expense: ["Food", "Rent", "Utilities", "Entertainment", "Shopping", "Transport", "Other"],
    income: ["Salary", "Freelance", "Investments", "Gift", "Other"]
};

// Type change hone par category dropdown update karne ka function
function updateCategories() {
    const typeSelect = document.getElementById("type");
    const categorySelect = document.getElementById("category");
    const selectedType = typeSelect.value;

    // Purane options clear karein
    categorySelect.innerHTML = "";

    // Naye options add karein
    if (categories[selectedType]){
        categories[selectedType].forEach(cat => {
            const option = document.createElement("option");
            option.value = cat.toLowerCase();
            option.textContent = cat;
            categorySelect.appendChild(option);
        });
    }
}

// Page load hote hi default categories set karne ke liye
document.addEventListener("DOMContentLoaded", () => {
    updateCategories();
    fetchTransactions();
});