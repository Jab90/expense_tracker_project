const deleteModal = new bootstrap.Modal(document.getElementById("deleteModal"));
const deleteButtons = document.getElementsByClassName("delete-expense");
const deleteForm = document.getElementById("deleteForm"); 


for (let button of deleteButtons) { 
    button.addEventListener("click", (e) => {
        let expenseId = e.target.getAttribute("data-expense-id");
        console.log("expense ID:", expenseId);
        if(expenseId) { 
            deleteForm.action = `/delete/${expenseId}/`;
            deleteModal.show();
        } else {
            console.error("Expense ID not found");
        }
        
    });
}