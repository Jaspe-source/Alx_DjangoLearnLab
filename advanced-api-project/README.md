## API Views Documentation

This project demonstrates the use of **Django REST Framework’s generic views** for CRUD operations on the Book model.

### Views Implemented

1. **BookListView (`/api/books/`)**
   - Retrieves all books.
   - Public access (no authentication required).

2. **BookDetailView (`/api/books/<id>/`)**
   - Retrieves details of a single book by its ID.
   - Public access.

3. **BookCreateView (`/api/books/create/`)**
   - Allows adding a new book.
   - Restricted to authenticated users.

4. **BookUpdateView (`/api/books/update/<id>/`)**
   - Updates an existing book.
   - Restricted to authenticated users.

5. **BookDeleteView (`/api/books/delete/<id>/`)**
   - Deletes a book.
   - Restricted to authenticated users.

### Permissions
- **Read operations (List & Detail):** Open to everyone.
- **Write operations (Create, Update, Delete):** Restricted to authenticated users only.

### Testing
- Use Postman or curl to test each endpoint.
- Unauthenticated users will receive `401 Unauthorized` for create, update, and delete requests.
