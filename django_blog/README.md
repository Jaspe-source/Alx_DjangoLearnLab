⚡ Features Overview

The blog supports complete CRUD operations (Create, Read, Update, Delete) for blog posts. Authenticated users can create, edit, and delete their own posts, while all users can view posts.

🛠 Implementation Details
1. CRUD Operations

ListView (PostListView): Displays all blog posts, ordered by most recent first.

DetailView (PostDetailView): Shows full details of a single blog post.

CreateView (PostCreateView): Allows logged-in users to create new posts. The logged-in user is automatically set as the author.

UpdateView (PostUpdateView): Allows the post author to update their own posts.

DeleteView (PostDeleteView): Allows the post author to delete their own posts.

2. Forms

Implemented using Django’s ModelForm.

Includes fields: title, content.

Author field is automatically assigned using form.instance.author = self.request.user.

3. Templates

Templates are stored in blog/templates/blog/:

home.html – lists all posts.

post_detail.html – displays single post.

post_form.html – form for creating and editing posts.

post_confirm_delete.html – confirmation page for deleting a post.

4. URL Patterns

Defined in blog/urls.py:

/ → List all posts (home).

/post/<int:pk>/ → View single post details.

/post/new/ → Create a new post.

/post/<int:pk>/update/ → Edit an existing post.

/post/<int:pk>/delete/ → Delete a post.

5. Permissions & Access Control

Authenticated users only can create posts (LoginRequiredMixin).

Only the author can edit or delete their own posts (UserPassesTestMixin).

All users (authenticated or not) can view posts.

6. Testing Guidelines

Verify that the post list loads correctly with all posts.

Confirm that the detail page shows full content.

Ensure that only authenticated users can access create, update, and delete forms.

Test that unauthorized users are redirected to login.

Verify that authorship is automatically assigned correctly.

Check that non-authors cannot update or delete another user’s posts.