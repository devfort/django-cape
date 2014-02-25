# CAPE Cautious Approach to Progressive Enhancement

A template that makes it easier to write sophisticated progressive enhancement, while keeping style rules in CSS without having to blatter them in Javascript. Also provides some standard blocks in the Django template language that we think you'll like.

What you need to know:

0. Add 'django_cape' to your `INSTALLED_APPS`, and extend `cape/shell.html`.

1. Set up Javascript variables in `javascript-variables`.

2. Pull in libraries in `javascript-libraries`.

3. Apply progressive enhancement in `javascript-enhance`.

4. Asynchronous code, analytics and further behavioural changes (eg form submission) will generally go in `javascript-asynchronous`.

5. If your primary language is not British English, override `html-lang`.

When everything runs smoothly, the CSS flow is as follows:

1. `html`: initial state
2. `html.js-capable`: script capability detected during load (can be useful to hide things that are being enhanced)
3. `html.js-ready`: libraries are loaded and your enhancement code has run

When things go wrong, the CSS flow is as follows:

1. `html`: initial state
2. `html.js-capable`: script capability detected during load (can be useful to hide things that are being enhanced)
3. `html.js-timeout`: Javascript error or page load cancellation means that not all enhancement code has run (or maybe none has)
         
Generally you use `.js-capable` to hide stuff, `.js-timeout` to show it again, and don't actually use `.js-ready` for very much as you'll actually add `.enhanced` or something while running your code, or during jQuery plugin initialisation. If you can hide any enhanced content and show the non-enhanced versions, you can recover entirely; if you enhance content in-place then it may be harder for you to recover from Javascript failure. (Which may teach you to be sparing in your use of such techniques.)

## Contact

CAPE was developed by Mark Norman Francis and James Aylett. Get in touch via our project page on github: <https://github.com/devfort/django-cape>.
