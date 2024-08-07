/**
 * Javascript code for deleting expenses.
 * 
 * Creates a modal to confirm an expense being deleted by the user.
 * Updates the form dynamically based on the unique expense ID. 
 * This creates a better UI/UX design to the Penny Pinchers expense web application.
 */

const deleteModal = new bootstrap.Modal(document.getElementById("deleteModal"));
const deleteButtons = document.getElementsByClassName("delete-expense");
const deleteForm = document.getElementById("deleteForm"); 


for (let button of deleteButtons) { 
    button.addEventListener("click", (e) => {
        let expenseId = e.target.getAttribute("data-expense-id");
        // check to see expense ID
        console.log("expense ID:", expenseId); 
        if(expenseId) { 
            deleteForm.action = `/delete/${expenseId}/`;
            deleteModal.show();
        } else {
            console.error("Expense ID not found");
        }
        
    });
}