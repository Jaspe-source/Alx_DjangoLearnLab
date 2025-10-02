Overview

This feature enhances the Django Blog application by introducing:

Tagging System → Allows authors to categorize posts using tags.

Search Functionality → Allows users to search posts by keywords or tags.

These features improve navigation and discoverability of content across the blog.

🔖 Tagging System
1. Tag Model

Defined a Tag model with a unique name field.

Established a many-to-many relationship between Post and Tag using:

tags = models.ManyToManyField(Tag, blank=True, related_name="posts")

2. Forms

Updated PostForm to allow adding/removing tags:

tags = forms.ModelMultipleChoiceField(
    queryset=Tag.objects.all(),
    required=False,
    widget=forms.CheckboxSelectMultiple
)

3. Views

Post create and update views handle saving tags when a post is created or edited.

Post detail view displays associated tags.

4. Templates

post_form.html → Displays checkboxes for selecting tags while creating/editing a post.

post_detail.html → Shows the tags assigned to a post.

Each tag links to a filtered view showing all posts under that tag.

5. URLs

Added routes for filtering posts by tag:

path("tags/<str:tag_name>/", views.PostByTagListView.as_view(), name="posts-by-tag"),

🔍 Search Functionality
1. Implementation

A search bar was added to the navigation or post list template.

Implemented using Django’s Q objects to allow flexible lookups:

Post.objects.filter(
    Q(title__icontains=query) | Q(content__icontains=query) | Q(tags__name__icontains=query)
).distinct()

2. View

A dedicated search view (SearchResultsView) processes queries from the search form and returns matching posts.

3. Templates

search_results.html displays all posts that match the search query.

Shows results dynamically based on user input.

4. URLs

Search functionality mapped at:

path("search/", views.SearchResultsView.as_view(), name="search-results"),

✅ Permissions

Only authenticated users can create, update, or delete posts and comments.

Any visitor (authenticated or not) can view posts, tags, and perform searches.

🧪 Testing

Tagging

Create/edit a post with one or more tags.

Click on a tag to view all posts associated with it.

Search

Enter a keyword in the search bar (matches title, content, or tags).

Confirm results show correctly.

📂 File Changes Summary

models.py: Added Tag model and tags field to Post.

forms.py: Updated PostForm with tags field.

views.py: Added search view and tag-based filtering.

urls.py: Added routes for tags and search.

Templates: Updated post form, detail, list, and created search_results.html.

💡 Usage

To add tags: Select one or more tags while creating/editing a post.

To search: Type a keyword in the search bar (title, content, or tags) and view results instantly.