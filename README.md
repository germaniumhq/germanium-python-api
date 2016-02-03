germanium
=========

Germanium is a set of extensions on top of the regular WebDriver API, allowing
for a super easy creation of tests. It's opensource and free.

Simply put Germanium is a Web Testing API that doesn't suck.

Here is some draft documentation: [doc/api/index.adoc](doc/api/index.adoc)

ChangeLog
---------

* 2016-01-28  1.3.4  *BugFix* Detect if the node is an element, by nodeType and not instanceof. (Fixes Chrome issues)
* 2016-01-26  1.3.3  *BugFix* Fixed the `type_keys` implementation for IE.
* 2016-01-25  1.3.2  *BugFix* `S` locator doesn't throw when is not finding elements.
* 2016-01-25  1.3.1  *BugFix* Release script.
* 2016-01-25  1.3.0  Added `S` super locator.
* 2016-01-25  1.2.0  Added `wait` utility function. Added a bunch of tests.
* 2015-12-03  1.1.1  Fixed returning `dict` object instead of `WebElement` under python 3.4.
* 2015-11-30  1.1.0  Added `type_keys` API.
* 2015-11-30  1.0.1  PIP deployment fix for python 3.4.

