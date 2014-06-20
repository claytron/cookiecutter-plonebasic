# Cookiecutter For Plone?

An experiment to try out [cookiecutter](https://github.com/audreyr/cookiecutter) for Plone usage.

If you want to try it out, do the following:

    $ mkvirtualenv cookies
    (cookies)$ pip install cookiecutter
    (cookies)$ cookiecutter https://github.com/claytron/cookiecutter-plonebasic

This will generate the package, which right now won't actually work if loaded into Plone.

## Verdict

No.

Reasons:

- No validation of user input
- No way of coercing the user input into a specific type. For example,
  if you want to have a question be an `int`. The prompt will force it
  to be a `string`. This means having to do logic in each template to
  force it into an `int`.
- No simple way of handling package namespacing
- No idea of structures like we are used to in templer. This would have
  to be done in a `post_gen_project` script.
- Prompt is very simple. Keys from the `cookiecutter.json` are shown
  directly, with no way of giving a prettified question. Also, no way of
  giving any help text.
