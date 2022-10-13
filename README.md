# pdtest

Django test task. Key points

1. Created profile app (first name, last name, data of birth, biography, contacts). Used fixtures.

2. Added authentication for this page.

3. Created middleware that stores all requests and execution time.

4. Created template context processor that add django.conf.settings to context (add randome variable to template).

5. Created a page where user may change his profile.

6. Worked with forms-widgets - assigned calendar widget to "date of birth" field.

* Saving IP of user who makes edit.

7. Worked with template-tags - created template tag, that gets any model object, and renders a link of change view in admin interface ( for example: {% edit_list request.user %}).

8. Worked with commands - created django command that prints all models and object counts (made it only for profile model).

9. Worked with signals - created signal handler, that creates a note in database when every model is created/edited/deleted.