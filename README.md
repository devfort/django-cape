# CAPE Cautious Approach to Progressive Enhancement

A template that makes it easier to write sophisticated progressive enhancement, while keeping style rules in CSS without having to blatter them in Javascript. Also provides some standard blocks in the Django template language that we think you'll like.

What you need to know:

0. Add 'django_cape' to your `INSTALLED_APPS`, and extend `cape/shell.html`.

1. Set up Javascript variables in `javascript-variables`.

2. Pull in libraries in `javascript-libraries`.

3. Apply progressive enhancement in `javascript-enhance`.

4. Asynchronous code, analytics and further behavioural changes (eg form submission) will generally go in `javascript-asynchronous`.

5. If your primary language is not British English, override `html-lang`.

6. If you need to add attributes to the `<html>` element, put them in `html-attributes`.

7. Add your normal page content in `body-sheath`.

When everything runs smoothly, the CSS flow is as follows:

1. `html`: initial state
2. `html.js-capable`: script capability detected during load (can be useful to hide things that are being enhanced)
3. `html.js-ready`: libraries are loaded and your enhancement code has run

When things go wrong, the CSS flow is as follows:

1. `html`: initial state
2. `html.js-capable`: script capability detected during load (can be useful to hide things that are being enhanced)
3. `html.js-timeout`: Javascript error or page load cancellation means that not all enhancement code has run (or maybe none has)
         
Generally you use `.js-capable` to hide stuff, `.js-timeout` to show it again, and don't actually use `.js-ready` for very much as you'll actually add `.enhanced` or something while running your code, or during jQuery plugin initialisation. If you can hide any enhanced content and show the non-enhanced versions, you can recover entirely; if you enhance content in-place then it may be harder for you to recover from Javascript failure. (Which may teach you to be sparing in your use of such techniques.)

## `cape/base.html`

Although CAPE is primarily about better progressive enhancement, we also provide a template with recommended slots for the `<head>` of your pages, which
you use by extending `cape/base.html` instead of `cape/shell.html`. It contains the following blocks:

* `head-title-website`: name of the website
* `head-title-page`: title of the page
* `head-title`: override if you need more control over the `<title>` tag
* `head-html5shim`: included by default, override if you don't want it
* `head-viewport`: set to `device-width` with a scale of 1 by default, override if you hate mobile users
* `head-meta`: where to put any other `<meta>` tags
* `head-icons`: where to declare your favicons and Apple touch icons
* `head-links`: where to put `<link>` tags, such as `rel=canonical`
* `head-alternate`: where to put your Atom feeds
* `head-css-stylesheet`: where to put the `<link>` to your stylesheet
* `head-css-localstyles`: where to put page-specific CSS links or blocks
* `head-css`: override if you need more control over styles

## Contact

CAPE was developed by Mark Norman Francis and James Aylett. Get in touch via our project page on github: <https://github.com/devfort/django-cape>.
