![Add image Here]

# Welcome to Penny Pinchers Expenses App

## A Expenses App To Help You Manage Your Finances
### Penny Pinchers helps people to manage their expenses and see how much they are spending! 

The Penny Pinchers Expenses app is designed to allow users to organise, edit, display and delete their expenses, which will help them long term to manage their finances. By just clicking the "Add expense" button and filling out the details a user can add thier costs to a list, later on down the line if they wish to the user can also delete or edit the list or expense. The user also gets a total of their expenses so they can be aware as to the exact number all their expenses come to. The web app allows only registered users to create thier own expenses tracker list. Users that aren't registered will not be able to use the expense tracker, but can register for an account and browse the about us page.

# **[Link to Live Site](INSERT HEROKU LINK HERE)**

*This project is created as a final portfolio project for Code Institute (CI).*

**Built by Ahmad Jabbeer Jeerooburkhan**

---

# Table of Contents 

1. [ UX/UI ](#UX/UI)
2. [ Agile Methodology ](#agile-methodology)
3. [ Features ](#features)
4. [ Future Features ](#future-features)
5. [ Design ](#design)
6. [ Testing and Validation ](#testing-and-validation)
7. [ Technology Stack Used ](#technology-stack-used)
8.
9.
10.

# UX/UI

## Database Planning

First off I had to create and Entity Relationship Diagram (ERD) This would help me see how each model(s) would relate to each other. I created my ERD's using Lucidchart. Below you will see that I had a simple idea to create the initial phases of the expenses app. 
![Database ERD Lucidchart](/static/images/readme/ERD_for_model_used.png)

From this I can determine the following: 
- A user can have many expenses (one-to-many).
- An expense belongs to one user (many-to-one).

## UX Design

### Overview
Penny Pinchers is a web expense tracker which can be for anyone at any stage or age in life looking to keep on top of their finances! The design outlay has purposefully been left simple and easy to read, to allow a pleasant user experience. 

### User Experience 

As a user of the app I want to be able to do the following: 
 - Log into my account securely using private authentication credentials. 
 - Have access and view my expenses. 
 - Add, delete and edit any of my expenses. 
 - Ensure that my personal data is private and secure. 

### User Demographic

The user demographic for this expense tracker, or expense trackers in general can be anyone from people collecting pocket money to those that are retired. Everyone who will use an expense tracker has a reason to do so whether thats for saving or just to keep on top of their finances. Some examples of this would be:
- Small business owners tracking business expenses.
- Families looking to see how much their spending. 
- A young person trying to get their finances in order from early on. 

The ultimate goal for these users is for them to gain better control over their finances, track their spending (good and bad) and acheive thier financial end goal. 

## Wireframes

I used Balsamic to create my wireframes. The final product does look slightly different to the original outlay which I feel in the design stages early on is quite normal as it was good to use for a guide/template to follow.
As you will see below I have included screen shots of the simple design layout I was going for and the final product isn't too far off this.

This is the Home page outlay I was looking to go with as a simple design:

![Desktop Wireframe View 1](/static/images/readme/desktop_wireframe1.png)

The same outlay was created in the wireframes as you can see from the sign in page below: 

![Sign In Page](/static/images/readme/desktop_signin.png)

Followed by the register page for users that don't have an account: 

![Register Page](/static/images/readme/desktop_register.png)

Now below you will see the outlay I wanted to create with the expense page, I wanted it to be simple and clear for the user, with a lot of the buttons all based around the centre of the page so it stops the user from looking all around the page for all the features as they are all in the centre together:

![Expense Page](/static/images/readme/desktop_expenses.png)

I then went on to design a simple mobile view of how I would like the app to look like and these are the wireframes you see below: 

![Mobile View Page 1](/static/images/readme/mobile1.png) ![Mobile View Page 2](/static/images/readme/mobile2.png)

#### [ Back to Top](#table-of-contents)



# Agile Methodology 

When developing this app an agile approach has been taken throughout this project. I adapted and agile methodology to ensure an efficient and continual progress was being made. I broke each instance down into smaller user stories so they were refined into more manageable tasks therefore each user story has different acceptance criterias. The link to the kanban board for the User Stories can be found [here](https://github.com/users/Jab90/projects/4).

## Kanban Board Overview

The Kanban Board provided a visual overview of the project's progress and facilitated efficient task management. It was organised into the following sections: 

- **Todo:** This section contained all the tasks that needed to be done for the project to be completed and done. 
- **In Progress:** The in progress section indicated active tasks that were being worked on. 
- **Done:** The done section are the tasks that were completed successfully. 

### User Stories

User stories played a vital role in the development process, it helped ensure the features were inline with the users needs, all of the user needs were written out onto the kanban project board, which helped guide tasks being implemented and what to prioritse. 

### Task Management 

In addition to tracking user stories, the kanban board functioned as a detailed task list. I used it to break down user stories into smaller, actionable tasks, ensuring clear and manageable objectives for development. This granular approach allowed for efficient progress tracking. 
By applying agile principles and effectively utilising the kanban board, the development of Penny Pinchers remained focused, adaptable, and responsive to changing requirements, resulting in a more robust and user-centered Django expense application. 

### User Authentication and Authorisation 

To safeguard user data within the expenses tracking app, it is crucial to implement strong authentication and authorisation systems. This epic focuses on securing user access to their accounts while preventing unauthorised entry/access. Through user authentication, individuals can log in to their accounts using unique credentials, such as usernames and passwords. User authorisation further ensures that only authenticated users have the necessary permissions to access specific features and data within the app. This epic highlights the importance of creating a secure entry and exit process for the app.

- [User Story #11 Authorisation](https://github.com/users/Jab90/projects/4?pane=issue&itemId=73017867)

### Expense Management and Validation 

Managing and validating expenses are key functions of the app that ensure the accuracy and reliability of financial information. This epic is dedicated to equipping users with comprehensive tools for expense management, including options to add, edit and delete expenses. The app also requires validation mechanisms to confirm the accuacy of the expense data entered by users this goes for the base currency selected to, so if a user has selected GBP for example they cannot select USD and add another expense, the app will throw up and error telling the user to select the same currency. By enabling precise and reliable expense tracking, this epic aims to empower users to make informed financial decisions and effectively achieve their financial goals. 

- [User Story Track Expenses [#1]](https://github.com/Jab90/expense_tracker_project/issues/1)
- [User Story Edit Expenses [#3]](https://github.com/Jab90/expense_tracker_project/issues/3)
- [User Story Validate Expenses [#5]](https://github.com/Jab90/expense_tracker_project/issues/5)
- [User Story Total Costs [#6]](https://github.com/Jab90/expense_tracker_project/issues/6)
- [User Story Save Feature For Each User [#9]](https://github.com/Jab90/expense_tracker_project/issues/9)
- [User Story Delete Expenses [#4]](https://github.com/Jab90/expense_tracker_project/issues/4)
- [User Story Currency Choice [#7]](https://github.com/Jab90/expense_tracker_project/issues/7)

### User Experience, Interface and Feeback

This epic is dedicated to reinfing the app's user interface to create a clean, intuitive, and easy to navigate experience. It addresses the user's need for a streamlined design that enhances usability. Additionally, this epic focuses on incorporating feeback mechanisms, such as notifications when users add, edit or delete and expense. A confirmation modal will also be introduced when the delete button is clicked, prompting users to confirm before an expense is permanently removed. By prioritising UI imporvements and user feedback, this epic seeks to enhance overall user satisfaction and improve the app's usability. 

- [User Story UI [#8]](https://github.com/Jab90/expense_tracker_project/issues/8)
- [User Story User Feedback [#10]](https://github.com/Jab90/expense_tracker_project/issues/10)

# Features

## Home Page

- Register and login hyperlinks on main splash page with a background image.
- If user is already logged in then can choose to logout or carry on adding expenses.
- Both logged in and non authorised users have access to the about me page. 
- Banner at the top tells the person browsing the site if they are logged in or not. (This feature is accross all pages)

![Home Page](/static/images/readme/home_page.png)

## About Page

- Brief desciption of what Penny Pinchers is all about.
- Includes a small logo next to the text.
- Accessible without the need to login or user authentication. 

![About Page](/static/images/readme/about_page.png)

## Navbar and Footer

- Navigation links at the top of the page allows the user to navigate through the website easily. On mobile theres a hamburger menu that appears and with one tap the nav bar drops down with the navigation links. 
- Social media links on the footer take you to the social media platforms listed. 

![Navbar](/static/images/readme/Navbar.png)     

![Navbar](/static/images/readme/Footer.png)

![Navbar Mobile](/static/images/readme/mobilenav_hamburger.png)     ![Navbar Mobile Dropdown](/static/images/readme/mobilenav_dropdown.png)

## Register Page

- Signs up new users and redirects them to the expenses tool page once logged in. 
- Secure sign up fuctionality allowing users to register securely.

![Sign Up Page](/static/images/readme/signup.png)

## Login Page

- Secure sign in functionality allowing existing users to sign into their account. 
- After a user logs in successfully they get redirected to the expense page. 

![Login Page](/static/images/readme/login.png)

## Sign Out

- Secure sign out procedure getting the user to confirm their sign out. 
- Once signed out they can see the confirmation as they get redirected to the login page. 

![Sign Out Page](/static/images/readme/sign_out.png)

![Sign Out Confirmation](/static/images/readme/sign_out_confirmation.png)

## Expenses Page

- The user can only see and gain access to this page once they have been authenticated.
- User can straight away start using the expenses app as it pops up after login. 

![Expenses Page](/static/images/readme/expenses_login.png)

- From here you can add, delete and edit existing expenses. When you click the "Add Expense" button you're redirected to the following page: 

![Add Expense Page](/static/images/readme/add_expense.png)

- When adding an expense you can only use one currency otherwise the app throws up an error, so no cross currency mixing can be done. The following error will show:

![Expense Currency Error](/static/images/readme/expense_currency_error.png)

- You can edit an existing expense whether its the item name, currency, or amount.

![Edit and Expense](/static/images/readme/edit_expense.png)

- Users can delete an expense, but this will have a confirmation modal pop up to confirm the action the user wants to take. 

![Delete Modal Pop Up](/static/images/readme/delete_modal.png)

- Users can see their total costs at the bottom of all of their expenses. 

![Total Costs](/static/images/readme/total_costs.png)

## User Friendly Interface

- With the overall layout of the web app users can navigate their way around simply, as the layout is clear and concise which was a goal from the start of building this web app. 

![Layout](/static/images/readme/layout.png)

## Additional Security Features

- Users coming to the web app aren't able to manipulate the URL to try gain access to someone elses account.
- Users only have direct access to their own account and expenses. 
- Users are redirected to the sign in page if trying to log in with the wrong credentials with an error message, errors will flag up if mandatory fields are left empty. 

![Additional Security](/static/images/readme/empty_field_error.png)

##### [ Back To Top ](#table-of-contents)

# Future Features

- Potentially getting a currency converter api linked to the backend, so if there's a mixture of currencies the user can add the currencies and the web app will automatically calculate the current price conversion and add it to the total expenses. 
- Have a more analytical view with graphs and charts to help the user with a more visual look as to where their money is going. 
- Add all the currencies in the world to choose from. 
- Reminders for certain bills or payments coming up. 
- Having a budgeting, investment and savings sector so users can split their different budgets how they feel. 

Below is an improved ERD mock up that I think would help with building a more improved version of the app. 

![Improved ERD](/static/images/readme/improved_ERD.png)

The relationships for this mock up would be the following: 

1. A user can have many expenses (one-to-many).
2. An expense belongs to one user (many-to-one).
3. A category can have many expenses (one-to many).
4. An expense belongs to one category (many-to-one).
5. A user can have many budgets (one-to-many).
6. A budget belongs to one user (many-to-one).
7. A category can have many budgets (one-to-many).
8. A budget belongs to one category (many-to-one). 

##### [ Back To Top ](#table-of-contents)

# Design

## Responsive Design

- The website is responsive ensuring users will have usability of the web app across various screen sizes. 
- When the screen is smaller the navbar collapses into a hamburger buttton for improved UI and navigation on smaller screens. 
- Images are responsive to so they are inline with the screen size being shown. 

![Responsive Mobile Design - Home Page](/static/images/readme/mobile_home.png)

## Colour

![Colour WCAG](/static/images/readme/colours1.png)  ![Colour WCAG 2](/static/images/readme/colours2.png)

The Penny Pinchers App adopts a light colour scheme to provide users with a clear and concise look with an easy to understand UI. 

# Testing and Validation: 

### HTML Validation

To check the HTML files in this project the [W3C validator](https://validator.w3.org/) was used via the direct input feature in W3C Validator. The curly braces used for Django code came back as errors but this is expected as its not recognised as base HTML code from the software. 

| **File**  | **Result** |
|---|---|
| base.html | &#10004; |
| logout.html | &#10004; |
| login.html | &#10004; |
| signup.html | &#10004; |
| **HTML Files Made:**|
| index.html | &#10004; |
| about.html | &#10004; |
| add.html | &#10004; |
| edit.html | &#10004; |
| expense_tool.html | &#10004; |

### CSS Validation

The [Jigsaw W3C Validator](https://jigsaw.w3.org/css-validator) was used to check the CSS stylesheet. No errors were found. 

![CSS Validator](/static/images/readme/css_validator.png)

| **File**  | **Result** |
|---|---|
| style.css | &#10004; |

### JavaScript Validation 

To validate the JavaScript code used [JShint](https://jshint.com/) was used. 8 ES6 warnings cmae back and an undentified variable because of Bootstrap, I can ignore the Bootstrap error since Bootstrap is already implemented.

![JS Validator](/static/images/readme/js_validator.png)

| **File**  | **Result** |
|---|---|
| delete_expense.js | &#10004; |

### Python Validation

For checking the python code [CI Python Linter](https://pep8ci.herokuapp.com/) was used.

![Python Validator](/static/images/readme/python_validator.png)

An issue that was commonly coming up in the python validator is the lines of code were too long, so breaking some of the code up and changing it around helped with this, but in some places I felt it was necessary to just leave it as some of the code would stop working, as there would be a break somewhere also most of the time this error was from comments. 

| **Project/App** | **File** | **Result** |
|---|---|---|
| about | modles.py | &#10004; |
| about | admin.py | &#10004; |
| about | urls.py | &#10004; |
|---|---|---|
| expense | admin.py | &#10004; |
| expense | forms.py | &#10004; |
| expense | models.py | &#10004; |
| expense | urls.py | &#10004; |
| expense | views.py | &#10004; |
|---|---|---|
| expense_tracker | settings.py | &#10004; |
| expense_tracker | urls.py | &#10004; |
| expense_tracker | wsgi.py | &#10004; |

## Manual Testing

### Test Navigation When Logged In 

| **Test** | **Expected Outcome** | **Result** | 
|---|---|---|
| Click on logout button | User gets logged out and redirected to the login page. | &#10004;
| Navigate to home page when clicking on logo or home | The home page telling a user to sign in or register is loaded | &#10004;
| Expense tab appears | Expense tab appears when user is logged in and loads their expenses if they have any already saved as soon as they log in | &#10004;

### Test Navigation When Not Logged In 

| **Test** | **Expected Outcome** | **Result** | 
|---|---|---|
| Absence of Expense Navbar link | No expense tab can be seen as user is not logged in, however can see Register, Sign in, About and Home. | &#10004;
| Clickable log in tab | Redirected to the login page.  | &#10004;
| Clickable register tab | Redirected to the register page. | &#10004;
| New user signed up | New account created and redirected to the expense_tool page | &#10004;
| New user sign up details | A new user has to input the correct criteria for username and password otherwise can't sign up. | &#10004;

### Test Login Status 

| **Test** | **Expected Outcome** | **Result** | 
|---|---|---|
| Logged in message | When the user is logged in a message on the top right just below the navbar will show as username is logged in. | &#10004;
| Not logged in message | When the user is not logged in there will be a message just below the navbar saying "You are not logged in" | &#10004;

### Test Adding An Expense 

| **Test** | **Expected Outcome** | **Result** | 
|---|---|---|
| On clicking "Add Expense" button | Redirected to add expense page with a form displayed to enter expense details. | &#10004;
| Filling out the expense form | The expense is added to the database successfully. | &#10004;
| Verifying the new expense is added | The new expense is visibile in the expense list. | &#10004;
| Filling out the expense form with invalid syntax/data | An error message is displayed indicating an invalid input. | &#10004;
| Filling out expense with a different currency | An error message is displayed indicating the base currency chosen.| &#10004;
| Submitting the form with incomplete or no data | An error message is displayed, indicating all fields are required | &#10004;
| Add expense notification | After a user adds their expense, a confirmation message appears at the top of the page. | &#10004;

### Test Edit An Expense 

| **Test** | **Expected Outcome** | **Result** | 
|---|---|---|
| On clicking the "Edit" button | Redirected to edit expense page with the form displaying the existing populated expense details. | &#10004;
| Modifying expense details | Changes are successfull saved to the database, currency value has to stay the same. | &#10004;
| Verifying the changes | Changes are reflected in the expense list. | &#10004;
| Submitting the form unchanged | The expense remains the same value as before. | &#10004;
| Edit expense notification | After a user edits their expense, a confirmation message appears at the top of the page. | &#10004;

### Test Delete An Expense

| **Test** | **Expected Outcome** | **Result** | 
|---|---|---|
| On clicking the "Delete" button | The delete Modal is pops up and is displayed. | &#10004;
| Confirm deleting an expense | The expense is successfully deleted from the list and database. | &#10004;
| Confirmation of the deletion | The deleted expense is no longer in the list. | &#10004;
| Cancel delete on modal pop up | Expense remains, and is unchanged in the list and database. | &#10004;
| On clicking the "Delete" button | The delete Modal is pops up and is displayed. | &#10004;
| Delete expense notification | After a user deletes their expense, a confirmation message appears at the top of the page. | &#10004;

### Testing The Admin Panel

The admin panel is there for admins and owners of the web app to have access to the backend, access will be granted to those that have a superuser account. 

| **Test** | **Expected Outcome** | **Result** | 
|---|---|---|
| Log in as Superuser/Admin | Displays the Django admin database panel | &#10004;
| Add an expense | Create a new expense in the database | &#10004;
| Edit an expense | Edit the details of an expense and save the changes. | &#10004;
| Delete an expense | Delete the details of an expense. | &#10004;

### Lighthouse Testing

Below is a result of the Penny Pinchers Home page desktop and mobile lighthouse test: 

#### Desktop

![Lighthouse Home Page test (Desktop)](/static/images/readme/lighthouse_desktop_home.png)

#### Mobile

![Lighthouse Home Page test (Mobile)](/static/images/readme/lighthouse_mobile_home.png)

Below is a result of the About page desktop and mobile lighthouse test: 

#### Desktop

![Lighthouse About Page test (Desktop)](/static/images/readme/lighthouse_desktop_about.png)

#### Mobile 

![Lighthouse About Page test (Mobile)](/static/images/readme/lighthouse_mobile_about.png)

Below is a result of the Register page desktop and mobile lighthouse test: 

#### Desktop

![Lighthouse Register Page test (Desktop)](/static/images/readme/lighthouse_desktop_register.png)

#### Mobile 

![Lighthouse Register Page test (Mobile)](/static/images/readme/lighthouse_mobile_register.png)


##### [ Back To Top ](#table-of-contents)








# Technology Stack Used:

- HTML - Used for page structure.
- CSS - Custom styling.
- Bootstrap - Frontend Framework used for custom styling and responsive development.
- Javascript - For the delete pop up modal.
- Python - For backend. 
- Django - Frame work to build this web app. 
- Heroku PostgreSQL - Used as the database.
- Heroku - For hosting the deployment of this project. 
- Balsamiq - For wireframes.
- Font Awesome - For social media icons.
- Lucidchart - For Entity Relationship Diagrams (ERD).
- Freepik - For free stock images
- Google Images - Penny Pincher image (on about page).
- Google fonts - For custom font styling. 
- GitHub - Used for storing code, and Kanban board. 
- GitPod - Used for coding the whole projet. 
- Cloudinary - Used for hosting the static files for images. 
- Git - for version control. 
- PEP8 - This was used to validate all the python code. 
- W3C: HTML - Validator for all the HTML code.
- W3C: CSS - Validator for all the CSS code. 
- Google Chrome Dev Tools - Helpful for debugging, fixing errors and checking app responsiveness. 

## Django Packages: 

- Allauth: Used for authentication, registration and account management. 
- Crispy Forms: To style the forms. 
- Dj_database_url:  To parse the database URL from the environment variables in Heroku.
- Gunicorn: Used as the server for Heroku. 
- Psycopg2: An adaptor for use in python. 






