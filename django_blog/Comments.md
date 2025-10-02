# Comment System — Documentation

## Overview
The blog has a comment system that allows authenticated users to add comments to posts, and comment authors to edit or delete their own comments. All users (including anonymous) can read comments.

## Data model
`Comment` model fields:
- `post` (ForeignKey to Post) — the post the comment belongs to.
- `author` (ForeignKey to User) — who wrote the comment.
- `content` (TextField) — the comment body.
- `created_at` (DateTimeField auto_now_add) — when the comment was created.
- `updated_at` (DateTimeField auto_now) — when the comment was last edited.

Access comments via `post.comments.all()`.

## Forms
- `CommentForm` (ModelForm) exposes the `content` field and provides a textarea widget.

## Views & URLs
- `post/<int:post_pk>/comment/new/` — `CommentCreateView` — create a comment for post with pk=`post_pk`. Requires login.
- `comment/<int:pk>/edit/` — `CommentUpdateView` — edit the comment with pk=`pk`. Author only.
- `comment/<int:pk>/delete/` — `CommentDeleteView` — delete the comment with pk=`pk`. Author only.

The `PostDetailView` includes a `CommentForm()` in its context so an inline comment form can be shown below the post content.

## Templates
- `blog/post_detail.html` shows:
  - Existing comments for the post (via `post.comments.all()`).
  - Inline comment form for authenticated users (`{{ form }}` provided by `PostDetailView`).
  - Edit/Delete links for comments visible only to the comment author.
- `blog/comment_form.html` — used by comment create/update views (fallback).
- `blog/comment_confirm_delete.html` — used by comment delete view.

## Permissions
- Creating comments: authenticated users only.
- Editing/deleting comments: only the comment author (enforced with `UserPassesTestMixin`).
- Viewing comments: everyone.

## How to test locally
1. Run migrations and start the server:
