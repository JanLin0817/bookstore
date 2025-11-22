Task: Bookstore Application
1. Create new Django project called bookstore
2. Create books app and add to installed_apps in settings.py
3. Redirect all routes to books app
4. Create templates and use to render bookstore homepage
5. Bookstore homepage will contain book and links to view individual books
6. Create layout template, inherit navbar, and add to bookstore homepage
7. Create route that gets book by id and renders book details
8. Create book model with attributes title, author, year, rating, and description
9. Use book model manager to return books on homepage and book detail page
10. Query and view book by id in book detail page
11. Register book in model admin
12. Create url, template, and view to add book to database and render errors
13. Create url, template, and view to edit book by id and render errors
14. Create url, template, and view to delete book by id
15. Create url, template, and view for registration with error validation
16. Create url, template, and view for login with error validation
17. Create url, button and view for logout
18. Restrict access to add book to logged in users using decorator
19. Restrict access to edit/delete book to users who posted book
20. Update navbar with conditional register, login, logout, add_book, and apis
21. Install Django Rest Framework and create api folder with __init__.py
22. Create serializer for book
23. Create urls and views to getRoutes, getBooks, and getBook by id